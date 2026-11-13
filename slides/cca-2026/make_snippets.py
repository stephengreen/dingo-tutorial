"""Regenerate config snippets for the slides from a tagged dingo release.

Usage: python make_snippets.py /path/to/dingo/clone [tag]   (default tag: v0.10.3)
"""
import re
import subprocess
import sys
from pathlib import Path

if len(sys.argv) < 2:
    sys.exit(__doc__)
REPO = sys.argv[1]  # a local clone of https://github.com/dingo-gw/dingo with tags
TAG = sys.argv[2] if len(sys.argv) > 2 else "v0.10.3"
OUT = Path(__file__).parent / "snippets"


def show(path):
    return subprocess.run(["git", "-C", REPO, "show", f"{TAG}:{path}"], check=True, capture_output=True, text=True).stdout


def section(text, key):
    """Top-level YAML section `key:` up to the next top-level key."""
    m = re.search(rf"^{key}:.*?(?=^\S|\Z)", text, flags=re.S | re.M)
    return m.group(0).rstrip() + "\n"


CAP = 60  # characters that fit in a half-slide code panel at 20.5px


def fit(line, cap=CAP):
    """Fit a line to the panel: drop a trailing comment if too long, then elide visibly."""
    if len(line) <= cap:
        return line
    code = re.sub(r"\s+#.*$", "", line)
    if len(code) <= cap:
        return code
    return code[: cap - 1].rstrip() + "…"


def write(name, lang, body, trim=True):
    """Write a fenced code block. With trim, drop blank and comment-only lines (and INI section rules)."""
    lines = body.rstrip().splitlines()
    if trim:
        lines = [l for l in lines if l.strip() and not l.lstrip().startswith("#")]
    lines = [fit(l) for l in lines]
    (OUT / f"{name}.md").write_text(f"```{lang}\n" + "\n".join(lines) + "\n```\n")


npe = "examples/npe_model"
train = show(f"{npe}/train_settings.yaml")
write("waveform_dataset", "yaml", show(f"{npe}/waveform_dataset_settings.yaml"))
write("asd_dataset", "yaml", show(f"{npe}/asd_dataset_settings.yaml"))
def flow_list(text, key):
    """Collapse a YAML block list under `key` into a flow-style list, to save lines."""
    m = re.search(rf"^(\s*){key}:\s*\n((?:\1  - .*\n|\1- .*\n)+)", text, flags=re.M)
    items = [l.split("- ", 1)[1].strip() for l in m.group(2).splitlines()]
    head = f"{m.group(1)}{key}: ["
    lines, cur = [], head
    for i, it in enumerate(items):
        piece = it + ("]" if i == len(items) - 1 else ", ")
        if len(cur) + len(piece) > 66 and cur.strip() not in (head.strip(),):
            lines.append(cur.rstrip())
            cur = " " * len(head)
        cur += piece
    lines.append(cur)
    return text.replace(m.group(0), "\n".join(lines) + "\n")


write("train_data", "yaml", flow_list(flow_list(section(train, "data"), "inference_parameters"), "detectors"))
write("train_data_model", "yaml", section(train, "data") + "\n# Model architecture\n" + section(train, "model"))
write("train_model", "yaml", section(train, "model"))
write("train_training", "yaml", section(train, "training"))
write("train_local", "yaml", section(train, "local"))
ini = show(f"{npe}/GW150914.ini")
write("pipe_ini", "ini", "\n".join(l for l in ini.splitlines() if l.strip()))

t1 = show("examples/dingo_t1/train_settings.yaml")
tok = re.search(r"^  tokenization:.*?(?=^  \S|^\S)", t1, flags=re.S | re.M).group(0)
write("t1_tokenization", "yaml", "data:\n  ...\n" + tok)
write("t1_local", "yaml", section(t1, "local"))
t1_ini = show("examples/dingo_t1/GW150914.ini")
keep = [l for l in t1_ini.splitlines() if re.match(r"^(channel-dict|minimum-frequency|maximum-frequency|psd-notch-dict)\s*=", l)]
write("t1_ini", "ini", "\n".join(keep))
print("wrote", sorted(p.name for p in OUT.glob("*.md")))

# Binary neutron stars: prior conditioning (training) and proxy / scan (inference)
bns = show("examples/binary_neutron_stars/train_settings.yaml")
cpc = re.search(r"^  chirp_prior_conditioning:.*?(?=^  \S)", bns, flags=re.S | re.M).group(0)
write("bns_train", "yaml", "data:\n  ...\n" + cpc + "  inference_parameters: [delta_chirp_mass, mass_ratio, ...]\n")
bns_ini = show("examples/binary_neutron_stars/GW170817.ini")
keep = [l for l in bns_ini.splitlines() if re.match(r"^#?\s*(fixed-context-parameters|chirp-mass-scan)\s*=", l)]
write("bns_ini", "ini", "\n".join(keep), trim=False)

# Variable frequency ranges: the (commented-out) cropping block of the NPE example
m = re.search(r"^#  random_strain_cropping:\n(?:#    .*\n)+", train, flags=re.M)
crop = "\n".join(l[1:] for l in m.group(0).splitlines())
write("crop_train", "yaml", "data:\n  ...\n" + crop)
write("crop_ini", "ini", "minimum-frequency = {H1: 20, L1: 30}  # <= f_min_upper\nmaximum-frequency = 800  # >= f_max_lower")

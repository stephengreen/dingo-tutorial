```ini
local = True
request-cpus-importance-sampling = 64
sampling-requirements = [TARGET.CUDAGlobalMemoryMb>40000]
model = training/model_latest.pt
device = 'cuda'
num-samples = 50000
batch-size = 50000
recover-log-prob = true
prior-dict-updates = {
luminosity_distance = bilby.gw.prior.UniformComovingVolume(…
}
trigger-time = GW150914
label = GW150914
outdir = outdir_GW150914
channel-dict = {H1:GWOSC, L1:GWOSC}
psd-length = 128
plot-corner = true
plot-weights = true
plot-log-probs = true
```

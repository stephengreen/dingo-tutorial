# Tutorial: Introduction to DINGO

*Tutorial by [Annalena Kofler](https://github.com/annalena-k) ([original repository](https://github.com/annalena-k/tutorial-dingo-introduction)). This fork updates it for `dingo-gw` 0.10.3 and DINGO-T1, and adds the slides of the DINGO tutorial at CCA, Flatiron Institute (November 2026) in [`slides/cca-2026/`](slides/cca-2026/) (online: <https://stephenrgreen.com/dingo-tutorial/cca-2026/>).*

This tutorial provides a first introduction on how to use the [DINGO package](https://github.com/dingo-gw/dingo) for analyzing gravitational wave data using neural posterior estimation.
It illustrates at a 2D toy example how to train a DINGO model from scratch in a simplified setting. Furthermore, the tutorial shows how to download and use the pre-trained DINGO-T1 model to analyze an event with different detector configurations. 
With this tutorial, we hope to help people get started with DINGO easily.

## Getting started
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/stephengreen/dingo-tutorial/blob/main/DINGO_Tutorial.ipynb)

To get started quickly, run the tutorial in Google Colab by clicking the button above. 

To run it locally (which may be faster), create a Python environment with the `dingo-gw` package. The file `constraints.txt` pins the dependencies to the versions `dingo-gw` 0.10.3 was tested with (from its `uv.lock`). Without it, newer releases are installed; in particular, `bilby_pipe>1.8` is not yet compatible with `dingo_pipe`.

We recommend [`uv`](https://docs.astral.sh/uv/), which installs the tested versions from `uv.lock` (and fetches Python 3.12 if needed):
```
uv sync
uv run jupyter lab DINGO_Tutorial.ipynb
```

Alternatively, with `pip` (requires Python 3.11 or 3.12 for the constraints):
```
python3.12 -m venv dingo-venv
source dingo-venv/bin/activate
pip install dingo-gw==0.10.3 jupyterlab -c constraints.txt
```

If using `conda` (not tested with 0.10.3), this can be done with
```
conda create -c conda-forge -n venv-dingo dingo-gw jupyterlab
conda activate venv-dingo
```

You can start the jupyter server by executing the command `jupyter lab` in the folder containing the notebook which should open a new browser window. Finally, you can click on the jupyter notebook `DINGO_Tutorial.ipynb` and start with the tutorial!
(The notebook's install cell only runs on Colab.)

If you are looking for a more general introduction to posterior estimation of gravitational wave data without DINGO, please check out the tutorial ["GW Parameter Inference with Machine Learning"](https://github.com/stephengreen/gw-school-corfu-2023).

### Updates
* (13.11.2026) Updated to `dingo-gw==0.10.3`: new configuration keys and sampler API (`GWComposedSampler`); Section 6 now uses the pre-trained DINGO-T1 model. Tested locally (macOS, CPU); not yet tested on Colab.
* (03.06.2025) Updated to `dingo=0.8.3`; additional minor changes.
* (30.01.2025) Tutorial was updated to be compatible with `dingo` version 0.7.0

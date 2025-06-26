# Installing Python and Kinetics Toolkit

This section shows you how to install Python, its main scientific packages such as NumPy, Matplotlib, and the Kinetics Toolkit package.


:::{note}
While Kinetics Toolkit is available on both [conda-forge](https://anaconda.org/conda-forge/kineticstoolkit) and [PyPI](https://pypi.org/), we only support **conda-forge** in this guide since it facilitates the management of virtual environments.
:::

## Step 1 - Install a conda distribution

Download and install one of these conda distribution:
- [Miniforge](https://conda-forge.org/download)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

:::{note}
Both are mostly equivalent. In general, Miniforge installs packages faster because it comes with `mamba`. However, Miniconda is easier to install on macOS because it has a user-friendly installation wizard.
:::

## Step 2 - Install Kinetics Toolkit

These command create the `ktk` environment. We recommend installing in such a separate environment; this way, when you will mess up (we all do), you can simply delete and recreate the environment.

:::::{tab-set}

::::{tab-item} Using Miniforge
:::{card}
Open `Miniforge Prompt` (on Windows) or a terminal (on macOS) and type:
```
mamba create -n ktk kineticstoolkit spyder-kernels
```
:::
::::

::::{tab-item} Using Miniconda
:::{card}
Open `Anaconda Prompt` (on Windows) or a terminal (on macOS) and type:
```
conda create -n ktk -c conda-forge kineticstoolkit spyder-kernels
```
:::
::::
:::::


Press `y` to confirm and wait until the installation completes.

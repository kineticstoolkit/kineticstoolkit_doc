# Installing Python, Spyder and Kinetics Toolkit

This section shows you how to install Python, its main scientific packages such as NumPy, Matplotlib, the Spyder environment, and the Kinetics Toolkit package. Since all packages are available on conda-forge, then using mini-conda is the simplest and lightest installation method.

1. Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. It is recommended to create a separate environment, so that if you mess up at some point (we all do), you can just delete and recreate your environment. Open an Anaconda Prompt (on Windows) or a terminal (on macOS and Linux) and type:

```
conda create -n ktk -c conda-forge python spyder kineticstoolkit
```

From now on, to launch the Spyder environment:

::::{tab-set}

:::{tab-item} Windows
Click on the Spyder icon in the start menu.
:::

:::{tab-item} macOS and Linux
Open a terminal and type:

```
conda activate ktk
spyder
```
:::

::::

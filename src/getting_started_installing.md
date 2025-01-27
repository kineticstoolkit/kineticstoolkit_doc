# Installing Python and Kinetics Toolkit

This section shows you how to install Python, its main scientific packages such as NumPy, Matplotlib, and the Kinetics Toolkit package. Using **conda** facilitates creating virtual environments and is the preferred method in this guide.

:::{note}
Although we don't cover this installation method in this guide, everything is also available using **pip** for those who prefer managing their virtual environments manually.
:::

1. Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. It is recommended to create a separate environment so that if you mess up at some point (we all do), you can just delete and recreate your environment. Open an Anaconda Prompt (on Windows) or a terminal (on macOS and Linux) and type:

```
conda create -n ktk -c conda-forge kineticstoolkit spyder-kernels
```

Press `y` to confirm and wait until the installation completes.

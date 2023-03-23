---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```



# Installing Python, Spyder and Kinetics Toolkit

This section will show you how to install Python, its main scientific packages (NumPy, Matplotlib, etc.), the Spyder environment, and the Kinetics Toolkit package.

Since all packages are available on conda-forge, then using mini-conda is the simplest and lightest installation method.

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
Open a terminal, and type:

```
conda activate ktk
spyder
```
:::

::::
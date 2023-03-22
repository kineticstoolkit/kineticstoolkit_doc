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

Kinetics Toolkit is distributed via [conda](https://anaconda.org/conda-forge/kineticstoolkit) and [pip](https://pypi.org/project/kineticstoolkit). The source code is hosted on [GitHub](https://github.com/felixchenier/kineticstoolkit).

Since reading c3d files relies on [ezc3d](https://github.com/pyomeca/ezc3d) which binaries are distributed only via conda, the recommended installation method is to use conda. If needed, go to the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) to install a minimal conda installation.


:::{card} Summary
The are many ways to install Python. This section shows how to install the [Spyder integrated development environment](https://spyder-ide.org) in a conda environment.
:::

## 📄 Installing a conda distribution

Download and install Anaconda or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## 📄 Creating a virtual environment

It is recommended to create a separate environment, so that if you mess up at some point (we all do), you can just delete and recreate your environment. Open an Anaconda Prompt (on Windows) or a terminal (on macOS and Linux) and type these commands one by one. This will create a conda environment with the basic requirements to get started in scientific python, including [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/).

```
conda create -n ktk -c conda-forge python spyder kineticstoolkit
```

[Spyder](https://spyder-ide.org) is an open-source integrated development environment (IDE) that was created explicitely for a scientific use. To launch Spyder, select the Spyder icon on Windows, or enter a terminal on Mac and enter these commands:

```
conda activate ktk
spyder
```




## Installing and updating Kinetics Toolkit

In the Anaconda/Miniconda prompt or terminal:

```
conda install -c conda-forge kineticstoolkit
```

You can keep Kinetics Toolkit up to date by typing this command regularly:

```
conda update -c conda-forge kineticstoolkit
```



## Interactive Matplotlib graphics

Kinetics Toolkit's interactive functions make use of IPython's integration of matplotlib's event loop. When you want to use interactive functions in IPython such as panning and zooming plots, editing events, or visualizing 3d points, type:

```
%matplotlib qt5
```

before importing anything. Alternatively, we recommend installing the [Spyder](https://www.spyder-ide.org/) development environment because of its strong orientation towards science. Kinetics Toolkit is developed on Spyder. See [](python_configuring_spyder.md) to see different recommended settings in Spyder, such as removing the requirement to type `%matplotlib qt5`.


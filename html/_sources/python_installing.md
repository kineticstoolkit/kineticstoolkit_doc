# Installing Python, Spyder and the most important scientific packages

The are many ways to install Python. To start without installing anything, you could use this [online virtual environment](https://repl.it/languages/Python3) where you can write python commands and see their direct effect. However, at one point, you will need to install Python and its scientific environment on your computer. This manual shows how to install the [Spyder integrated development environment](https://spyder-ide.org) in a conda environment.

## Installing a conda distribution

Download and install Anaconda or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Creating a virtual environment

It is recommended to create a separate environment, so that if you mess up at some point (we all do), you can just delete and recreate your environment. Open an Anaconda Prompt (on Windows) or a terminal (on macOS and Linux) and type these commands one by one.

This will create a conda environment with the basic requirements to get started in scientific python, including [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/).

```
conda create -n ktk -c conda-forge python spyder kineticstoolkit
```

[Spyder](https://spyder-ide.org) is an open-source integrated development environment (IDE) that was created explicitely for a scientific use. To launch Spyder, you can select the Spyder icon on Windows, or enter a terminal on Mac and enter these commands:

```
conda activate ktk
spyder
```

# Installing Python and Spyder

There exist a great lot of ways to install Python. To start without installing anything, you could use this [online virtual environment](https://repl.it/languages/Python3) where you can write python commands and see their direct effect.

At one point, you will need to install Python and its scientific environment on your computer. In our lab, we mainly use the Spyder integrated development environment (IDE), in a conda environment. This is what we suggest in this guide:

## Installing a conda distribution

Download and install Anaconda or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Creating a virtual environment

It is recommended to create a separate environment, so that if you mess up at some point (we all do), you can just delete and recreate your environment. Open an Anaconda Prompt (on Windows) or a terminal (on macOS and Linux) and type these commands one by one.

This will create a conda environment with the basic requirements to get started in scientific python.

```
conda create -n ktk
conda activate ktk
conda install -c conda-forge python=3.8 numpy matplotlib scipy spyder
```

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

# Installing and importing

Kinetics Toolkit is distributed via both [conda-forge](https://anaconda.org/conda-forge/kineticstoolkit) and [PyPi](https://pypi.org/project/kineticstoolkit). The source code is hosted on [GitHub](https://github.com/felixchenier/kineticstoolkit).

Since reading c3d files relies on [ezc3d](https://github.com/pyomeca/ezc3d) which binaries are distributed only via conda-forge, the recommended installation method is therefore using conda-forge. If needed, go to the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) to install a minimal conda installation.

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

Kinetics Toolkit's interactive functions make use of IPython's integration of Matplotlib/Qt5's event loop. When you want to use interactive functions in IPython, type:

```
%matplotlib qt5
```

before importing anything. Alternatively, we recommend installing the [Spyder](https://www.spyder-ide.org/) development environment because of its strong orientation towards science. Kinetics Toolkit is developed on Spyder. See [](python_configuring_spyder.md) to see different recommended settings in Spyder, such as removing the requirement to type `%matplotlib qt5`.

## Importing Kinetics Toolkit

There are two ways to import Kinetics Toolkit:

- In standard mode: `import kineticstoolkit as ktk`
- In lab mode: `import kineticstoolkit.lab as ktk`

:::{note}
The first import can take several seconds; subsequent imports are much faster.
:::

Lab mode is a convenience tool that sets some defaults for a more enjoyable data processing session in IPython-based environments such as Spyder. It automatically imports all installed [extensions](extensions.md), makes cosmetics changes to the representations (repr) of dictionaries, arrays and warnings, and improves Matplotlib defaults colours and sizes for interactive biomechanics work. See [](api/ktk.import_extensions.rst) and [](api/ktk.change_defaults.rst) for more information.

```
import kineticstoolkit.lab as ktk
```

is equivalent to:
```
import kineticstoolkit as ktk
ktk.import_extensions()
ktk.change_defaults()
```

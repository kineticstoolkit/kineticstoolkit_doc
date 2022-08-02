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

## Configuring Matplotlib graphics in IPython/Spyder

Kinetics Toolkit's interactive functions make use of IPython's integration of Matplotlib/Qt5's event loop. When you want to use interactive functions in IPython, type:

```
%matplotlib qt5
```

beforehand.

Alternatively, installing the [Spyder](https://www.spyder-ide.org/) development environment is recommended, because of its strong orientation towards science. Kinetics Toolkit is developped using Spyder.

To configure Spyder for interactive graphics, go to the Spyder's preferences, to the **IPython console** item, then to the **Graphics** pane. In the **Graphics backend** box, select **Qt5**, then restart Spyder.

# Importing Kinetics Toolkit

There are two ways to import Kinetics Toolkit:

- In standard mode: `import kineticstoolkit as ktk`
- In lab mode: `import kineticstoolkit.lab as ktk`

:::{note}
The first import can take several seconds; subsequent imports are much faster.
:::

These modes are very similar, with lab mode being simply a convenience that makes scientific research more enjoyable in IPython-based environments (see below for details).

## When to use lab mode

**Use it** if you want to use Kinetics Toolkit as an integrated work environment using IPython based environments (Spyder, Jupyter) in a biomechanics research labs. If you're not sure, use lab mode.

    >>> import kineticstoolkit.lab as ktk

**Do not use it** if you already have a working environment and you simply want to use some ktk classes or functions within your own setup, and you don't want ktk to mess with your defaults.

    >>> import kineticstoolkit as ktk

## What lab mode does

**1. Automatic import of extensions**

Importing in lab mode automatically imports all installed [extensions](extensions.md). In standard mode, we need to manually import the extensions using [ktk.import_extensions()](api/kineticstoolkit.import_extensions.rst).

**2. Modification to repr of dictionaries**

Kinetics Toolkit often stores data as nested dictionaries, which can lead to very large printouts when we simply want to see the dictionary's contents. Importing ktk in lab mode simplifies the printout. For example:

```{code-cell} ipython3
import numpy as np
data = dict()
data["data1"] = np.arange(30)
data["data2"] = np.arange(30) ** 2
```

The default dict printout is:

```{code-cell} ipython3
data
```

Lab mode's dict printout is:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

data
```

**3. Modification to warnings format**

Lab mode pretty-prints warnings so they are a bit clearer.

**4. Modification to repr of numpy's floats**

Numpy is set to display floats with floating point precision.

**5. Alternative defaults for matplotlib**

The dpi and figure size are optimized for interactive work in default matplotlib figures. Additionally, the default color order is changed to (rgbcmyko). The first colors, (rgb) are consistent with the colours assigned to x, y and z in most 3D visualization softwares.

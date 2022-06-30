---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# Importing Kinetics Toolkit

There are two ways to import Kinetics Toolkit:

- In standard mode: `import kineticstoolkit as ktk`
- In lab mode: `import kineticstoolkit.lab as ktk`

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

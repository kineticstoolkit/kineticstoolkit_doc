---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

# 📖 Importing NumPy

:::{card} Summary
This section introduces the concept of a package and how to import its contents.
:::

NumPy, as many other libraries such as [Matplotlib](matplotlib.md) or [Pandas](pandas.md), is a package that needs to be installed alongside Python. Please refer to section [](python_installing.md) to install it.

Once a package is installed, we need to tell Python to import its contents, each time we want to access it. This is usually done at the beginning of each Python file where we need the package, using the `import` statement.

For NumPy, we would write:

```{code-cell}
import numpy
```

If there is no error, then the package is correctly imported. From now on, we can access anything from the Numpy library by using the `numpy` namespace:

```{code-cell}
numpy.mean([1.0, 2.0, 3.0])
```

:::{note}
A **namespace** is a name that groups different functions, variables, classes, etc. It is used to avoid ambiguities between two module that could have used similar names to define two objects. For instance, Python provides the function `max` that returns the maximum value between two floats. NumPy also provides a function `max` that returns the maximum value of an array. Using namespaces avoid name clashes: Python's is accessed using `max()` and NumPy's max is accessed using `numpy.max()`.
:::

Since a typical code uses NumPy a lot, it is convenient and very common to import it using an alias:

```{code-cell}
import numpy as np
```

This line does exactly the same thing as the first one, but NumPy is imported into the `np` namespace instead of the `numpy` namespace. The only advantage is to shorten the length of the code lines, `np` being only two letter long.

```{code-cell}
np.mean([1, 2, 3])
```


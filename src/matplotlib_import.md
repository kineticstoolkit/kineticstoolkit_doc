---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Importing **pyplot**

Matplotlib, as many other libraries such as {{numpy}} or {{pandas}}, is a package that needs to be installed alongside Python. Normally, it should already be installed in your setup; it not, please refer to section [getting_started_installing](getting_started_installing.md) to install it.

Once a package is installed, we need to tell Python to import its contents. This is usually done at the beginning of the Python file where we need the package, using the `import` statement. For the {{pyplot}} module of the {{matplotlib}} package, we would write:

```{code-cell} ipython3
import matplotlib.pyplot
```

Once imported, we can access this module's contents under the `matplotlib.pyplot` namespace:

```{code-cell} ipython3
matplotlib.pyplot.plot([0, 1, 4], "o-");
```

:::{note}
A **namespace** is a name that groups different objects (functions, variables, classes). It is used to avoid ambiguities between two modules that could use identical names to define their respective objects.

For instance, Python provides the function `max` that returns the maximum value between two floats. NumPy also provides a function `max` that returns the maximum value of an array. Namespaces avoid name clashes: Python's max is accessed using `max()` while NumPy's max is accessed using `numpy.max()`.
:::

To avoid typing `matplotlib.pyplot` each time we need a pyplot function, it is convenient and very common to import it using an alias:

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

This line behaves like the previous import, but this time `matplotlib.pyplot` is imported into the `plt` namespace instead of the `matplotlib.pyplot` namespace. This leads to shorter lines of code:

```{code-cell} ipython3
plt.plot([0, 1, 4], "o-");  # instead of matplotlib.pyplot.plot([0, 1, 4], "o-")
```

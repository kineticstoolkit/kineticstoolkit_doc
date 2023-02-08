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

# 📖 Importing `pyplot`

:::{card} Summary
This section introduces the concept of a package and how to import its contents.
:::

Matplotlib, as many other libraries such as [](numpy.md) or [](pandas.md), is a package that needs to be installed alongside Python. Normally, it should already be installed in your setup; it not, please refer to section [](python_installing.md) to install it.

Once a package is installed, we need to tell Python to import its contents, each time we want to access it. This is usually done at the beginning of each Python file where we need the package, using the `import` statement.

For the {{pyplot}} module of the {{matplotlib}} package, we would write:

```{code-cell} ipython3
import matplotlib.pyplot
```

If there is no error, then the package is correctly imported. From now on, we can access anything from Matplotlib's pyplot module using the `matplotlib.pyplot` namespace:

```{code-cell} ipython3
matplotlib.pyplot.plot([0, 1, 4], "o-")
```

:::{note}
A **namespace** is a name that groups different functions, variables, classes, etc. It is used to avoid ambiguities between two module that could have used similar names to define two objects.

For instance, Python provides the function `max` that returns the maximum value between two floats. NumPy also provides a function `max` that returns the maximum value of an array. Using namespaces avoid name clashes: Python's is accessed using `max()` and NumPy's max is accessed using `numpy.max()`.
:::

Since it would be tedious to type `matplotlib.pyplot` each time we want to access a pyplot function, it is convenient and very common to import it using an alias:

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

This line does exactly the same thing as the first one, but `matplotlib.pyplot` is imported into the `plt` namespace instead of the `matplotlib.pyplot` namespace.

```{code-cell} ipython3
plt.plot([0, 1, 4], "o-")
```

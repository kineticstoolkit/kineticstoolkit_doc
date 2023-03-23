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

# Line plots

## Plotting a series

The most common command of Matplotlib's pyplot module is probably {{plt_plot}}. This function plots series expressed either as [standard Python lists](python_lists.md), as [NumPy Arrays](numpy_ndarray.md) or as `Pandas DataFrames`. For unidimensional data, it takes one list (y) or two lists (x, y) as arguments, and plots it as a line graph.

For exemple, to plot this list: `[0.0, 1.0, 4.0, 3.0, -2.0]`:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y = [0.0, 1.0, 4.0, 3.0, -2.0]
plt.plot(y)

plt.show()  # Usually unnecessary in Spyder and Jupyter
```

By default, `x` starts at 0 and increments by 1 for each point. But we can also specify custom coordinates for `x`:

```{code-cell} ipython3
x = [0.0, 5.0, 10.0, 15.0, 20.0]
plt.plot(x, y)

plt.show()
```

The `x` values don't have to be equidistant:

```{code-cell} ipython3
x = [0.0, 0.5, 1, 10, 500]
plt.plot(x, y)

plt.show()
```

## Plotting multiple series

Many series can be plotted on the same figure, simply by calling `plt.plot` multiple times:

```{code-cell} ipython3
x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
```

:::{tip}
By default, any new plot is added to the same figure. To generate new figures, you have the following options:

- `plt.figure()`: The {{plt_figure}} function prepares a new, empty figure that will be used for each subsequent plot, leaving the original one intact.
- `plt.clf()`: The {{plt_clf}} function **cl**ears the current **f**igure.
:::

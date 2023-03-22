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

:::{card} Summary
This section shows:

- how to generate line plots using {{plt_plot}};
- how to add axis labels using {{plt_xlabel}} and {{plt_ylabel}};
- how to add a title using {{plt_title}};
- how to add a legend using {{plt_legend}};
- how to add a grid using {{plt_grid}};
- how to create new figures or clear figures using {{plt_figure}} and {{plt_clf}}.
:::

## 📄 Plotting a series

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

## 📄 Plotting multiple series

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

## 📄 Title, axis labels, legend and grid

The figure above is nice, but it lacks axes and a legend, maybe a grid, and also a title. These elements are added using the following functions:

```{code-cell} ipython3
plt.plot(x, y1)
plt.plot(x, y2)

# Add axis labels
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (m)")

# Add a legend (same order as the plt.plot functions above)
plt.legend(["Instrument 1", "Instrument 2"])

# Add a title
plt.title("Comparing a same measurement using two instruments")

# Add a grid
plt.grid(True)

plt.show()
```

:::{good-practice} Legend labels
Another, less error-prone way to add legends is to define the labels at plot time. Instead of:

```
plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(["Instrument 1", "Instrument 2"])
```

we do:

```
plt.plot(x, y1, label="Instrument 1")
plt.plot(x, y2, label="Instrument 2")
plt.legend()
```

Both methods give the same results, but in the first one, the legend may be wrong if we add or remove `plt.plot` calls without updating the `plt.legend` call. In the second one, the legend always matches what is displayed on the figure.
:::

## 💪 Exercise 1

Using a video camera, you recorded the position of a sprinter each 2 seconds. The recorded data are:

```{code-cell} ipython3
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters
```

Write a code that produce this figure:

```{code-cell} ipython3
:tags: [remove-input]

plt.plot(t, p)
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.show()
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

plt.plot(t, p)
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
```

## 💪 Exercise 2

During the same race, you also used five timing gates placed at positions 0m, 25m, 50m, 75m and 100m. The time recorded by these timing gates are:

```{code-cell} ipython3
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]
```

Write a code that produces this figure:

```{code-cell} ipython3
:tags: [remove-input]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True)
plt.show()
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend(["Video camera", "Timing gates"])
```

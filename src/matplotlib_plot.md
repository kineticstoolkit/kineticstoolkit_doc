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

The most common command of Matplotlib's pyplot module is probably {{plt_plot}}. This function plots one or many series expressed either as [standard Python lists](python_lists.md), as [NumPy Arrays](numpy_ndarray.md), or as `Pandas DataFrames`. For one-dimensional data, it takes one list (y) or two lists (x, y) as arguments.

For example, to plot this list: `[1.0, 2.0, -1.0, -0.0]`:

```
import matplotlib.pyplot as plt

y = [1.0, 2.0, -1.0, -0.0]
plt.plot(y)
```

```{figure-md} fig_matplotlib_qt5
:width: 5in
![](_static/images/fig_matplotlib_qt5.png)

A Matplotlib figure window.
```

You should normally see the plot in a new window, as shown in {numref}`fig_matplotlib_qt5`. If, instead, you see the figure inline, or in Spyder's *Graph* pane, or not at all, then you probably did not configure Matplotlib for interactive graphics. See [](getting_started_configuring_spyder.md).

The different buttons on the figure allow some interaction with the plot:

|                      Icon                       | Function                         |
| :---------------------------------------------: | -------------------------------- |
|     ![](_static/images/matplotlib_move.png)     | Move the figure around (panning) |
| ![](_static/images/matplotlib_zoom_to_rect.png) | Zoom                             |
|     ![](_static/images/matplotlib_back.png)     | Undo the last pan/zoom operation |
|   ![](_static/images/matplotlib_forward.png)    | Redo the last pan/zoom operation |
|     ![](_static/images/matplotlib_home.png)     | Reset to the initial pan/zoom    |
|   ![](_static/images/matplotlib_filesave.png)   | Save the figure to an image file |

By default, `x` starts at 0 and increments by 1 for each point. But we can also specify custom coordinates for `x`:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y = [1.0, 2.0, -1.0, -0.0]
x = [0.0, 5.0, 10.0, 15.0]

plt.plot(x, y);
```

The `x` values don't have to be equidistant:

```{code-cell} ipython3
x = [0.0, 0.5, 1, 10]

plt.plot(x, y);
```

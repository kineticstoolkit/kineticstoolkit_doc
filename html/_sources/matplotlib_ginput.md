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

# Graphical input

Matplotlib provides extensive options to interact with figures, with different levels of complexity. One of the most helpful (and also the most basic) is {{plt_ginput}}. It lets the user click on a number of points on the figure, and then returns these coordinates. For instance, these instructions:

```
import matplotlib.pyplot as plt

plt.plot([0.0, 1.0, -1.0, 2.0, 0.5, 0.0])
points = plt.ginput(10)  # 10 points
```

generate {numref}`fig_matplotlib_ginput` and let the user click a maximum of 10 points.

```{figure-md} fig_matplotlib_ginput
:width: 5in
![plt.ginput -width:wider](_static/images/fig_matplotlib_ginput.png)

Clicking and retrieving coordinates using plt.ginput.
```


- Left-click adds a point (red cross);
- Right-click removes the last added point;
- Middle-click stops and returns the current points.

The function then returns the point coordinates as a list of (x, y) tuples.

```{code-cell} ipython3
:tags: [remove-cell]

points = [
    (0.44858870967741926, 0.003571428571428781),
    (1.1693548387096775, 0.42321428571428577),
    (2.089717741935484, 0.6107142857142862),
    (3.5756048387096775, 0.8339285714285718),
]
```

```{code-cell} ipython3
points
```


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

# Multiple plots side by side

In some situations, it is useful to show multiple plots side by side in a same figure. This can be done using the {{plt_subplot}} function, which splits a figure in a grid, and specifies the location of the next plot on this grid. Its arguments are:

1. The number of lines (int);
2. The number of columns (int);
3. The location of the next plot, starting at 1 in the upper left corner, then going left to right then up to down:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5, 0.5, f"Location {i+1}", ha="center", va="center")
plt.tight_layout()
```

For instance, to spread five plots on two lines and three columns:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y1 = [1.0, 2.0, 3.0, 1.0]
y2 = [1.0, 3.0, -1.0, 2.0]
y3 = [-1.0, 4.0, -2.0, 2.0]
y4 = [-1.0, -4.0, -3.0, 0.0]
y5 = [2.0, 3.0, -1.0, 1.0]

plt.subplot(2, 3, 1)
plt.plot(y1)
plt.title("First plot")

plt.subplot(2, 3, 2)
plt.plot(y2)
plt.title("Second plot")

plt.subplot(2, 3, 3)
plt.plot(y3)
plt.title("Third plot")

plt.subplot(2, 3, 4)
plt.plot(y4)
plt.title("Fourth plot")

plt.subplot(2, 3, 5)
plt.plot(y5)
plt.title("Fifth plot");
```

We can see that the titles of the second line overlaps with the horizontal axes of the first line. This is a common issue with Matplotlib: it does not know how to optimize the spacing while we progressively build the figure. Calling {{plt_tight_layout}} just after building the plot optimizes the spacing so that everything looks clean.

```{code-cell} ipython3
plt.subplot(2, 3, 1)
plt.plot(y1)
plt.title("First plot")

plt.subplot(2, 3, 2)
plt.plot(y2)
plt.title("Second plot")

plt.subplot(2, 3, 3)
plt.plot(y3)
plt.title("Third plot")

plt.subplot(2, 3, 4)
plt.plot(y4)
plt.title("Fourth plot")

plt.subplot(2, 3, 5)
plt.plot(y5)
plt.title("Fifth plot")

plt.tight_layout()
```

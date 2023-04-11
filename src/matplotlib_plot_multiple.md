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

# Plotting multiple series

Many series can be plotted on the same figure, simply by calling `plt.plot` multiple times:

```{code-cell} ipython3
import matplotlib.pyplot as plt


x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
```

By default, any new plot is added to the same figure. To generate new figures, you have the following options:

- `plt.figure()`: The {{plt_figure}} function prepares a new, empty figure that will be used for each subsequent plot, leaving the original one intact.
- `plt.clf()`: The {{plt_clf}} function **cl**ears the current **f**igure.

---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```


# Title, axis labels, legend and grid

In the previous sections, we learned how to plot one or many series:

```{code-cell} ipython3
import matplotlib.pyplot as plt


x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

plt.plot(x, y1)
plt.plot(x, y2);
```

This figure is nice, but it lacks axes and a legend, maybe a grid, and also a title. These elements are added using the following functions:

- {{plt_xlabel}}: Add a label for the horizontal (x) axis
- {{plt_ylabel}}: Add a label for the vertical (y) axis
- {{plt_legend}}: Add a legend to identify the series
- {{plt_title}}: Add a title to the graph
- {{plt_grid}}: Add a grid in the background


```{code-cell} ipython3
import matplotlib.pyplot as plt


x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

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
plt.grid(True);
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

Both methods give the same results, but in the the second one, the legend always matches what is displayed on the figure, even if we modified the number of `plt.plot` calls and forgot to update the `plt.legend` call accordingly.
:::

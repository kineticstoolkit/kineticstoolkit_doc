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

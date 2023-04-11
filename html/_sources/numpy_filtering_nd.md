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


# Filtering multidimensional arrays

In the previous section, we learned how to use lists of boolean and lists of integers to filter unidimensional arrays. This also works on multidimensional arrays, although filtering on axes other than the first one is somewhat unintuitive and may lead to unexpected array shapes. Luckily, in biomechanical data processing, filtering happens mainly on the first axis, which usually corresponds to time.

**Example 10: Read the marker's coordinates at samples 0 and 2**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(position, title="position")

# Highlight the second line
for i in range(4):
    tbl[0, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl[2, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
mask = [0, 2]

position[mask]
```


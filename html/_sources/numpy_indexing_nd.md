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


# Indexing multidimensional arrays

As for unidimensional arrays, we also index multidimensional arrays using integers in brackets. Using a single integer indexes the first dimension. For example:

**Example 1: Read the marker position at first sample**

```{code-cell} ipython3
:tags: [remove-input]

import ktkdoctools

tbl = ktkdoctools.draw_table(
    position,
    title="position",
)

# Highlight the first line
for i in range(4):
    tbl[0, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
```

```{code-cell} ipython3
position[0]
```

**Example 2: Read the marker position at second sample**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(
    position,
    title="position",
)

# Highlight the second line
for i in range(4):
    tbl[1, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)


plt.show()
```

```{code-cell} ipython3
:tags: []

position[1]
```

Look how indexing an array reduces its dimension by one. In the example above, we indexed the second row of a 2d array, which returned a 1d array that corresponds to the four columns of this row. Therefore, to also select a column, we can index the result:

**Example 3: Read the marker's z coordinate at second sample**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(position, title="position")
tbl[1, 2].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_1)
tbl[1, 0].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
tbl[1, 1].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
tbl[1, 3].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
plt.show()
```

```{code-cell} ipython3
position[1][2]
```

This is perfectly valid. However, we normally use another notation that groups the indexes together between the brackets using commas `,`:

```{code-cell} ipython3
position[1, 2]
```

Both notations are equivalent, but the second one is more powerful (as we will see in slicing). It makes it also clearer that we index one whole array, and not a list that is nested into another list.

**Example 4: Read the segment's orientation at second sample**

```{code-cell} ipython3
:tags: [remove-input]

plt.subplot(1, 2, 1)
tbl0 = ktkdoctools.draw_table(orientation[0], title="orientation[0]", width=5)

plt.subplot(1, 2, 2)
tbl1 = ktkdoctools.draw_table(orientation[1], title="orientation[1]", width=5)

# Highlight the whole second matrix
for i in range(4):
    for j in range(4):
        tbl1[i, j].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
# Orientation of the segment at second sample
orientation[1]
```

**Example 5: Read the 3rd line of the segment's orientation matrix at second sample**

```{code-cell} ipython3
:tags: [remove-input]

plt.subplot(1, 2, 1)
tbl0 = ktkdoctools.draw_table(orientation[0], title="orientation[0]", width=5)

plt.subplot(1, 2, 2)
tbl1 = ktkdoctools.draw_table(orientation[1], title="orientation[1]", width=5)

for i in range(4):
    tbl1[0, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl1[1, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl1[2, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_1)
    tbl1[3, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
orientation[1, 2]
```

**Example 6: Read 3rd line, 2nd column of the segment's orientation matrix at 2nd sample**

```{code-cell} ipython3
:tags: [remove-input]

plt.subplot(1, 2, 1)
tbl0 = ktkdoctools.draw_table(orientation[0], title="orientation[0]", width=5)

plt.subplot(1, 2, 2)
tbl1 = ktkdoctools.draw_table(orientation[1], title="orientation[1]", width=5)

for i in range(4):
    tbl1[0, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl1[1, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl1[2, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_1)
    tbl1[3, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

tbl1[2, 1].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_2)

plt.show()
```

```{code-cell} ipython3
orientation[1, 2, 1]
```

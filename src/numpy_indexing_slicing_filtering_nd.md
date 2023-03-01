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

# 📖 Indexing, slicing and filtering multidimensional arrays

:::{card} Summary
This section shows how to read or write single or multiple data in a multidimensional array, using indexing, slicing and filtering.
:::

In the previous section, we learned how to read one element of a unidimensional array using indexing, and how to read multiple elements of a unidimensional array using slicing and filtering. We will now generalize this to multidimensional arrays. Through this tutorial, we will use these two sample arrays:

**Sample array #1: Trajectory of a marker during three samples**

The position of a marker is expressed by three coordinates (x, y, z), usually followed by a constant of 1. A trajectory is expressed as a series of positions. Therefore, we express the trajectory of a marker using:

- Axis 0: sample
- Axis 1: coordinate

```{code-cell} ipython3
:tags: [remove-input]

import ktkdoctools
import numpy as np
import matplotlib.pyplot as plt

position = np.array(
    [
        [0.497, 0.973, 0.010, 1.0],
        [0.528, 0.973, 0.017, 1.0],
        [0.589, 0.970, 0.025, 1.0],
    ]
)

tbl = ktkdoctools.draw_table(
    position,
    title="position",
    col_labels=["x", "y", "z", "1"],
    row_labels=["Sample 0", "Sample 2", "Sample 3"],
)
```

```{code-cell} ipython3
import numpy as np

position = np.array(
    [
        [0.497, 0.973, 0.010, 1.0],
        [0.528, 0.973, 0.017, 1.0],
        [0.589, 0.970, 0.025, 1.0],
    ]
)

position
```

**Sample array #2: Series of segment orientation during two samples**

The orientation of a segment is expressed as a 4x4 homogeneous matrix. Therefore, we can express a series of orientations using:

- Axis 0: sample
- Axis 1: line of the homogeneous transform matrix
- Axis 2: column of the homogeneous transform matrix

```{code-cell} ipython3
:tags: [remove-input]

orientation = np.array(
    [
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [1.0, 0.000, 0.000, 0.0],
            [0.0, 0.999, -0.017, 0.0],
            [0.0, 0.017, 0.999, 0.0],
            [0.0, 0.000, 0.000, 1.0],
        ],
    ]
)

plt.subplot(1, 2, 1)
tbl0 = ktkdoctools.draw_table(
    orientation[0],
    title="orientation at sample 0",
    width=5,
    row_labels=["L0", "L1", "L2", "L3"],
    col_labels=["C0", "C1", "C2", "C3"],
)

plt.subplot(1, 2, 2)
tbl1 = ktkdoctools.draw_table(
    orientation[1],
    title="orientation at sample 1",
    width=5,
    row_labels=["L0", "L1", "L2", "L3"],
    col_labels=["C0", "C1", "C2", "C3"],
)

plt.show()
```

```{code-cell} ipython3
orientation = np.array(
    [
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [1.0, 0.000, 0.000, 0.0],
            [0.0, 0.999, -0.017, 0.0],
            [0.0, 0.017, 0.999, 0.0],
            [0.0, 0.000, 0.000, 1.0],
        ],
    ]
)

orientation
```

+++ {"tags": []}

## 📄 Indexing

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



## 📄 Slicing

We just learned how to index multidimensional matrices using indexes separated by commas. Slicing works the same way: for a given dimension, all we need is to use a slice instead of an index.

**Example 7: Read the marker's y coordinate at samples 0 and 1**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(position, title="position")

# Highlight the second line
for i in range(2):
    tbl[i, 1].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
position[0:2, 1]
```

**Example 8: Read the marker's y and z coordinates at samples 0 and 1**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(position, title="position")

# Highlight the second line
for i in range(2):
    for j in range(1, 3):
        tbl[i, j].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
position[0:2, 1:3]
```

:::{tip}
A slice can be as simple as a column operator `:`. This is a slice with no bound, which literally means from the beginning up to the end. In other words, "all data on this dimension".
:::

**Example 9: Read the marker's z coordinate at all samples**

```{code-cell} ipython3
:tags: [remove-input]

tbl = ktkdoctools.draw_table(position, title="position")

# Highlight the second line
for i in range(3):
    tbl[i, 2].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
```

```{code-cell} ipython3
position[:, 2]
```

## 📄 Filtering

In the previous section, we learned how to use lists of boolean and lists of integers to filter unidimensional arrays. This also works multidimensional arrays, although only the first dimension is intuitive (see {{np_ix_}} for more complex cases). Luckily, in biomechanical data processing, we filter mainly on the time axis, which is often the first dimensions.

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

Filtering an array is a very powerful method to select elements of an array based on a criteria. This will be seen later in section [](numpy_comparisons.md).

+++

## 💪 Exercise 1

#todo To be continued.

```{code-cell} ipython3

```

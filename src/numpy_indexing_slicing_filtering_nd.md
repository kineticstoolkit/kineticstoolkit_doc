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

# Indexing, slicing and filtering multidimensional arrays

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


## 💪 Exercise

We recorded this series of forces using a gait force platform, where the first axis corresponds to time and the second axis corresponds to the three force components $F_x$, $F_y$ and $F_z$.

```{code-cell} ipython3
forces = np.array(
    [
        [0.17619048, 0.82380952, 17.61904762],
        [0.21428571, 0.78571429, 21.42857143],
        [0.17619048, 0.82380952, 17.61904762],
        [0.17619048, 0.82380952, 17.61904762],
        [0.17619048, 0.82380952, 17.61904762],
        [0.32857143, 0.67142857, 32.85714286],
        [0.25238095, 0.74761905, 25.23809524],
        [0.17619048, 0.82380952, 17.61904762],
        [0.29047619, 0.70952381, 29.04761905],
        [0.32857143, 0.67142857, 32.85714286],
        [0.25238095, 0.74761905, 25.23809524],
        [0.21428571, 0.78571429, 21.42857143],
        [0.67142857, 0.32857143, 67.14285714],
        [8.1, -7.1, 810.0],
        [8.70952381, -7.70952381, 870.95238095],
        [8.02380952, -7.02380952, 802.38095238],
        [7.26190476, -6.26190476, 726.19047619],
        [7.75714286, -6.75714286, 775.71428571],
        [9.47142857, -8.47142857, 947.14285714],
        [9.85238095, -8.85238095, 985.23809524],
        [9.54761905, -8.54761905, 954.76190476],
        [8.63333333, -7.63333333, 863.33333333],
        [7.83333333, -6.83333333, 783.33333333],
        [6.76666667, -5.76666667, 676.66666667],
        [5.2047619, -4.2047619, 520.47619048],
        [2.95714286, -1.95714286, 295.71428571],
        [1.50952381, -0.50952381, 150.95238095],
        [0.48095238, 0.51904762, 48.0952381],
        [-0.01428571, 1.01428571, -1.42857143],
        [0.02380952, 0.97619048, 2.38095238],
        [0.17619048, 0.82380952, 17.61904762],
        [0.02380952, 0.97619048, 2.38095238],
        [0.06190476, 0.93809524, 6.19047619],
        [0.06190476, 0.93809524, 6.19047619],
        [0.06190476, 0.93809524, 6.19047619],
        [0.02380952, 0.97619048, 2.38095238],
        [0.06190476, 0.93809524, 6.19047619],
        [0.13809524, 0.86190476, 13.80952381],
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]

import kineticstoolkit.lab as ktk
plt.plot(forces)
plt.xlabel("# sample")
plt.ylabel("Force (N)")
plt.legend(["Fx", "Fy", "Fz"])
plt.show()
```

Write a code that calculates the mean of $F_x$, but only during the weight support phase. We consider that the weight support phase consists in any sample where $F_z > 10$.

Follow these steps:

1. Isolate the weight support phase using $F_z$;
2. Isolate $F_x$ during this phase;
3. Calculate the average of $F_x$.

```{code-cell} ipython3
:tags: [hide-cell]

# Step 1

# We create a mask to keep only the weight support phase
is_weight_support_phase = forces[:, 2] > 10

# Step 2

# We isolate Fx during this phase
f_x = forces[is_weight_support_phase, 0]

# Step 3

# We calculate the average
print(np.mean(f_x))
```

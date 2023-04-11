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

# Multidimensional arrays

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

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


# Slicing multidimensional arrays

We just learned how to index multidimensional matrices using indexes separated by commas. Slicing works the same way: for a given dimension, all we need is to use a slice instead of an index.

**Example 1: Read the marker's y coordinate at samples 0 and 1**

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

tbl = ktkdoctools.draw_table(position, title="position")

# Highlight the second line
for i in range(2):
    tbl[i, 1].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

plt.show()
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

position[0:2, 1]
```

**Example 2: Read the marker's y and z coordinates at samples 0 and 1**

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

**Example 3: Read the marker's z coordinate at all samples**

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

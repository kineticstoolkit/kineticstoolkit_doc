---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
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

In section [](numpy_filtering_1d.md), we learned how to use lists of booleans and lists of integers to filter one-dimensional arrays. This also works on multidimensional arrays, although filtering on axes other than the first is somewhat unintuitive and can result in unexpected array shapes. Fortunately, in biomechanical data processing, filtering often occurs on the first axis, which typically corresponds to time.

**Example: Read the marker coordinates at samples 0 and 2**

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
for i in range(4):
    tbl[0, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)
    tbl[2, i].set_facecolor(ktkdoctools.HIGHLIGHT_BLUE_0)

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

mask = [0, 2]
position[mask]
```

or directly:

```{code-cell} ipython3
position[[0, 2]]
```

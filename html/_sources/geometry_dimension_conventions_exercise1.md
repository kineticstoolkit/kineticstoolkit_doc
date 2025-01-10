---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Expressing a series of points

Using [Kinetics Toolkit's conventions](geometry_dimension_conventions.md), create a NumPy array that corresponds to the following trajectory:

$$
\vec{p}(t_0) = (3, 4, 5) \\
\vec{p}(t_1) = (4, 5, 5) \\
\vec{p}(t_2) = (5, 6, 5) \\
\vec{p}(t_3) = (6, 7, 5) \\
\vec{p}(t_4) = (7, 8, 5) \\
$$

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

# or

p = ktk.geometry.create_point_series(
    [[3, 4, 5], [4, 5, 5], [5, 6, 5], [6, 7, 5], [7, 8, 5]]
)

p
```

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

# Exercise: Expressing a constant vector

Using [Kinetics Toolkit's conventions](geometry_dimension_conventions.md), create a NumPy array that corresponds to the following time-invarying vector:

$$
\vec{v} = (1, 2, 0)
$$

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

v = np.array([[1.0, 2.0, 0.0, 0.0]])

# or

v = ktk.geometry.create_vector_series([[1, 2, 0]])

v
```

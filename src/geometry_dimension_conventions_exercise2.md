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

# Exercise: Expressing a constant vector

Using [Kinetics Toolkit's conventions](geometry_dimension_conventions.md), create a NumPy array that corresponds to the following time-invarying vector:

$$
\vec{v} = (1, 2, 0)
$$

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

v = np.array([[1.,2.,0.,0.]])

v
```

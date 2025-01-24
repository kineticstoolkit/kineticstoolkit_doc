---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Creating vector series

A series of N vectors (e.g., speeds, forces) is expressed as:

    [
        [x(t0), y(t0), z(t0), 0.0],
        [x(t1), y(t1), z(t1), 0.0],
        [x(t2), y(t2), z(t2), 0.0],
        [ ... ,  ... ,  ... , ...],
    ]

As with points, the function [ktk.geometry.create_vector_series](api/ktk.geometry.create_vector_series.rst) can create such series from different forms:

## Using multiple arrays

In this case, the arguments `x`, `y`, and `z` accept arrays of floats:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ktk.geometry.create_vector_series(
    x=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5], z=[5.0, 5.0, 5.0, 5.1, 5.1, 5.1]
)
```

## Using a single array

The default argument accepts an array of NxM where M could be 1 (x), 2 (x, y), 3 (x, y, z) or 4 (x, y, z, 0):

```{code-cell} ipython3
ktk.geometry.create_vector_series(
    [
        [0.0, 0.0, 5.0],
        [0.1, 0.0, 5.0],
        [0.2, 0.0, 5.0],
        [0.3, 0.0, 5.1],
        [0.4, 0.0, 5.1],
        [0.5, 0.0, 5.1],
    ]
)
```

## Series of constant values

Similar to point series, the function [ktk.geometry.create_vector_series](api/ktk.geometry.create_vector_series.rst) has a convenient argument `length` for series of constant values. For instance, if we need to repeat a constant vector over five samples:

```{code-cell} ipython3
ktk.geometry.create_vector_series([[1.0, 2.0, 3.0]], length=5)
```

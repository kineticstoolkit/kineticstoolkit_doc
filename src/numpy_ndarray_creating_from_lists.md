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

# Creating arrays from lists

## One dimension

A simple way to create an array from a list is to use the {{np_array}} function:

```{code-cell} ipython3
import numpy as np

array_1d = np.array([0.1, 0.2, 0.3])

array_1d
```

It is also possible to convert back an array to a list, using its {{ndarray_tolist}} method:

```{code-cell} ipython3
array_1d.tolist()
```

We get the size (shape) of an array using its {{ndarray_shape}} property:

```{code-cell} ipython3
array_1d.shape
```

This tuple has only 1 value, which denotes a unidimensional array. This value is **3**, which means the array has a length of **3**. In other words, this is a vector of length 3. For unidimensional arrays, both {{ndarray_shape}} and Python's `len` keyword have very similar meanings:

```{code-cell} ipython3
len(array_1d)
```

:::{note}
NumPy's documentation usually refer to **axis** to denote a **dimension**. Both terms refer to the same thing.
:::

## More dimensions

We can create a 2d array using nested lists:

```{code-cell} ipython3
array_2d = np.array(
    [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]
)

array_2d
```

Its shape is:

```{code-cell} ipython3
array_2d.shape
```

This tuple has 2 values, which denotes a bidimensional array. It has a length of **2** on its first axis, and of **3** on its second axis. In other words, this is a **2**x**3** matrix.

We can even create arrays with more axes:

```{code-cell} ipython3
array_3d = np.array(
    [
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
        ],
        [
            [0.7, 0.8, 0.9],
            [1.1, 1.2, 1.3],
        ],
    ]
)

array_3d
```

Its shape is:

```{code-cell} ipython3
array_3d.shape
```

This tuple has 3 values, which denotes a tridimensional array. It has a length of **2** on its first axis, of **2** on its second axis, and of **3** on its third axis. In other words, this is a series of **two** **2**x**3** matrices.
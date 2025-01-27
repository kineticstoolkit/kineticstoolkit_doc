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

A simple way to create an array from a list is to use the {{np_array}} function. To create the one-dimensional array of {numref}`fig_array_1d_float`, we would write:

```{figure-md} fig_array_1d_float
:width: 2in
![](_static/images/fig_array_1d_float.png)

A one-dimensional array.
```

```{code-cell} ipython3
import numpy as np

array_1d = np.array([0.0, 0.1, 0.2, 0.3])

array_1d
```

It is also possible to convert back an array to a list, using its {{ndarray_tolist}} method:

```{code-cell} ipython3
array_1d.tolist()
```

To create the two-dimensional array of {numref}`fig_array_2d_float`, we would use nested lists:

```{figure-md} fig_array_2d_float
:width: 3in

![](_static/images/fig_array_2d_float.png)

A two-dimensional array.
```

```{code-cell} ipython3
array_2d = np.array(
    [
        [0.0, 0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6, 0.7],
        [0.8, 0.9, 1.0, 1.1],
    ]
)

array_2d
```


To create the three-dimensional array of {numref}`fig_array_3d_float`, we would use multiple levels of nested lists:

```{figure-md} fig_array_3d_float
:width: 4in

![](_static/images/fig_array_3d_float.png)

A three-dimensional array.
```

```{code-cell} ipython3
array_3d = np.array(
    [
        [
            [0.0, 0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6, 0.7],
            [0.8, 0.9, 1.0, 1.1],
        ],
        [
            [1.2, 1.3, 1.4, 1.5],
            [1.6, 1.7, 1.8, 1.9],
            [2.0, 2.1, 2.2, 2.3],
        ],
        [
            [2.4, 2.5, 2.6, 2.7],
            [2.8, 2.9, 3.0, 3.1],
            [3.2, 3.3, 3.4, 3.5],
        ],
    ]
)

array_3d
```

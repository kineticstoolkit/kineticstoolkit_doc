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


# Statistical functions

NumPy provides common statistical functions such as:

- {{np_sum}}
- {{np_mean}}
- {{np_std}}
- {{np_min}}
- {{np_max}}
- {{np_median}}
- {{np_quantile}}


which all take an array as an argument. For multidimensional arrays, these functions accept an additional `axis` argument to select which axis (rows, columns, etc.) to perform the operation on. For example, for a matrix, an operation on the first axis is performed on the **rows**:

```{code-cell} ipython3
import numpy as np

a = np.array(
    [
        [0.0, 0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6, 0.7],
        [0.8, 0.9, 1.0, 1.2],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

An operation on the second axis is performed on the **columns**:

```{code-cell} ipython3
print(f"Sum on second axis = {np.sum(a, axis=1)}")
print(f"Max on second axis = {np.max(a, axis=1)}")
```

If the array contains `nan` values, using these functions can be problematic because any arithmetic operation that includes `nan` results in `nan`:

```{code-cell} ipython3
a = np.array(
    [
        [0.0, 0.1, 0.2, 0.3],
        [0.4, 0.5, np.nan, 0.7],
        [0.8, 0.9, 1.0, 1.2],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

In these cases, NumPy provides alternate functions:
- {{np_nansum}}
- {{np_nanmean}}
- {{np_nanstd}}
- {{np_nanmin}}
- {{np_nanmax}}
- {{np_nanmedian}}
- {{np_nanquantile}}

that ignore `nan` values during the calculation.

```{code-cell} ipython3
print(f"Sum on first axis = {np.nansum(a, axis=0)}")
print(f"Max on first axis = {np.nanmax(a, axis=0)}")
```

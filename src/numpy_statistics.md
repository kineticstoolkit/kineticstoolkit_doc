# Statistical functions

NumPy also provides statistical functions such as {{np_sum}}, {{np_mean}}, {{np_std}}, {{np_min}}, {{np_max}}, {{np_median}}, and {{np_quantile}}. For multidimensional arrays, these functions accept an `axis` parameter that indicates which axis to perform the operation on. For example, for a matrix, an operation on the first axis is performed on the **lines**:

```{code-cell} ipython3
import numpy as np


a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

Whereas an operation on the second axis is performed on the **columns**:

```{code-cell} ipython3
print(f"Sum on second axis = {np.sum(a, axis=1)}")
print(f"Max on second axis = {np.max(a, axis=1)}")
```

If the array contains `nan` values, using these functions can be problematic because any arithmetic operation that includes `nan` results in `nan`:

```{code-cell} ipython3
a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, np.nan, 6.0],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

For these cases, NumPy provides alternate functions: {{np_nansum}}, {{np_nanmean}}, {{np_nanstd}}, {{np_nanmin}}, {{np_nanmax}}, {{np_nanmedian}}, {{np_nanquantile}} that ignore `nan` values from the calculation.

```{code-cell} ipython3
print(f"Sum on first axis = {np.nansum(a, axis=0)}")
print(f"Max on first axis = {np.nanmax(a, axis=0)}")
```

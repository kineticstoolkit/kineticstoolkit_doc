---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Converting and copying TimeSeries

We now know how to create a TimeSeries from scratch. We can also create a TimeSeries from other variables or even from other TimeSeries.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np
import pandas as pd
```

## Converting a variable to a TimeSeries

Any [list](python_lists.md), [NumPy array](numpy_ndarray.md), Pandas {{pd_series}} or Pandas {{pd_dataframe}} can be converted to a TimeSeries.

+++

### List to TimeSeries

```{code-cell} ipython3
example_list = [1, 2, 3, 4, 5]

example_list
```

```{code-cell} ipython3
ts = ktk.TimeSeries(example_list)

ts
```

### Array to TimeSeries

```{code-cell} ipython3
example_array = np.array([1, 2, 3, 4, 5])

example_array
```

```{code-cell} ipython3
ts = ktk.TimeSeries(example_array)

ts
```

### Series to TimeSeries

```{code-cell} ipython3
example_series = pd.Series([1, 2, 3, 4, 5])

example_series
```

```{code-cell} ipython3
ts = ktk.TimeSeries(example_series)

ts
```

### DataFrame to TimeSeries

```{code-cell} ipython3
example_dataframe = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["x", "y"])

example_dataframe
```

```{code-cell} ipython3
ts = ktk.TimeSeries(example_dataframe)

ts
```

## Copying a TimeSeries

As for most types in Python, a TimeSeries is a mutable type, which means that simply writing `ts2 = ts1` does not create a second TimeSeries `ts2` based on TimeSeries `ts1`. Instead, it creates a new variable that addresses the same TimeSeries. As a consequence, modifying `ts2` would also modify `ts1`. To create an independent copy of `ts1`, we use `ts2 = ts1.copy()`.

:::{note}
This same phenomenon also happens with most Python types, including NumPy arrays and Pandas DataFrames. This is why they also include a `copy` method.
:::

The [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method has different arguments to select which attributes to copy. For instance, if we want to create TimeSeries with the same time and events as another one, but without its data or info, we would use:

```
ts2 = ts1.copy(copy_data=False, copy_info=False)
```

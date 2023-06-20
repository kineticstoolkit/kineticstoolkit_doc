# Copying a TimeSeries

This section introduces the [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method.

As for most types in Python, a TimeSeries is a mutable type, which means that simply writing `ts2 = ts1` does not create a second TimeSeries `ts2` based on TimeSeries `ts1`. Instead, it creates a new variable that addresses the same TimeSeries. As a consequence, modifying `ts2` would also modify `ts1`. To create an independent copy of `ts1`, we use `ts2 = ts1.copy()`.

:::{note}
This same phenomenon also happens with most Python types, including NumPy arrays and Pandas DataFrames. This is why they also include a `copy` method.
:::

The [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method has different arguments to select which attributes to copy. For instance, if we want to create TimeSeries with the same time and events as another one, but without its data, we would use:

```
ts2 = ts1.copy(copy_data=False, copy_data_info=False)
```

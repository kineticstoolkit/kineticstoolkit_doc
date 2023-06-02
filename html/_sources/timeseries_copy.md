---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```


# Copying a TimeSeries

This section introduces the [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method.

As for most types in Python, a TimeSeries is a mutable type, which means that simply writing `ts2 = ts1` does not create a second TimeSeries `ts2` based on TimeSeries `ts1`. Instead, it creates a new variable that addresses the same TimeSeries. Here is the consequence:

```{code-cell}
import kineticstoolkit.lab as ktk
import numpy as np
import matplotlib.pyplot as plt

# Create ts1
ts1 = ktk.TimeSeries(time = np.arange(10) / 2)
ts1.data['Example'] = ts1.time ** 2

# Create ts2
ts2 = ts1
```

As expected, we have two identical TimeSeries:

```{code-cell}
:tags: [remove-input]

# Plot ts1 and ts2
plt.subplot(1, 2, 1)
ts1.plot()
plt.title("ts1")
plt.subplot(1, 2, 2)
ts2.plot()
plt.title("ts2")
plt.tight_layout()
```

However, modifying `ts2` also modifies `ts1` since both variables refer to the same TimeSeries:

```{code-cell}
ts2.data['Example'][3:5] = np.nan
```

```{code-cell}
:tags: [remove-input]

# Plot ts1 and ts2
plt.subplot(1, 2, 1)
ts1.plot()
plt.title("ts1")
plt.subplot(1, 2, 2)
ts2.plot()
plt.title("ts2")
plt.tight_layout()
```

To create an **independent copy** of a TimeSeries, we use the [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method:

```{code-cell} ipython3
# Create ts1
ts1 = ktk.TimeSeries(time = np.arange(10) / 2)
ts1.data['Example'] = ts1.time ** 2

# Create ts2 using copy
ts2 = ts1.copy()
```

Now, modifying one TimeSeries does not modify the other:

```{code-cell}
# Modify ts2; this should not modify ts1
ts2.data['Example'][3:5] = np.nan
```

```{code-cell}
:tags: [remove-input]

# Plot ts1 and ts2
plt.subplot(1, 2, 1)
ts1.plot()
plt.title("ts1")
plt.subplot(1, 2, 2)
ts2.plot()
plt.title("ts2")
plt.tight_layout()
```


:::{important}
This same phenomenon also happens with most Python types, including NumPy arrays and Pandas DataFrames. This is why they also include a `copy` method.
:::

The [ktk.TimeSeries.copy](api/ktk.TimeSeries.copy.rst) method has different arguments to select which attributes to copy. For instance, if we want to create TimeSeries with the same time and events as another one, but without its data, we could use:

```{code-cell} ipython3
ts2 = ts1.copy(copy_data=False, copy_data_info=False)

ts2
```

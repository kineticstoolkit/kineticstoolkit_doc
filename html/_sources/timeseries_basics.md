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

# The TimeSeries type

The [ktk.TimeSeries](api/ktk.TimeSeries.rst) type is largely inspired by Matlab's `timeseries` and `tscollection`. Every TimeSeries contains time, data, events, and metadata.

## Time and data

A TimeSeries in its simplest form contains a time attribute and at least one data series. For example:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = ktk.TimeSeries()                     # Create an empty TimeSeries
ts.time = np.arange(0, 10, 0.1)           # Assign time
ts.data["Sinus"] = np.sin(ts.time)        # Add a data series
ts.data["Cosinus"] = np.cos(ts.time)      # Add another data series
ts.data["SquareRoot"] = np.sqrt(ts.time)  # Add yet another data series

ts
```

We can also add data to a TimeSeries using its [add_data](api/ktk.TimeSeries.add_data.rst) method. This method checks that each data series has the same number of samples, whereas assigning it directly to `data` (as above) does not perform such verification.

```{code-cell} ipython3
ts = ktk.TimeSeries()                             # Create an empty TimeSeries
ts.time = np.arange(0, 10, 0.1)                   # Assign time
ts = ts.add_data("Sinus", np.sin(ts.time))        # Add a data series
ts = ts.add_data("Cosinus", np.cos(ts.time))      # Add another data series
ts = ts.add_data("SquareRoot", np.sqrt(ts.time))  # Add yet another data series

ts
```

To see the TimeSeries data:

```{code-cell} ipython3
ts.data
```

TimeSeries can be [plotted](api/ktk.TimeSeries.plot.rst) directly using Matplotlib, and we can also specify which of the series to plot.

```{code-cell} ipython3
plt.subplot(1, 3, 1)
ts.plot()

plt.subplot(1, 3, 2)
ts.plot("Cosinus")

plt.subplot(1, 3, 3)
ts.plot(["Sinus", "Cosinus"])

plt.tight_layout()
```

A TimeSeries can also contain multidimensional data, as long as the first dimension corresponds to time. For instance, this [dataset of wheelchair propulsion kinetics](dataset_kinetics_wheelchair_propulsion.md) expresses forces and moments as Nx4 series of vectors:

$$
\text{Forces} = \begin{bmatrix}
F_x(0) & F_y(0) & F_z(0) & 0 \\
F_x(1) & F_y(1) & F_z(1) & 0 \\
F_x(2) & F_y(2) & F_z(2) & 0 \\
... & ... & ... & ... \\
F_x(N-1) & F_y(N-1) & F_z(N-1) & 0
\end{bmatrix}
$$

$$
\text{Moments} = \begin{bmatrix}
M_x(0) & M_y(0) & M_z(0) & 0 \\
M_x(1) & M_y(1) & M_z(1) & 0 \\
M_x(2) & M_y(2) & M_z(2) & 0 \\
... & ... & ... & ... \\
M_x(N-1) & M_y(N-1) & M_z(N-1) & 0
\end{bmatrix}
$$

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip"))

ts.data
```

```{code-cell} ipython3
ts.plot()
```

## Events

In the figure above, we see that the TimeSeries contains cyclic data. These cycles could be delimited using events. There are several ways to edit the events of a TimeSeries, which will be presented later in section [](timeseries_event_management.md). For now, we will add the events manually using [ktk.TimeSeries.add_event](api/ktk.TimeSeries.add_event.rst):

```{code-cell} ipython3
ts = ts.add_event(8.56, "push")
ts = ts.add_event(9.93, "recovery")
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")
ts = ts.add_event(11.78, "push")
ts = ts.add_event(12.33, "recovery")
ts = ts.add_event(13.39, "push")
ts = ts.add_event(13.88, "recovery")
ts = ts.add_event(14.86, "push")
ts = ts.add_event(15.30, "recovery")
```

These 10 events are now added to the TimeSeries' list of events:

```{code-cell} ipython3
ts.events
```

If we plot the TimeSeries again, we can see the added events.

```{code-cell} ipython3
ts.plot()
```

## Metadata

The TimeSeries' `time_info` and `data_info` attributes are dictionaries that associate information to time and data. By default, `time_info` includes the "Unit" key, which corresponds to "s". Any other time information can be added by adding new keys to `time_info`.

```{code-cell} ipython3
ts.time_info
```

Similarly, the `data_info` attribute is a dictionary that associates information to data. You may use the [ktk.TimeSeries.add_data_info](api/ktk.TimeSeries.add_data_info.rst) and [ktk.TimeSeries.remove_data_info](api/ktk.TimeSeries.remove_data_info.rst) methods to ease the management of `data_info`:

```{code-cell} ipython3
ts = ts.add_data_info("Forces", "Unit", "N")
ts = ts.add_data_info("Moments", "Unit", "Nm")

ts.data_info
```

Unless explicitly mentioned, metadata is not used for calculation and is strictly optional. Some functions, however, read metadata: for example, the [ktk.TimeSeries.plot](api/ktk.TimeSeries.plot.rst) method looks for possible "Unit" metadata and prints it on the y-axis; and the [ktk.Player](api/ktk.Player.rst) class looks for possible "Colour" metadata to set the colour of 3D points.

```{code-cell} ipython3
ts.plot()
```

## Converting variables to TimeSeries

We can convert a [list](python_lists.md), a [NumPy array](numpy_ndarray.md), a Pandas {{pd_series}} or a Pandas {{pd_dataframe}} to a TimeSeries, using this form:

```{code-cell} ipython3
example_list = [1, 2, 3, 4, 5]
example_array = np.array([1, 2, 3, 4, 5])
example_series = pd.Series([1, 2, 3, 4, 5])
example_dataframe = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["x", "y"])
```

### List to TimeSeries

```{code-cell} ipython3
ktk.TimeSeries(example_list)
```

### Array to TimeSeries

```{code-cell} ipython3
ktk.TimeSeries(example_array)
```

### Series to TimeSeries

```{code-cell} ipython3
ktk.TimeSeries(example_series)
```

### DataFrame to TimeSeries

```{code-cell} ipython3
ktk.TimeSeries(example_dataframe)
```

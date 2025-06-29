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

# The TimeSeries type

A TimeSeries is a single container that hold time, data, events and general info.

## Time and data

A TimeSeries in its simplest form contains a time attribute and some data. For example:

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

## Info

The TimeSeries' `info` attribute contains metadata such as units and other information. This dictionary is addressed using two nested keys: the first (outer) one is generally what the information refers to (e.g., "Time", "Forces", "LateralFemoralEpicondyleR", "Speed"), and the second (inner) one defines the nature of the information (e.g., "Unit", "Date", "Name").

By default, `info` includes the time unit:

```{code-cell} ipython3
ts.info
```

You may use the [ktk.TimeSeries.add_info](api/ktk.TimeSeries.add_info.rst), [ktk.TimeSeries.rename_info](api/ktk.TimeSeries.rename_info.rst) and [ktk.TimeSeries.remove_info](api/ktk.TimeSeries.remove_info.rst) to manage `info`:

```{code-cell} ipython3
ts = ts.add_info("Forces", "Unit", "N")
ts = ts.add_info("Moments", "Unit", "Nm")

ts.info
```

Unless explicitly mentioned, metadata is not used for calculation and is strictly optional. "Unit" info is however used by [ktk.TimeSeries.plot](api/ktk.TimeSeries.plot.rst) to plot the units:

```{code-cell} ipython3
ts.plot()
```


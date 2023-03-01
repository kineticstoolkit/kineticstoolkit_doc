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

# 📖 TimeSeries basics

:::{card} Summary
This section presents the `TimeSeries` data container and its attributes.
:::

TimeSeries are largely inspired by Matlab's `timeseries` and `tscollection`. Every TimeSeries contains the following attributes:

- `time`: A numpy array that contains the time vector.
- `data`: A dict where each entry is a numpy array, with the first dimension corresponding to time.
- `events`: An optional list of events.
- `time_info`: Metadata corresponding to time, that contains at least the time unit.
- `data_info`: Optional metadata.

## 📄 Time and Data

A TimeSeries in its simplest form contains a time vector and at least one data series. For example:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

ts = ktk.TimeSeries()
ts.time = np.arange(0, 10, 0.1)  # 10 seconds at 10 Hz
ts.data["Sinus"] = np.sin(ts.time)

ts
```

```{code-cell} ipython3
ts.data
```

TimeSeries can be [plotted](api/ktk.TimeSeries.plot.rst) directly using Matplotlib:

```{code-cell} ipython3
ts.plot()
```

A TimeSeries can contain many independent data that share a same time vector:

```{code-cell} ipython3
ts.data["Cosinus"] = np.cos(ts.time)

ts.data
```

```{code-cell} ipython3
ts.plot()
```

A TimeSeries can also contain multidimensional data, as long as the first dimension corresponds to time.

For the rest of this section, we will load a TimeSeries that contains forces and moments during manual wheelchair propulsion. These forces and moments are expressed as Nx4 series of vectors:

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
ts = ktk.load(ktk.doc.download("timeseries_example.ktk.zip"))

ts
```

:::{tip}
You can download and read any data shown in any tutorial on this website. Be sure to be connected to the internet, then [ktk.doc.download](api/ktk.doc.download.rst) will download the file for you.
:::

```{code-cell} ipython3
ts.data
```

```{code-cell} ipython3
ts.plot()
```

## 📄 Metadata

The `time_info` property associates metadata to the time vector. It is a dictionary where each key is the name of one metadata. By default, `time_info` includes the "Unit" metadata, which corresponds to "s". Any other metadata can be added by adding new keys in `time_info`.

```{code-cell} ipython3
ts.time_info
```

Similarly, the `data_info` property associates metadata to data. This property is a dictionary of dictionaries, where the outer key corresponds to the data key, and the inner key is the metadata. Use the [](api/ktk.TimeSeries.add_data_info.rst) method to ease the management of `data_info`:

```{code-cell} ipython3
ts = ts.add_data_info("Forces", "Unit", "N")
ts = ts.add_data_info("Moments", "Unit", "Nm")

ts.data_info
```

```{code-cell} ipython3
ts.data_info["Forces"]
```

Unless explicitly mentioned, metadata is not used for calculation and is optional. It is simply a way to clarify the data by adding information to it. Some functions however read metadata: for example, the [](api/ktk.TimeSeries.plot.rst) method looks for possible "Unit" metadata and prints it on the y axis; the [ktk.Player](api/ktk.Player.rst) class looks for possible "Color" metadata to set the colour of 3D points.

```{code-cell} ipython3
ts.plot()
```

## 📄 Events

In the figure above, we see that the TimeSeries contains cyclic data that could be characterized by events. We will add these events to the TimeSeries.

There are several ways to edit the events of a TimeSeries:
- Editing events manually, using the [](api/ktk.TimeSeries.add_event.rst) and [](api/ktk.TimeSeries.remove_event.rst) methods;
- Editing events interactively, using the [](api/ktk.TimeSeries.ui_edit_events.rst) method;
- Adding events automatically, for example using the [](api/ktk.cycles.rst) module that can detect cycles automatically.

In this tutorial, we will add the events manually.

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

These 11 events are now added to the TimeSeries' list of events:

```{code-cell} ipython3
ts
```

```{code-cell} ipython3
ts.events
```

If we plot again the TimeSeries, we can see the added events.

```{code-cell} ipython3
ts.plot()
```

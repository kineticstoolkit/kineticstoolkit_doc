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

# Exercise: Creating a TimeSeries

The position of an object has been recorded in metres during one second at a sampling frequency of 100 Hz:

```{code-cell} ipython3
import numpy as np

p = np.array(
    [
        0.    , 0.0099, 0.0196, 0.0291, 0.0384, 0.0475, 0.0564, 0.0651,
        0.0736, 0.0819, 0.09  , 0.0979, 0.1056, 0.1131, 0.1204, 0.1275,
        0.1344, 0.1411, 0.1476, 0.1539, 0.16  , 0.1659, 0.1716, 0.1771,
        0.1824, 0.1875, 0.1924, 0.1971, 0.2016, 0.2059, 0.21  , 0.2139,
        0.2176, 0.2211, 0.2244, 0.2275, 0.2304, 0.2331, 0.2356, 0.2379,
        0.24  , 0.2419, 0.2436, 0.2451, 0.2464, 0.2475, 0.2484, 0.2491,
        0.2496, 0.2499, 0.25  , 0.2499, 0.2496, 0.2491, 0.2484, 0.2475,
        0.2464, 0.2451, 0.2436, 0.2419, 0.24  , 0.2379, 0.2356, 0.2331,
        0.2304, 0.2275, 0.2244, 0.2211, 0.2176, 0.2139, 0.21  , 0.2059,
        0.2016, 0.1971, 0.1924, 0.1875, 0.1824, 0.1771, 0.1716, 0.1659,
        0.16  , 0.1539, 0.1476, 0.1411, 0.1344, 0.1275, 0.1204, 0.1131,
        0.1056, 0.0979, 0.09  , 0.0819, 0.0736, 0.0651, 0.0564, 0.0475,
        0.0384, 0.0291, 0.0196, 0.0099
    ]
)
```

Create a TimeSeries that contains this data and its corresponding time, so that

```
ts.plot()
```

gives this:

```{code-cell} ipython3
:tags: [remove-input]

import kineticstoolkit.lab as ktk

# Create the TimeSeries
ts = ktk.TimeSeries()

# Assign the time
ts.time = np.arange(100)/100

# Assign the position
ts = ts.add_data("Position", p)

# Add the position unit
ts = ts.add_info("Position", "Unit", "m")

ts.plot()
```

```{code-cell} ipython3
:tags: [hide-cell]

import kineticstoolkit.lab as ktk

# Create the TimeSeries
ts = ktk.TimeSeries()

# Assign the time
ts.time = np.arange(100)/100

# Assign the position
ts = ts.add_data("Position", p)

# Add the position unit
ts = ts.add_info("Position", "Unit", "m")

ts.plot()
```

---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# 📖 Converting between TimeSeries and pandas DataFrames

:::{card} Summary
This section shows how to import a pandas DataFrame as a TimeSeries, and how to export a TimeSeries as a pandas DataFrame.
:::

To ensure a great compatibility between Kinetics Toolkit and other frameworks, TimeSeries can be converted from and to pandas DataFrames using the [](api/ktk.TimeSeries.from_dataframe.rst) and [](api/ktk.TimeSeries.to_dataframe.rst) methods, and thus benefit from the myriad of options offered by pandas. This section showcases these functions using examples.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import pandas as pd
```

## ⚙️ Example 1: Importing a csv file

In this example, we want to import the contents of this csv file:

```
    Time,Force,Position
    0,0,0
    0.1,0,0.01
    0.2,0,0.02
    0.3,0,0.03
    0.4,0.3,0.04
    0.5,0.5,0.05
    0.6,0.6,0.06
    0.7,0.5,0.07
    0.8,0.3,0.08
    0.9,0,0.09
    1,0,0.1
```

First, we will read it as a pandas DataFrame using `pd.read_csv()`:

```{code-cell} ipython3
df = pd.read_csv(
    ktk.doc.download("timeseries_dataframe_example1.csv"),
    index_col="Time",
)

df
```

Note the `index_col` parameter: the DataFrame index must correspond to time in seconds.

Then, we import it as a TimeSeries:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts
```

```{code-cell} ipython3
ts.data
```

## ⚙️ Example 2: Importing multidimensional data

TimeSeries are well suited for multidimensional data. In the last example, the force sensor was unidimensional; however, for a tridimensional force sensor, we would expect three signals (x, y, z). In this second example, we will import the following csv file:

```
    Time,Fx,Fy,Fz,Position
    0,0,-9.81,0,0
    0.1,0,-9.81,0,0.01
    0.2,0,-9.81,0,0.02
    0.3,0,-9.81,0,0.03
    0.4,0.3,-9.81,1.5,0.04
    0.5,0.5,-9.81,2.5,0.05
    0.6,0.6,-9.81,3,0.06
    0.7,0.5,-9.81,2.5,0.07
    0.8,0.3,-9.81,1.5,0.08
    0.9,0,-9.81,0,0.09
    1,0,-9.81,0,0.1
```

As for example 1, we first read the csv file as a DataFrame:

```{code-cell} ipython3
df = pd.read_csv(
        ktk.doc.download("timeseries_dataframe_example2.csv"),
        index_col="Time",
    )

df
```

Then we import this DataFrame as a TimeSeries:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts.data
```

The csv file was correctly read as a TimeSeries. However, force components are scattered into three separate arrays. Would it be possible to read it as one Nx3 array instead?

To this effect, simply rename the columns of the DataFrame, either in the original csv file or after reading it, using index brackets:

```{code-cell} ipython3
df.columns = ["Forces[0]", "Forces[1]", "Forces[2]", "Position"]

df
```

Finally, we can import this new DataFrame as a TimeSeries, with the three forces signals combined in one Nx3 array:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts.data
```

```{code-cell} ipython3
ts.data["Forces"]
```

For series of arrays with more than one dimension, the brackets would have multiple indexes. For example, a series of Nx4x4 homogeneous matrices would require 16 columns and the indexes would go from [0,0] to [3,3].

## ⚙️ Example 3: Converting a c3d file to csv

In this example, we will read 3d marker positions from a sample `c3d` file, and then export these positions to a `csv` file. We first read the `c3d` file using the [](api/ktk.kinematics.rst) module, which results in a TimeSeries with 26 markers:

```{code-cell} ipython3
markers = ktk.read_c3d(
    ktk.doc.download("kinematics_basket_sprint.c3d")
)["Points"]

markers
```

```{code-cell} ipython3
markers.data
```

To convert this TimeSeries to a `csv`, we first create a DataFrame:

```{code-cell} ipython3
df = markers.to_dataframe()

df
```

Then we export this DataFrame to a `csv` file. Let's print the first 3 lines of this file:

```{code-cell} ipython3
df.to_csv("output.csv", index_label="Time")

!head -3 output.csv
```

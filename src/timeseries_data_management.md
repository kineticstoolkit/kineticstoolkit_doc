---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Data management

This section shows how to use these methods for data management:

- [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst)
- [ktk.TimeSeries.rename_data](api/ktk.TimeSeries.rename_data.rst)
- [ktk.TimeSeries.remove_data](api/ktk.TimeSeries.remove_data.rst)
- [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst)
- [ktk.TimeSeries.merge](api/ktk.TimeSeries.merge.rst)

We will use this sample [kinematic acquisition](dataset_kinematics_tennis_serve.md) of 39 bilateral markers with 1092 samples recorded at 50 Hz during tennis serve:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

markers = ktk.read_c3d(ktk.doc.download("kinematics_tennis_serve.c3d"))[
    "Points"
]
```

## Removing data

The TimeSeries loaded above has many markers, which makes lots of data to visualize and process:

```{code-cell} ipython3
markers.plot(legend=False)
```

We can remove superfluous data from this TimeSeries using two methods:

**1. Subsetting a TimeSeries**

We can use [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst) to select which data to **keep** from a TimeSeries. For instance, to process only the markers of the thorax:

```{code-cell} ipython3
markers_thorax = markers.get_subset(
    [
        "Derrick:C7",
        "Derrick:T10",
        "Derrick:STRN",
        "Derrick:CLAV",
    ],
)

markers_thorax.plot()
```

**2. Removing data one at a time**

We can also use [ktk.TimeSeries.remove_data](api/ktk.TimeSeries.remove_data.rst), to select which data to **remove** from a TimeSeries:

```{code-cell} ipython3
markers_thorax = markers_thorax.remove_data("Derrick:C7")
markers_thorax = markers_thorax.remove_data("Derrick:T10")

markers_thorax.plot()
```

## Adding data

There are three ways to add new data to a TimeSeries. In the last step, we removed the marker "Derrick:C7" from `markers_thorax`. To put it back, we could use any of these methods:

**1. Setting the data attribute directly**

```{code-cell} ipython3
data_to_add = markers.data["Derrick:C7"]

markers_thorax.data["Derrick:C7"] = data_to_add
```

This method does not perform any check.

**2. Using `add_data`**

Usually, we would rather use the [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst) method, which performs two additional tests:

1. It ensures that we don't inadvertently overwrite data that was already present in the TimeSeries, using an optional `overwrite` paramater.
2. It ensures that the shape of the data is coherent with other data already in the TimeSeries. This way, combining data with different lengths or sampling rates would likely produce an error, which is a good thing to prevent further mistakes in data analysis.

```{code-cell} ipython3
markers_thorax = markers_thorax.add_data("Derrick:C7", data_to_add, overwrite=True)
```

```{tip}
[ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst) matches 1-sample inputs to the contents of the TimeSeries. For example, adding the 1-sample series `[3]` to a TimeSeries of 10 samples effectively adds a series of 10 samples: `[3, 3, 3, 3, 3, 3, 3, 3, 3, 3]`
```

+++

**3. Using `merge`**

In this third method, we first subset the source TimeSeries to keep only the markers to add in the destination TimeSeries. Then, we merge both TimeSeries.

```{code-cell} ipython3
ts_subset = markers.get_subset("Derrick:C7")

markers_thorax = markers_thorax.merge(ts_subset, overwrite=True)
```

This method performs three tests:

1. Same as [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst): it ensures that we don't inadvertently overwrite data.
2. Same as [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst): it ensures that the shape of the data is coherent with other data already in the TimeSeries.
3. It ensures that both TimeSeries have the same time attribute. This is the safest method to ensure that all data have both the same length and same sample rate.

## Renaming data

Finally, [ktk.TimeSeries.rename_data](api/ktk.TimeSeries.rename_data.rst) renames data and its associated metadata (in data_info):

```{code-cell} ipython3
markers_thorax = markers_thorax.rename_data('Derrick:STRN', "Sternum")
markers_thorax = markers_thorax.rename_data('Derrick:CLAV', "Interclavicular")
markers_thorax = markers_thorax.rename_data('Derrick:C7', "C7")

markers_thorax.data
```

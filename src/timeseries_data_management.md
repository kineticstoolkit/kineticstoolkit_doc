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

# Data management

This section shows how to use these methods for data management:

- [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst)
- [ktk.TimeSeries.merge](api/ktk.TimeSeries.merge.rst)
- [ktk.TimeSeries.rename_data](api/ktk.TimeSeries.rename_data.rst)
- [ktk.TimeSeries.remove_data](api/ktk.TimeSeries.remove_data.rst)

We will use this sample [kinematic acquisition](dataset_kinematics_tennis_serve.md) of 39 bilateral markers with 1092 samples recorded at 50 Hz during tennis serve:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

markers = ktk.read_c3d(ktk.doc.download("kinematics_tennis_serve.c3d"))[
    "Points"
]
```

## Removing data

This TimeSeries has many markers, which makes lots of data to visualize and process:

```{code-cell} ipython3
markers.plot(legend=False)
```

If not all data is required for analysis, we can subset the TimeSeries into a new, smaller TimeSeries, using [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst). For instance, to process only the markers of the thorax:

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

We could also remove data one by one from a TimeSeries using [ktk.TimeSeries.remove_data](api/ktk.TimeSeries.remove_data.rst):

```{code-cell} ipython3
markers_thorax = markers_thorax.remove_data("Derrick:C7")
markers_thorax = markers_thorax.remove_data("Derrick:T10")

markers_thorax.plot()
```

## Adding data

We can assign new data directly to the TimeSeries' data attribute:

```{code-cell} ipython3
markers_thorax.data["Derrick:C7"] = markers.data["Derrick:C7"]

markers_thorax.data
```

However, when possible, a better way is to:
- Subset the original TimeSeries using [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst);
- Merge this subset with the new TimeSeries using [ktk.TimeSeries.merge](api/ktk.TimeSeries.merge.rst) method:

```{code-cell} ipython3
markers_thorax = markers_thorax.merge(markers.get_subset("Derrick:T10"))

markers_thorax.data
```

:::{good-practice} Merging TimeSeries
Using the second method is more robust because it checks that both TimeSeries' time match together before merging. For example, trying to merge two TimeSeries that do not have the same length or sampling rate would generate an error (which is good) using method 2, whereas it would be undetected (which is bad) by method 1.
:::

## Renaming data

Finally, [ktk.TimeSeries.rename_data](api/ktk.TimeSeries.rename_data.rst) renames data and its associated metadata (in data_info):

```{code-cell} ipython3
markers_thorax = markers_thorax.rename_data('Derrick:STRN', "Sternum")
markers_thorax = markers_thorax.rename_data('Derrick:CLAV', "Interclavicular")
markers_thorax = markers_thorax.rename_data('Derrick:C7', "C7")
markers_thorax = markers_thorax.rename_data('Derrick:T10', "T10")

markers_thorax.data
```

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
import matplotlib.pyplot as plt

markers = ktk.read_c3d(ktk.doc.download("kinematics_tennis_serve.c3d"))[
    "Points"
]
```

## Adding data

The TimeSeries loaded above has many markers, which makes lots of data to visualize and process:

```{code-cell} ipython3
markers.plot()
```

+++ {"jp-MarkdownHeadingCollapsed": true}

To keep only the data we need, it is often practical to make a [copy](api/ktk.TimeSeries.copy.rst) of the TimeSeries with no data, and selectively add the data we need using [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst):

```{code-cell} ipython3
# Copy the TimeSeries without its data
selected_markers = markers.copy(copy_data=False)

# Add the markers to this new TimeSeries
for key in ["Derrick:C7", "Derrick:T10", "Derrick:STRN", "Derrick:CLAV"]:
    selected_markers = selected_markers.add_data(key, markers.data[key])

selected_markers.plot()
```

## Removing data

We could do the same by removing the superfluous data from the TimeSeries, using [ktk.TimeSeries.remove_data](api/ktk.TimeSeries.remove_data.rst):

```{code-cell} ipython3
# Copy the whole TimeSeries, with all data
selected_markers = markers.copy()

# Delete the unwanted markers from this new TimeSeries
for key in markers.data:
    if key not in ["Derrick:C7", "Derrick:T10", "Derrick:STRN", "Derrick:CLAV"]:
        selected_markers = selected_markers.remove_data(key)

selected_markers.plot()
```

## Subsetting

As a shortcut method, we can also use [ktk.TimeSeries.get_subset](api/ktk.TimeSeries.get_subset.rst), which returns a TimeSeries with only a selection of data keys:

```{code-cell} ipython3
selected_markers = markers.get_subset(
    [
        "Derrick:C7",
        "Derrick:T10",
        "Derrick:STRN",
        "Derrick:CLAV",
    ],
)

selected_markers.plot()
```

## Renaming data

Use the [ktk.TimeSeries.rename_data](api/ktk.TimeSeries.rename_data.rst) to change the name of a data key:

```{code-cell} ipython3
selected_markers = selected_markers.rename_data("Derrick:C7", "C7")
selected_markers = selected_markers.rename_data("Derrick:T10", "T10")
selected_markers = selected_markers.rename_data("Derrick:STRN", "Sternum")
selected_markers = selected_markers.rename_data("Derrick:CLAV", "Clavicular")

selected_markers.plot()
```

## Merging data

Let say we have two different TimeSeries, one for the left lower limb and one for the right one:

```{code-cell} ipython3
left_lower_limb = markers.get_subset(
    [
        "Derrick:LANK",
        "Derrick:LHEE",
        "Derrick:LKNE",
        "Derrick:LTOE",
    ]
)

right_lower_limb = markers.get_subset(
    [
        "Derrick:RANK",
        "Derrick:RHEE",
        "Derrick:RKNE",
        "Derrick:RTOE",
    ]
)

plt.subplot(1,2,1)
left_lower_limb.plot(legend=False)
plt.subplot(1,2,2)
right_lower_limb.plot(legend=False)
```

To merge these TimeSeries, we could simply use the [ktk.TimeSeries.add_data](api/ktk.TimeSeries.add_data.rst) method as we did above:

```{code-cell} ipython3
merged = left_lower_limb.copy()

for key in right_lower_limb.data:
    merged = merged.add_data(key, right_lower_limb.data[key])

merged.plot(legend=False)
```

As a shortcut method, we can also use [ktk.TimeSeries.merge](api/ktk.TimeSeries.merge.rst):

```{code-cell} ipython3
merged = left_lower_limb.merge(right_lower_limb)

merged.plot(legend=False)
```

Using [ktk.TimeSeries.merge](api/ktk.TimeSeries.merge.rst) has several other benefits, such as merging events, information, and even resample TimeSeries that may have been recorded at different sampling rates.

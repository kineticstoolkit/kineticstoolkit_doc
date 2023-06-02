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

# Segmenting TimeSeries

This section shows how to use these methods to segment TimeSeries:

- [ktk.TimeSeries.get_ts_before_index](api/ktk.TimeSeries.get_ts_before_index.rst)
- [ktk.TimeSeries.get_ts_after_index](api/ktk.TimeSeries.get_ts_after_index.rst)
- [ktk.TimeSeries.get_ts_between_indexes](api/ktk.TimeSeries.get_ts_between_indexes.rst)
- [ktk.TimeSeries.get_ts_at_time](api/ktk.TimeSeries.get_ts_at_time.rst)
- [ktk.TimeSeries.get_ts_before_time](api/ktk.TimeSeries.get_ts_before_time.rst)
- [ktk.TimeSeries.get_ts_after_time](api/ktk.TimeSeries.get_ts_after_time.rst)
- [ktk.TimeSeries.get_ts_between_times](api/ktk.TimeSeries.get_ts_between_times.rst)
- [ktk.TimeSeries.get_ts_at_event](api/ktk.TimeSeries.get_ts_at_event.rst)
- [ktk.TimeSeries.get_ts_before_event](api/ktk.TimeSeries.get_ts_before_event.rst)
- [ktk.TimeSeries.get_ts_after_event](api/ktk.TimeSeries.get_ts_after_event.rst)
- [ktk.TimeSeries.get_ts_between_indexes](api/ktk.TimeSeries.get_ts_between_indexes.rst)

All these methods do the same: they extract a new TimeSeries using a criteria based on index, time or event. We will once again use [kinetic data of wheelchair propulsion](dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

## Using indexes

If we know that the sync event happened at index 1049 (we could know it using `index = ts.get_index_at_event("sync")`), we could discard any data that happened before this index:

```{code-cell} ipython3
new_ts = ts.get_ts_after_index(1049)
new_ts.plot()
```

## Using time

If we know that the sync event happened at time 4.37 (we could know it using `time = ts.time[ts.get_index_at_event("sync")]`), we could do the same using time:

```{code-cell} ipython3
new_ts = ts.get_ts_after_time(4.37)
```

## Using events

Or, we could simply use the event itself:

```{code-cell} ipython3
new_ts = ts.get_ts_after_event("sync")
```


These methods are very helpful to analyze only specific sections of a TimeSeries. For instance, to analyze only the four first pushes and get rid of any other data, we would do:

```{code-cell} ipython3
# Extract the four pushes
first_four_pushes = ts.get_ts_between_events(
    "push", "push", 0, 4, inclusive=True
)

# Remove the events outside the resulting TimeSeries
first_four_pushes = first_four_pushes.trim_events()

# Plot the result
first_four_pushes.plot()
```

:::{note}
In this example, we set `inclusive=True` to ensure that the push 0 and push 4 events are included in the resulting TimeSeries.
:::

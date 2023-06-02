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

# Indexing TimeSeries

This section shows how to use these methods for TimeSeries indexing:
- [ktk.TimeSeries.get_index_at_time](api/ktk.TimeSeries.get_index_at_time.rst)
- [ktk.TimeSeries.get_index_before_time](api/ktk.TimeSeries.get_index_before_time.rst)
- [ktk.TimeSeries.get_index_after_time](api/ktk.TimeSeries.get_index_after_time.rst)
- [ktk.TimeSeries.get_index_at_event](api/ktk.TimeSeries.get_index_at_event.rst)
- [ktk.TimeSeries.get_index_before_event](api/ktk.TimeSeries.get_index_before_event.rst)
- [ktk.TimeSeries.get_index_after_event](api/ktk.TimeSeries.get_index_after_event.rst)

For this section, we will continue to use [kinetic data from wheelchair propulsion](dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```


Despite the title of this section, we do not index or slice a TimeSeries. Instead, we address its time or data arrays, as for any NumPy array. For instance, to get the time and force data at the 100th sample of the TimeSeries, we would do:

```{code-cell}
print("Time is", ts.time[99])
print("Force is", ts.data["Forces"][99])
```

More practically, we may want to know which index corresponds to a given time. To this effect, we can use [ktk.TimeSeries.get_index_at_time](api/ktk.TimeSeries.get_index_at_time.rst), [ktk.TimeSeries.get_index_before_time](api/ktk.TimeSeries.get_index_before_time.rst):

```{code-cell}
print("The index that is nearest to 15 seconds is:")
print(ts.get_index_at_time(15.0))

print("The index that is just before 15 seconds is:")
print(ts.get_index_before_time(15.0))

print("The index that is just after 15 seconds is:")
print(ts.get_index_after_time(15.0))
```

Or, we may want to know which index corresponds to a given event, using [ktk.TimeSeries.get_index_at_event](api/ktk.TimeSeries.get_index_at_event.rst), [ktk.TimeSeries.get_index_before_event](api/ktk.TimeSeries.get_index_before_event.rst) or [ktk.TimeSeries.get_index_after_event](api/ktk.TimeSeries.get_index_after_event.rst):

```{code-cell}
print("The index that is nearest to 2nd push is:")
print(ts.get_index_at_event("push", occurrence=1))

print("The index that is just before 2nd push is:")
print(ts.get_index_before_event("push", occurrence=1))

print("The index that is just after 2nd push is:")
print(ts.get_index_after_event("push", occurrence=1))
```

The `get_index_before_...` and `get_index_after_...` methods have a parameter `inclusive` that selects if the selection is inclusive (`<=`, `>=`) or exclusive (`<`, `>`):

| Method                                                    | Returns                                |
| --------------------------------------------------------- | -------------------------------------- |
| get_index_before_time(t, inclusive=False)                 | index for nearest time $<$ t           |
| get_index_before_time(t, inclusive=True)                  | index for nearest time $<=$ t          |
| get_index_after_time(t, inclusive=False)                  | index for nearest time $>$ t           |
| get_index_after_time(t, inclusive=True)                   | index for nearest time $>=$ t          |
| get_index_before_event(name, occurrence, inclusive=False) | index for nearest time $<$ event time  |
| get_index_before_event(name, occurrence, inclusive=True)  | index for nearest time $<=$ event time |
| get_index_after_event(name, occurrence, inclusive=False)  | index for nearest time $>$ event time  |
| get_index_after_event(name, occurrence, inclusive=True)   | index for nearest time $>=$ event time | 

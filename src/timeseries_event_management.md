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

# Event management

This section shows how to use these methods for event management:
- [ktk.TimeSeries.add_event](api/ktk.TimeSeries.add_event.rst)
- [ktk.TimeSeries.count_events](api/ktk.TimeSeries.count_events.rst)
- [ktk.TimeSeries.rename_event](api/ktk.TimeSeries.rename_event.rst)
- [ktk.TimeSeries.remove_event](api/ktk.TimeSeries.remove_event.rst)
- [ktk.TimeSeries.sort_events](api/ktk.TimeSeries.sort_events.rst)
- [ktk.TimeSeries.remove_duplicate_events](api/ktk.TimeSeries.remove_duplicate_events.rst)
- [ktk.TimeSeries.trim_events](api/ktk.TimeSeries.trim_events.rst)
- [ktk.TimeSeries.ui_edit_events](api/ktk.TimeSeries.ui_edit_events.rst)

We will use this TimeSeries that contains [cyclic kinetic data in wheelchair propulsion](dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip"))
ts.plot()
```

## Adding events

We already know how to manually add events using [ktk.TimeSeries.add_event](api/ktk.TimeSeries.add_event.rst):

```{code-cell} ipython3
ts = ts.add_event(4.37, "sync")
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

ts.plot()
```

## Counting the number of occurrences of an event

Each event is defined by its name, and if it is repeated multiple times, by an occurrence. To count these occurrences, we use [ktk.TimeSeries.count_events](api/ktk.TimeSeries.count_events.rst):

```{code-cell} ipython3
print(ts.count_events('sync'), " occurrences of event 'sync'")
print(ts.count_events('push'), " occurrences of event 'push'")
print(ts.count_events('recovery'), " occurrences of event 'recovery'")
```

## Renaming events

Renaming events is done using [ktk.TimeSeries.rename_event](api/ktk.TimeSeries.rename_event.rst):

```{code-cell} ipython3
ts = ts.rename_event("push", "lastpush", occurrence=4)
ts = ts.rename_event("recovery", "lastrecovery", occurrence=4)

ts.plot()
```

## Removing events

To remove an occurrence of an event, we use [ktk.TimeSeries.remove_event](api/ktk.TimeSeries.remove_event.rst). For instance, to remove the second push cycle:

```{code-cell} ipython3
ts = ts.remove_event("push", occurrence=1)
ts = ts.remove_event("recovery", occurrence=1)

ts.plot()
```

## Sorting events

Let's put back the push cycle we just removed.

```{code-cell} ipython3
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")

ts.plot()
```

Observe carefully the figure above: what we would expect to be push 1 and recovery 1 are push 3 and recovery 3 instead. We understand that the events are sorted by **order of addition to the TimeSeries**, not by time. This is reflected in the TimeSeries' event list:

```{code-cell} ipython3
ts.events
```

To sort the events in time, we use [ktk.TimeSeries.sort_events](api/ktk.TimeSeries.sort_events.rst):

```{code-cell} ipython3
ts = ts.sort_events()

ts.plot()
```

## Removing duplicate events

It may happen that events get duplicated in a TimeSeries. For instance, we may have added some events twice:

```{code-cell} ipython3
ts = ts.add_event(4.37, "sync")
ts = ts.add_event(8.56, "push")
ts = ts.add_event(9.93, "recovery")
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")
ts = ts.add_event(11.78, "push")
ts = ts.add_event(12.33, "recovery")

ts.plot()
```

Note the superposition of occurrences on the first events. To remove the duplicate events, we use [ktk.TimeSeries.remove_duplicate_events](api/ktk.TimeSeries.remove_duplicate_events.rst):

```{code-cell} ipython3
ts = ts.remove_duplicate_events()
ts.plot()
```

## Trimming events

For some reasons, it may happen that a TimeSeries have events outside its time array. Let's simulate this situation:

```{code-cell} ipython3
ts = ts.add_event(-3.0, "before")
ts = ts.add_event(-1.0, "before")
ts = ts.add_event(23.0, "after")
ts = ts.add_event(25.0, "after")

ts.plot()
```

To remove any event that is outside the TimeSeries' time array, we use [ktk.TimeSeries.trim_events](api/ktk.TimeSeries.trim_events.rst).

```{code-cell} ipython3
ts = ts.trim_events()
ts.plot()
```

## Editing events interactively

Finally, it is possible to edit the events interactively, using [ktk.TimeSeries.ui_edit_events](api/ktk.TimeSeries.ui_edit_events.rst). This allows to add, remove and move events by clicking on a figure.

{{interactive}}

```
ts = ts.ui_edit_events()
```

which gives {numref}`fig_timeseries.ui_edit_events_1` and {numref}`fig_timeseries.ui_edit_events_2`.


```{figure-md} fig_timeseries.ui_edit_events_1
:width: 7in
![timeseries.ui_edit_events](_static/images/fig_timeseries.ui_edit_events_1.png)

Interactive figure created by [ktk.TimeSeries.ui_edit_events](api/ktk.TimeSeries.ui_edit_events.rst)
```

```{figure-md} fig_timeseries.ui_edit_events_2
:width: 4in
![timeseries.ui_edit_events](_static/images/fig_timeseries.ui_edit_events_2.png)

Interactive menu created by [ktk.TimeSeries.ui_edit_events](api/ktk.TimeSeries.ui_edit_events.rst)
```

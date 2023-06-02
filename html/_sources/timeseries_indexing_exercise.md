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

# Exercise: Indexing TimeSeries

Using the following data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write a code that counts the number of pushes and recoveries, and that generates the following lists:

```
push_times  # list[float]: List of times corresponding to each push event
recovery_times  # list[float]: List of times corresponding to each recovery event
```


```{code-cell} ipython3
:tags: [hide-cell]

# Create empty lists
push_times = []
recovery_times = []

# Count the number of pushes/recoveries
n_pushes = ts.count_events("push")
n_recoveries = ts.count_events("recovery")

# Find the push times
for i_push in range(n_pushes):
    index = ts.get_index_at_event("push", occurrence=i_push) 
    push_times.append(ts.time[index])

# Find the recovery times
for i_recovery in range(n_recoveries):
    index = ts.get_index_at_event("recovery", occurrence=i_recovery)
    recovery_times.append(ts.time[index])

# Print it!
print("Push times:", push_times)
print("Recovery times:", recovery_times)
```
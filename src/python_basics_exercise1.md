---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Python basics 1

A sprinter runs through two timing gates spaced by 50 m as shown in {numref}`fig_exercise_timing_gates`. Each timing gate records the time (in seconds) at which the sprinter passes through it.

```{figure-md} fig_exercise_timing_gates
:width: 4in
![](_static/images/fig_exercise_timing_gates.png)

Two timing gates separated by 50 meters.
```

Given the following program:

```
time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters
```

Continue this program so that it prints the mean velocity of the sprinter between gates 1 and 2.

```{code-cell} ipython3
:tags: [hide-cell]

time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters

print(distance_gates12 / (time_gate2 - time_gate1))
```

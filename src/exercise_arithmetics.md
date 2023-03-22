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

# Exercise: Speed on 50 meters

A sprinter runs through two timing gates spaced by 50 m. Each timing gate records the time (in seconds) at which the sprinter passes through it.

![exercices_illustration -width:normal](_static/images/exercise_timing_gates.png)

Given the following program:

```
time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters
```

Continue this program so that it prints the mean velocity of the sprinter between gates 1 and 2. You can then show a suggested answer by clicking on the plus sign below.

```{code-cell} ipython3
:tags: [hide-cell]

time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters

print(distance_gates12 / (time_gate2 - time_gate1))
```

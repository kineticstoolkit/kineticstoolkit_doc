---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Function argument's default values

Let's repeat the [timing gate exercise](python_basics_exercise1.md), but this time using a proper function.

A sprinter runs through two timing gates spaced by 50 m as shown in {numref}`fig_exercise_timing_gates`. Each timing gate records the time (in seconds) at which the sprinter passes through it.

Write a function named `calculate_speed` that takes two mandatory arguments, which are the time of each timing gate, and that returns the mean velocity of the sprinter between gates 1 and 2, so that calling:

```
print(calculate_speed(1.3, 6.7))
```

prints a value of 9.2593.

In addition, this function should accommodate alternate distances between the timing gates, specified by a facultative argument named `distance_gates12`:

```
calculate_speed(1.3, 6.7, distance_gates12=75)
```

Do not forget to include a docstring to your function.


```{code-cell} ipython3
:tags: [hide-cell]

def calculate_speed(time_gate1, time_gate2, distance_gates12=50):
    """
    Calculate the average velocity between two timing gates.

    Parameters
    ----------
    time_gate1, time_gate2 : float
        Time at which the athlete passed through the gate, in seconds.
    distance_gates12 : float
        Optional. Distance between both timing gates, in meters. Default is 50.

    Returns
    -------
    float
        The velocity, in m/s.

    """

    return distance_gates12 / (time_gate2 - time_gate1)


# Test the function:
print(calculate_speed(1.3, 6.7))
print(calculate_speed(1.3, 6.7, distance_gates12=75))
```

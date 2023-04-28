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

# Exercise: Indexing lists 1

We measured some spatial parameters of gait using an instrumented walkway, as illustrated in Figure 1. This instrumented walkway stores the longitudinal distance between the origin and each heel strike in a list `y`, where each element corresponds to one heel strike, as shown in {numref}`fig_instrumented_walkway`.

```{figure-md} fig_instrumented_walkway
:width: 7in
![](_static/images/fig_instrumented_walkway.png)

Foot coordinates obtained via an instrumented walkway.
```

We want to calculate the step length, which is the distance between one heel strike and the next one by the opposite foot. For a given participant, we recorded this `y` list:

```{code-cell} ipython3
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write and test this function:

```
def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length.
    """
```

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_step_length(y, step):
    return y[step + 1] - y[step]

# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
```

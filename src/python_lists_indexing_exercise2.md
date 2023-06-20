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

# Exercise: Indexing lists 2

You are happy with the function `calculate_step_length` you wrote in the [previous exercise ](python_lists_indexing_exercise1.md), but sometimes, you obtain an IndexError:

```{code-cell} ipython3
:tags: [remove-cell]
def calculate_step_length(y, step):
    return y[step + 1] - y[step]
```

```{code-cell} ipython3
:tags: [raises-exception]
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

calculate_step_length(y, 9)
```

**Question 1)** Explain why this call produces an IndexError.

:::{toggle}
This happens because to calculate a step length, we need two consecutive heel strikes. To calculate the length of step 9, we need heel strikes 9 and 10. However, the last element of `y` is at index 9.

One way to avoid this error is to check that we won't index the list out of its range, before calculating the step length.
:::

**Question 2)** Modify your function so that instead of producing this error, it simply returns 0.

:::{good-practice} Invalid data
For this example, we ask to return 0 for invalid data, but a better practice would be to return {{np_nan}}, which will be seen in section [](numpy_inf_nan.md). Simply return 0 for now since we didn't see NumPy yet.
:::

```{code-cell} ipython3
:tags: [hide-cell]

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
        The requested step length, or 0 if this step could not be calculated.
    """
    if step + 1 < len(y):
        return y[step + 1] - y[step]
    else:
        return 0.0


# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
print(calculate_step_length(y, 9))
```

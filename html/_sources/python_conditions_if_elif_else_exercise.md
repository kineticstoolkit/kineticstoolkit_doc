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

# 💪 Conditions: if/elif/else

We have three timing gates. We want to know if an athlete has accelerated, decelerated, or kept a constant speed between gates 1-2 and gates 2-3.

Write a function with the following signature and docstring:

```
def compare_speed(time1, time2, time3, distance12, distance23):
    """
    Check if an athlete accelerated or decelerated based on timing gates.

    Parameters
    ----------
    time1, time2, time3 : float
        Time at which the athlete passed through timing gate 1, 2, 3,
        in seconds.
    distance12, distance23 : float
        Distance between timing gates 1 and 2; and between timing gates
        2 and 3.

    Returns
    -------
    str
        Returns "accelerated", "decelerated", or "kept constant" according
        to the calculation.

    """
```


```{code-cell} ipython3
:tags: [hide-cell]


def compare_speed(time1, time2, time3, distance12, distance23):
    """
    Check if an athlete accelerated or decelerated based on timing gates.

    Parameters
    ----------
    time1, time2, time3 : float
        Time at which the athlete passed through timing gate 1, 2, 3,
        in seconds.
    distance12, distance23 : float
        Distance between timing gates 1 and 2; and between timing gates
        2 and 3.

    Returns
    -------
    str
        Returns "accelerated", "decelerated", or "kept constant" according
        to the calculation.

    """
    speed1 = distance12 / (time2 - time1)
    speed2 = distance23 / (time3 - time2)

    if speed2 > speed1:
        return "accelerated"
    
    elif speed2 < speed1:
        return "decelerated"

    else:
        return "kept constant"


# Test the function:
print(compare_speed(1.0, 2.0, 3.0, 50, 50))
print(compare_speed(1.0, 2.0, 3.5, 50, 50))
print(compare_speed(1.0, 2.0, 2.5, 50, 50))

```


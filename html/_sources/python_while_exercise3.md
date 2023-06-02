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

# Exercise: Looping using **while** 3

Using a force plate, we recorded the vertical ground reaction force during one step, at a sampling frequency of 20 Hz:

```{code-cell}
grf = [
    0.5, 0.9, 0.2, 0.0, 0.3, 0.2, 0.4, 0.7, 5.5, 7.1, 4.5, 37.7, 180.8,
    400.2, 603.1, 598.4, 584.2, 620.6, 635.5, 602.7, 246.0, 14.5, -1.2,
    -0.7, 0.4, 0.5, 0.8, 0.6
]
```

```{code-cell}
:tags: [remove-input]
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(len(grf))/20, grf)
plt.xlabel('Time (s)')
_ = plt.ylabel('Force (N)')
```

We consider that the step begins when the force exceeds a given threshold, and that it ends when the force stops exceeding this threshold. Write the function `calculate_step_time` that calculates the duration of the step, then test it with a threshold of 50 N.

```
def calculate_step_time(grf, threshold, sampling_frequency):
    """
    Calculate the step time using vertical ground reaction forces.

    Parameters
    ----------
    grf : list[float]
        A list of vertical ground reaction forces in newtons. There must
        be only one step in this list.
    threshold : float
        A value above which we consider the step begins, and below which
        the step ends.
    sampling_frequency :
        The sampling frequency in Hz.

    Returns
    -------
    float
        The duration of the step.

    """
```

:::{tip}
- Start by finding at which index the step begins.
- From this index, find at which index the step ends.
- Calculate the step time using the difference between the indexes and the sampling frequency.
:::

```{code-cell}
:tags: [hide-cell]
def calculate_step_time(grf, threshold, sampling_frequency):
    # Find i_begin
    current_index = 0
    while grf[current_index] < threshold:
        current_index += 1
    i_begin = current_index

    # Find i_end
    while grf[current_index] >= threshold:
        current_index += 1
    i_end = current_index

    # Calculate and return the time step
    return (i_end - i_begin) / sampling_frequency

# Test it
calculate_step_time(grf, threshold=50, sampling_frequency=20)
```


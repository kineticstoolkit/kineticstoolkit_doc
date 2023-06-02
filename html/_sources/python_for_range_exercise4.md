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

# Exercise: Looping using **for** and **range** 4

Knowing that:

```{math}
v(t) = \left( {p(t+1) - p(t-1)} \right) * \dfrac{\text{sampling frequency}}{2}
```

write this function:

```
def calculate_speed(position, sampling_frequency):
    """
    Calculate speed based on position.

    Parameters
    ----------
    position : list[float]
        A list of positions in meters.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.

    Returns
    -------
    list[float]
        A list of speeds in m/s. This list is the same size as `position`.
        Since speed cannot be calculated on first and last time, values
        of zero are returned for these times.
    
    """

```

and test it with the following position values that were sampled at 100 Hz:

```{code-cell}
list_of_positions = [
    30.5, 30.511, 30.523, 30.535, 30.548, 30.56, 30.572, 30.584, 30.595, 30.606,
    30.619, 30.631, 30.645, 30.658, 30.672, 30.687, 30.702, 30.716, 30.731,
    30.746, 30.763, 30.779, 30.795, 30.81, 30.824, 30.838, 30.853, 30.868, 30.884,
    30.901, 30.917, 30.934, 30.951, 30.969, 30.988, 31.006, 31.024, 31.042, 31.059,
    31.076, 31.092, 31.109, 31.125, 31.143, 31.161, 31.178, 31.196, 31.214, 31.232,
    31.25
]
```

:::{tip}
It will be impossible to calculate speed on the first sample, because it would need the position before the first sample. It will also be impossible to calculate speed on the last sample, because it would need the position after the last sample. Simply fill the first and last sample of the speed with zero as shown in {numref}`fig_padding_speed_with_zero`.
:::

```{figure-md} fig_padding_speed_with_zero
:width: 6in

![](_static/images/fig_padding_speed_with_zero.png)

Padding the first and last indexes of `speed` with zeros.
```


```{code-cell}
:tags: [hide-cell]
def calculate_speed(position, sampling_frequency):
    speed = [0]  # First element

    # Calculate speed for every element but first and last
    for i in range(1, len(position) - 1):
        speed.append((position[i+1] - position[i-1]) * sampling_frequency / 2)

    speed.append(0)  # Last element
    return speed

# Test this function
calculate_speed(list_of_positions, 100)
```

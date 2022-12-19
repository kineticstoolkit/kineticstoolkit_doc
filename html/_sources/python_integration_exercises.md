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

# 📖 Integration exercises

:::{card} Summary
This section proposes exercises to integrate the basic python notions viewed in the previous sections.
:::

At this point, we viewed just enough of the python language to be able to process an impressing number of data. We saw:

- how to store and access data in memory using [variables](python_arithmetics_and_variables.md) such as [strings](python_strings.md), [integers](python_numbers.md), [floats](python_numbers.md), [lists](python_lists.md) and [dictionaries](python_dicts.md);
- how to perform [python_arithmetics_and_variables](python_arithmetics_and_variables.md) operations such as addition, subtraction, multiplication and division;
- how to check for [python_conditions](python_conditions.md) and perform operation according to these conditions;
- how to [repeat code](python_looping.md) several times or [loop through lists](python_for_range.md) or [dictionaries](python_dicts.md);
- decompose code in smaller [functions](python_functions.md).

Obviously, using higher level libraries such as [numpy](numpy.md), [matplotlib](matplotlib.md) and [pandas](pandas.md) (which will follow in the next chapter) will make such data processing much easier and powerful. But in the mean time, it is already possible to solve these exercises, using only the subset of python that we just learned.

## 💪 Exercise 1: Calculation of power based on force and velocity

Someone pushes on a carriage using a dynamometer, in such a way that we get a measurement of the contact force in newtons every tenth of a second, during five seconds.

```{code-cell}
push_force = [
    91.19, 99.22, 93.11, 91.76, 94.93, 96.54, 92.27, 96.01, 92.48,
    94.89, 91.55, 90.82, 97.91, 93.19, 95.65, 93.07, 93.65, 90.57,
    98.71, 99.97, 95.72, 96.27, 92.67, 93.4 , 98.84, 92.63, 97.03,
    93.93, 98.34, 95.82, 99.39, 99.29, 92.74, 90.29, 94.57, 90.69,
    93.16, 95.01, 93.16, 97.04, 97.23, 98.9 , 90.26, 97.46, 92.4 ,
    90.84, 97.39, 93.56, 97.47, 93.93
]
```

At the same time, an odometer reports the carriage speed in m/s, also every tenth of a second.

```{code-cell}
carriage_speed = [
    1.05, 1.08, 1.04, 1.09, 1.04, 1.06, 1.04, 1.05, 1.05, 1.05, 1.04,
    1.01, 1.09, 1.09, 1.05, 1.01, 1.06, 1.03, 1.08, 1.08, 1.09, 1.00,
    1.00, 1.00, 1.01, 1.05, 1.06, 1.03, 1.07, 1.02, 1.03, 1.07, 1.07,
    1.02, 1.04, 1.06, 1.00, 1.01, 1.00, 1.04, 1.08, 1.00, 1.02, 1.06,
    1.03, 1.06, 1.05, 1.01, 1.04, 1.00,
]
```

Write this function, knowing that power equals force times speed:

```
def calculate_power(force, speed):
    """
    Calculate the power according to force and speed.

    Parameters
    ----------
    force : list[float]
        A list of forces in newtons.
    speed : list[float]
        A list of speeds in m/s. Its length must be the same as force.

    Returns
    -------
    list[float]
        A list of powers in watts.

    """
```

and use it to calculate the power developed by the person to push the carriage.

```{code-cell}
:tags: [hide-cell]

def calculate_power(force, speed):
    power = []  # Initialize the output list
    
    for i in range(len(force)):
        power.append(force[i] * speed[i])

    return power

# Test the function with the supplied data
calculate_power(push_force, carriage_speed)
```


## 💪 Exercise 2: Calculation of speed based on position

Knowing that:

$v(t) = \left( {p(t+1) - p(t-1)} \right) * \dfrac{\text{sampling frequency}}{2}$

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

## 💪 Exercise 3: Calculation of velocity and power based on position and force

We repeat exercise 1, but this time instead of measuring the speed of the carriage, we measure its position. We have these two lists where data has been acquired at a sampling frequency of 10 Hz.

```{code-cell}
push_force = [
    91.19, 99.22, 93.11, 91.76, 94.93, 96.54, 92.27, 96.01, 92.48,
    94.89, 91.55, 90.82, 97.91, 93.19, 95.65, 93.07, 93.65, 90.57,
    98.71, 99.97, 95.72, 96.27, 92.67, 93.4 , 98.84, 92.63, 97.03,
    93.93, 98.34, 95.82, 99.39, 99.29, 92.74, 90.29, 94.57, 90.69,
    93.16, 95.01, 93.16, 97.04, 97.23, 98.9 , 90.26, 97.46, 92.4 ,
    90.84, 97.39, 93.56, 97.47, 93.93
]

carriage_position = [
    111.5, 111.613, 111.73, 111.852, 111.98, 112.103, 112.225, 112.34,
    112.452, 112.567, 112.692, 112.818, 112.952, 113.085, 113.228, 113.37,
    113.52, 113.666, 113.813, 113.969, 114.13, 114.296, 114.454, 114.602,
    114.749, 114.887, 115.033, 115.186, 115.347, 115.511, 115.676, 115.844,
    116.017, 116.199, 116.386, 116.568, 116.745, 116.922, 117.095, 117.262,
    117.424, 117.592, 117.757, 117.931, 118.113, 118.289, 118.469, 118.644,
    118.826, 119.001
 ]
```

Write a function named `calculate_speed_and_power` that would have this docstring:

```
def calculate_speed_and_power(force, position, sampling_frequency):
    """
    Calculate speed and power based on force and position.

    Parameters
    ----------
    force : list[float]
        A list of forces in newtons.
    position : list[float]
        A list of positions in meters. Its length must be the same as `force`.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.
        
    Returns
    -------
    list[dict]
        A list of the same length of `force` and `position`, that contains
        dictionaries with the following keys:
        - 'Force': force in newtons
        - 'Position': position in meters
        - 'Speed': speed in m/s
        - 'Power': power in watts.

    Example
    -------
    To get the power at the 5th sample, we would do:
    >>> data = calculate_speed_and_power(force, position, sampling_frequency)
    >>> power_5th_sample = data[4]['Power']

    """
```

:::{tip}
You are encouraged to reuse the functions you wrote in exercises 1 and 2.
:::

```{code-cell}
:tags: [hide-cell]
def calculate_speed_and_power(force, position, sampling_frequency):
    # Calculate speed based on position
    speed = calculate_speed(position, sampling_frequency)

    # Calculate power based on speed and force
    power = calculate_power(force, speed)

    # Generate a list of dictionaries with this information
    output = []
    for i in range(len(position)):
        output.append(
            {
                "Force": force[i],
                "Position": position[i],
                "Speed": speed[i],
                "Power": power[i],
            }
        )
        
    return output

# Test it
data = calculate_speed_and_power(
    push_force,
    carriage_position,
    sampling_frequency=10
)

data[4]
```

## 💪 Exercise 4: Calculation of step time using a force threshold

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


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

# Exercise: Trigonometry 1

A ball is thrown horizontally with a constant horizontal velocity of 10 m/s and with no initial vertical velocity at release. Once released, its horizontal velocity remains constant while its vertical velocity increases negatively at a rate of 9.81 m/s². Plot a curve of its total speed for one second after release. The total speed is the magnitude (norm) of the vector created by the horizontal velocity and the vertical velocity, as shown in {numref}`fig_falling_ball_horizontal`.

```{figure-md} fig_falling_ball_horizontal
:width: 3.5in
![](_static/images/fig_falling_ball_horizontal.png)

A falling ball with both horizontal and vertical velocity components.
```


::::{tip}
:::{toggle}
You already calculated the vertical velocity in [](numpy_arithmetics_exercise.md). Now use the Pythagorean theorem with arithmetic operations on arrays to calculate the total speed `v_total` based on `v_x` and `v_y`.
:::
::::

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np
import matplotlib.pyplot as plt

# First, let's define a time array
t = np.linspace(0, 1, 100, endpoint=False)

# Calculate the vertical velocity as -9.81 * t
v_y = -9.81 * t

# Constant horizontal speed of 10 m/s2
v_x = 10

# Calculate the total speed
v_total = np.sqrt(v_x**2 + v_y**2)

# Plot it
plt.plot(t, v_total)
plt.xlabel("Time (s)")
plt.ylabel("Total speed (m/s)")
plt.grid()
plt.show()
```

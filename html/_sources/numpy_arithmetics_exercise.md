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

# Exercise: Arithmetics

A ball is released from a point in air. Knowing that it was immobile when it was released, and that it gains negative speed at a rate of 9.81 m/s², plot a curve of its velocity as shown in {numref}`fig_falling_ball` during one second from release time.

```{figure-md} fig_falling_ball
:width: 3in
![](_static/images/fig_falling_ball.png)

Vertical velocity of a falling ball.
```

::::{tip}
:::{toggle}
Start by creating a time array using {{np_arange}} or {{np_linspace}}. Then, use this time array to create a velocity array. Finally, plot the velocity as a function of time.
:::
::::

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np
import matplotlib.pyplot as plt


# First, let's define a time array
t = np.linspace(0, 1, 100, endpoint=False)

# Calculate the velocity as -9.81 * t
v = -9.81 * t

# Show it
plt.plot(t, v)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()
```

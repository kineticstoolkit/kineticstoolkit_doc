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

# 💪 Exercise 1

A ball is threw horizontally with a constant horizontal velocity of 10 m/s, and with no initial vertical velocity at release time. Once released, its horizontal velocity stays constant while its vertical velocity increases negatively at a rate of 9.81 m/s². Plot a curve of its total speed during one second from release time. The total speed is the norm of the vector created by the horizontal velocity and the vertical velocity:

![Exercise 2 -height:short](_static/images/ball_total_speed.png)

::::{tip}
:::{toggle}
You already calculated the vertical velocity `v_y` in the previous exercise. Now use the Pythagorean theorem using arithmetic operations on arrays to calculate the total speed `v_total` based on `v_x` and `v_y`.
:::
::::

```{code-cell} ipython3
:tags: [hide-cell]

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

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


# Exercise: Plotting a series 2

Using a video camera, you recorded the position of a sprinter each 2 seconds. The recorded data are:

```{code-cell} ipython3
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters
```

You also used five timing gates placed at positions 0m, 25m, 50m, 75m and 100m. The time recorded by these timing gates are:

```{code-cell} ipython3
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]
```

Write a code that produces this figure:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt


plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True);
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]
import matplotlib.pyplot as plt


plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend(["Video camera", "Timing gates"]);
```

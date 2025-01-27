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

# Exercise: Plot styling

In [](matplotlib_plot_titles_labels_exercise2.md), using these data:

```{code-cell} ipython3
# Video camera data
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # metres

# Timing gates data (placed at positions 0m, 25m, 50m, 75m, and 100m)
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]  # seconds
```

you generated the following figure:

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

You now need to print it in black and white for publication in a journal. To maximize the clarity of the figure, you want to use markers and line styles instead of grey shades.

Generate the figure again, but this time with these specifications:

- The video camera curve must be a solid black line with square markers.
- The timing gates curve must be a dashed black line with round markers.

```{code-cell} ipython3
:tags: [hide-cell]
import matplotlib.pyplot as plt

plt.plot(t, p, "s-k")
plt.plot(timing_gates_time, [0, 25, 50, 75, 100], "o--k")
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True);
```

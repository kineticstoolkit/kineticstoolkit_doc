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


# 💪 Exercise 2

During the same race, you also used five timing gates placed at positions 0m, 25m, 50m, 75m and 100m. The time recorded by these timing gates are:

```{code-cell} ipython3
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]
```

Write a code that produces this figure:

```{code-cell} ipython3
:tags: [remove-input]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True)
plt.show()
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend(["Video camera", "Timing gates"])
```

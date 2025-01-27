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


# Exercise: Looping using **while** 1

Using an instrumented walkway, we recorded the following positions of heel strike, first for the right heel, then for the left heel, then for the right heel, and son on according to {numref}`fig_instrumented_walkway`.

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write a program that creates a list named `step_lengths` which contains the length of every step. The first step length should be `y[1] - y[0]`, the second should be `y[2] - y[1]`, and so on. In this specific example, we recorded nine steps, but your code should work for any number of steps.

```{code-cell}
:tags: [hide-cell]

# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
i = 0
while i < n_steps:
    step_lengths.append(y[i + 1] - y[i])
    i += 1

# Done
step_lengths
```

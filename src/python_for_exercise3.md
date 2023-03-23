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


# Exercise 3

Let's redo this [exercise](python_while_exercise1.md), this time with a `for` instead of a `while`.

Using an instrumented walkway, we recorded the following positions of heel strike, first for the right heel, second for the left heel, third for the right heel, etc.:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

![Instrumented walkway -width:full](_static/images/instrumented_walkway.png)

*Figure 1. Foot coordinates obtained via an instrumented walkway*

Write a program that creates a list named `step_lengths`, that contains the length of every step. The first step length would be `y[1] - y[0]`, the second would be `y[2] - y[1]`, etc. In this specific example, we recorded nine steps, but your code must work on any number of steps.

```{code-cell}
:tags: [hide-cell]

# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
for i in range(n_steps):
    step_lengths.append(y[i + 1] - y[i])

# Done!
step_lengths
```

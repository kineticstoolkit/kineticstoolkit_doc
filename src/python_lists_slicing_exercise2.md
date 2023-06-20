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

# Exercise: Slicing lists 2

Let's get back to the spatial parameters of gait measured [previously](python_lists_indexing_exercise1.md). For a given participant, we recorded this `y`:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

If we know that the first element of `y` always corresponds to the y-coordinate of the right foot, write a 2-line code that separates `y` into two lists:
- `y_right`, which contains the y-coordinates of all heel strikes for the right foot
- `y_left`, which contains the y-coordinates all heel strikes for the left foot

```{code-cell} ipython3
:tags: [hide-cell]

y_right = y[0::2]
y_left = y[1::2]

# Print the results
print(f"Right foot: {y_right}")
print(f"Left foot: {y_left}")
```

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


# Exercise: Indexing/slicing/filtering one-dimensional arrays 1

We measured the step length of a person during 10 steps. Here are these measurements:

```{code-cell} ipython3
import numpy as np

step_length = np.array(
    [0.707, 0.730, 0.752, 0.707, 0.691, 0.726, 0.722, 0.726, 0.710, 0.661]
)  # in meters
```

For each of these questions, write a single line of code that prints the requested step lengths.

1. From the third step up to the end;
2. The last two steps;
3. All steps, but without the first two and the last two;
4. Every other step starting from the third;
5. Steps 2, 5, 6, and 7, with step 0 being the first.
6. The first and the last.

```{code-cell} ipython3
:tags: [hide-cell]

# 1. From the third step up to the end;
print(step_length[2:])

# 2. The two last steps;
print(step_length[-2:])

# 3. All steps, but without the two firsts and the two lasts;
print(step_length[2:-2])

# 4. Every other step starting from the third;
print(step_length[2::2])

# 5. Steps 2, 5, 6, 7, with step 0 being the first.
print(step_length[[2, 5, 6, 7]])
# Note the double bracket: this is equivalent to write:
# >> mask = [2, 4, 6, 7]
# >> step_length[mask]

# 6. The first and the last.
print(step_length[[0, -1]])
```

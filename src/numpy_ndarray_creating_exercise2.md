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

Unfortunately, during the experiment of [exercise 1](numpy_ndarray_creating_exercise1.md), the dynamometer was not plugged in, and you only recorded a series of zero. Using one line of code, create a NumPy array named `force` that is the same shape as `time`, but that only contains zeros.

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np

# We use the shape of `time` to create an array filled with zeros.

force = np.zeros(time.shape)

force
```

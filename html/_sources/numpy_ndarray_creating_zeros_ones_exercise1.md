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

# Exercise: Creating arrays using zeros and ones 1

We recorded the force measured by a dynamometer at a sampling frequency of 100 Hz, during 2.5 seconds. Unfortunately, the dynamometer was not plugged in, and we only recorded a series of zero.

Using one line of code, create a NumPy array named `force` that contains this series of zeros.

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np

# The number of points is 2.5 * 100Hz = 250.

force = np.zeros(250)

force
```

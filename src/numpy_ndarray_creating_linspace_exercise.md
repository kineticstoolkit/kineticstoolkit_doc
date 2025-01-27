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

# Exercise: Creating linearly spaced arrays

We recorded the force measured by a dynamometer at a sampling frequency of 100 Hz for 2.5 seconds.

Using one line of code (excluding the `import` line), create a NumPy array named `time` that represents the time corresponding to each sample. The first element of this array will be 0, the second will be 0.01, and so on.

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np

# The initial time is 0 s
# The final time corresponds to 2.5 seconds
# The number of points is 2.5 * 100Hz = 250.

time = np.linspace(0, 2.5, 250, endpoint=False)

# Note that if we interpret the question to include the final time, then we
# need to increase the number of points by 1 to include this new point:
# >> time = np.linspace(0, 2.5, 251)

time
```
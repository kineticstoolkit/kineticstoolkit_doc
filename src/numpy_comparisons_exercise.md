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


# Exercise: Comparisons

We recorded this series of vertical forces using a gait force platform:

```{code-cell} ipython3
import numpy as np

force = np.array(
    [
        17.61, 21.42, 17.61, 17.61, 17.61, 32.85, 25.23, 17.61, 29.04, 32.85,
        25.23, 21.42, 67.14, 810.0, 870.95, 802.38, 726.19, 775.71, 947.14,
        985.23, 954.76, 863.33, 783.33, 676.66, 520.47, 295.71, 150.95, 48.09,
        -1.42, 2.38, 17.61, 2.38, 6.19, 6.19, 6.19, 2.38, 6.19, 13.80,
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]

import matplotlib.pyplot as plt
import kineticstoolkit.lab as ktk

plt.plot(force)
plt.xlabel("# sample")
plt.ylabel("Force (N)");
```

We want to identify the weight support phase. We define this phase as any sample where the force is higher than 100 newton.

- Write a one-line code that creates a NumPy array named `is_weight_support`, which has the same shape as `force`, and that contains `True` during the weight support phase, and `False` otherwise.

- Verify your code by plotting both `force` and `is_weight_support` on the same figure.

```{code-cell} ipython3
:tags: [hide-cell]
import matplotlib.pyplot as plt

# We create a mask to keep only the weight support phase
is_weight_support = force > 100

# Verify
plt.plot(force, label="Force (N)")
plt.plot(is_weight_support * 1000, label="Weight support (True/False)")
plt.legend();

# Note that we plotted (is_weight_support * 1000) instead of
# is_weight_support to match the vertical scale of the force plot
# so that the comparison is more visible on the figure.
```

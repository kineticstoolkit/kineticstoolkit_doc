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


# Creating arrays of zeros or ones

To create arrays filled with zeros or ones, we use the {{np_zeros}} and {{np_ones}} functions, which both take the shape of the array to create:

```{code-cell} ipython3
import numpy as np

np.zeros((2, 5))
```

```{code-cell} ipython3
np.ones((3, 4))
```

:::{tip}
Note the double parentheses. The argument of {{np_zeros}} and {{np_ones}} is a shape, which is a tuple. Writing `np.zeros(2, 5)` would generate an error, since this is not one tuple argument, but two integer arguments.
:::

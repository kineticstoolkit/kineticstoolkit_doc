---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

# Importing NumPy

It is very common to import NumPy using the `np` alias:

```{code-cell}
import numpy as np
```

So that every NumPy function is available under the `np` namespace:

```{code-cell}
np.mean([1, 2, 3])
```

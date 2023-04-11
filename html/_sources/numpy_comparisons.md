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

# Comparisons

As for [arithmetic operations on NumPy arrays](numpy_arithmetics.md), we can use comparison operators such as `>` or `==` to compare two arrays element-wise. In this case, the result is an array of bool:

```{code-cell} ipython3
import numpy as np

a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
    ]
)

b = np.array(
    [
        [5.0, 5.0, 5.0],
        [5.0, 5.0, 5.0],
        [5.0, 5.0, 5.0],
    ]
)

a > b
```


Comparisons can be made with a single number instead of a whole array:

```{code-cell} ipython3
a > 5.0
```

```{code-cell} ipython3
a == 5.0
```

```{code-cell} ipython3
a >= 5.0
```

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

We can use comparison operators such as `>` or `==` to compare two arrays element-wise. In this case, the result is an array of booleans:

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


We can also compare arrays with a single number instead of another array:

```{code-cell} ipython3
a > 5.0
```

```{code-cell} ipython3
a == 5.0
```

```{code-cell} ipython3
a >= 5.0
```


To find the indices of the array where the comparison returned true, we can use {{np_nonzero}}:

```{code-cell}
a = np.array([1.0, 2.2, 10.4, 4.6, 5.8, 6.0, 1.2])

print("Result of the comparison:", a > 5)
print("Indices where the result was True:", np.nonzero(a > 5))
```

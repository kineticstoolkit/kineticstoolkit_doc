---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Arithmetics

All Python arithmetic operators (`+`, `-`, `*`, `/`, `**`) work directly on NumPy arrays, assuming both arrays have the same shape. Operations are performed between each element of a same position. For example, using `a + b`, the 1st element of `a` is summed with the 1st element of `b`, the 2nd of `a` with the 2nd of `b`, etc.:

```{code-cell} ipython3
import numpy as np

a = np.array(
    [
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
    ]
)

b = np.array(
    [
        [1.0, 1.0, 1.0],
        [2.0, 2.0, 2.0],
    ]
)
```

**Addition**:

```{code-cell} ipython3
a + b
```

**Subtraction**:

```{code-cell} ipython3
a - b
```

**Multiplication**:

```{code-cell} ipython3
a * b
```

**Division**:

```{code-cell} ipython3
a / b
```

**Exponent**:

```{code-cell} ipython3
a**b
```

It is also possible to perform operations between an array and a single number.

**Addition**:

```{code-cell} ipython3
a + 1
```

**Subtraction**:

```{code-cell} ipython3
a - 1
```

etc.

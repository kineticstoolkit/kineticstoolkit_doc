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

# Creating linearly spaced arrays

## Linear spacing: np.arange

It is very common to generate unidimensional arrays of equally spaced values, such as `[0, 1, 2, 3, 4]` or `[0, 0.1, 0.2, 0.3]`. We could do it using:

```{code-cell} ipython3
import numpy as np

np.array(range(5))
```

which creates a range from 0 (incl.) to 5 (excl.), then converts this range to an array. NumPy provides a shortcut for it: {{np_arange}}

```{code-cell} ipython3
np.arange(5)
```

This function takes the same arguments as the Python's [range](python_for.md) function.

:::{good-practice} np.arange
While `range` only takes integers as arguments, `np.arange` also accepts floats. For example:

```
np.arange(0, 0.5, 0.1)
```

generates:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```

However, this practice is not recommended due to potential floating point problems that can generate surprising results. Without going further into these issues, just remind that in most cases, `np.arange` should be used only with integers. For the example above:

```
np.arange(5) / 10
```

is safer and gives the same result:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```
:::

## Linear spacing: np.linspace

Another function to create equally spaced series of float is {{np_linspace}}, which takes as arguments the initial value, the final value, and the number of points in the new array. By default, `np.linspace` includes both the initial and final values. For example, to create an array that goes from 5.0 (included) to 10.0 (included) and that contains 11 elements:

```{code-cell} ipython3
np.linspace(5.0, 10.0, 11)
```

To exclude the final value, we set the `endpoint` argument to False.

```{code-cell} ipython3
np.linspace(5.0, 10.0, 10, endpoint=False)
```

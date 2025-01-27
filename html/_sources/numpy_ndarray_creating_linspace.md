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

It is very common to generate one-dimensional arrays of equally spaced values, such as `[0, 1, 2, 3, 4]` or `[0, 0.1, 0.2, 0.3]`. We can do it using:

```{code-cell} ipython3
import numpy as np

np.array(range(5))
```

which creates a range from 0 (inclusive) to 5 (exclusive), then converts this range to an array. NumPy provides a shortcut for this: {{np_arange}}

```{code-cell} ipython3
np.arange(5)
```

This function takes the same arguments as Python's [range](python_for.md) function.

:::{good-practice} np.arange
While `range` only accepts integers as arguments, `np.arange` also accepts floats. For example:

```
np.arange(0, 0.5, 0.1)
```

generates:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```

However, this practice is not always recommended due to potential floating-point issues that cannot guarantee the length of the resulting array. Without delving further into these issues, just remind that in most cases, `np.arange` should be used only with integers. For the example above:

```
np.arange(5) / 10
```

is safer and gives the same result:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```
:::

Another function to create equally spaced series of floats is {{np_linspace}}, which takes as arguments the initial value, the final value, and the number of points in the new array. By default, `np.linspace` includes both the initial and final values as arguments. For example, to create an array that goes from 5.0 (inclusive) to 10.0 (inclusive) and that contains 11 elements:

```{code-cell} ipython3
np.linspace(5.0, 10.0, 11)
```

To exclude the final value, set the `endpoint` argument to False.

```{code-cell} ipython3
np.linspace(5.0, 10.0, 10, endpoint=False)
```

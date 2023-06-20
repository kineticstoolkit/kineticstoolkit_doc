---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Filtering unidimensional arrays

:::{important}
This section is about manipulating NumPy arrays, and more precisely about selecting specific indexes in an array using a mask of booleans or integers. This is not about filtering a time series using a moving average or Butterworth filter, which will be seen later in section [](filters.md).
:::

We learned how to access **one data** using indexing, and **multiple regularly-spaced data** using slicing. To read **multiple non-regularly-spaced data**, we use filtering. We call it filtering because we selectively filter out some data using a mask.

Using these NumPy arrays:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

data = np.array([0.0, 0.58, 0.95, 0.95, 0.58, 0.0, -0.59, -0.96, -0.96, -0.59])
time = np.arange(10) / 10
```

Let's say we want to keep only the following indexes:

```{code-cell} ipython3
:tags: [remove-input]

bool_mask = [True, False, False, True, False, False, False, False, True, True]

plt.plot(time, data, "s-")
for i, value in enumerate(bool_mask):
    if value:
        plt.text(
            time[i],
            data[i] + 0.04,
            "$\checkmark$",
            ha="center",
            fontsize=50,
            color="g",
        )
    else:
        plt.text(
            time[i], data[i] + 0.04, "x", ha="center", fontsize=30, color="r"
        )
plt.grid(True);        
```

We can create a mask to select directly which items to keep, and which items to reject.

This mask can be either a **boolean** mask, which is the same shape as `data`, and where each data to keep is True, and where each data to discard is False:

```{code-cell} ipython3
bool_mask = [True, False, False, True, False, False, False, False, True, True]
```

of an **integer** mask, where we explicitly list the indexes to keep:

```{code-cell} ipython3
int_mask = [0, 3, 8, 9]
```

In any case, we then use this mask between brackets, as we would index or slice the array:

```{code-cell} ipython3
plt.subplot(3,1,1)
plt.plot(time, data, "s-")
plt.title("Original data")

plt.subplot(3,1,2)
plt.plot(time[bool_mask], data[bool_mask], "s-")
plt.title("Filtered data, using a mask of bool")

plt.subplot(3,1,3)
plt.plot(time[int_mask], data[int_mask], "s-")
plt.title("Filtered data, using a mask of int")

plt.tight_layout();
```

:::{tip}
Since indexes can also be negative, then masks of integers can also use negative values.
:::

In section [](numpy_arithmetics.md), we learned how to generate arrays of bool by comparing an array to a number using comparison operators such as `==`, `<`, `>=`, etc. These comparisons are a powerful way to filter an array. For example, to keep every positive value and reject the rest:

```{code-cell} ipython3
to_keep = data >= 0  # Create a boolean mask of the values to keep
print("to_keep =", to_keep)

plt.plot(time, data, "s-", label="Original data")
plt.plot(time[to_keep], data[to_keep], "o-", label="Filtered data")
plt.legend();
```

Or, as another example, to replace any negative value by 0:

```{code-cell} ipython3
is_negative = data < 0
print("is_negative =", is_negative)

new_data = data.copy()
new_data[is_negative] = 0  

plt.plot(time, data, "s-", label="Original data")
plt.plot(time, new_data, "o-", label="New data")
plt.legend();
```

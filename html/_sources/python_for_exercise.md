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


# Exercise: Looping using **for**

In section [](python_while.md), we took some measurements in metres, that we needed to convert to millimeters.

```{code-cell}
meters = [0.329, 0.009, 0.210, 0.726, 0.686, 0.912, 0.285, 0.833, 0.334, 0.165]
```

Repeat this example, but using a `for` loop instead of a `while` loop.

```{code-cell}
:tags: [hide-cell]

# Create an empty list of the same measurements in millimeters, that we will
# fill up using a for loop.
millimeters = []

# Multiply each element of meters by 1000, and append it to the millimeters list.
for one_measurement in meters:
    millimeters.append(one_measurement * 1000)

# Done.
millimeters
```

:::{good-practice} `for` vs `while`
Note how the solution of this exercise is much clearer using `for` than `while`: we don't need to initialize an index at 0 before starting the loop, and we don't need to manually increment the index at the end of each loop. Therefore, in this case, using a `for` loop is less error-prone than using a `while` loop.

Generally:
- We use a `for` loop when we know the number of iterations in advance (in the case above, this is the length of the list);
- We use a `while` loop when we don't know in advance when the loop will stop (e.g., if the stop condition is the result of a calculation).
:::


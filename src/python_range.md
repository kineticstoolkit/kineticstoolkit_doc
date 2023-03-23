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


# Range

A range is a type of variable that specifies a series of values using a final value, an optional initial value, and an optional increment. Since a range makes an ideal counter, it is often used with `for` loops to repeat a code block a given number of time:

```{code-cell}
for i in range(5):  # Repeat the following code block 5 times
    print("The variable i is:", i)
```

In this example, the `range` function creates a sequence of values from 0 (inclusive) to 5 (exclusive), and `i` takes each of these values sequentially. It is possible to create more complex ranges, by using one of the three forms of the `range` function:

- `range(end)`
- `range(begin, end)`
- `range(begin, end, step)`

Creating ranges is very similar to usual [slicing](python_lists_slicing.md), with `begin` being inclusive and `end` being exclusive. Some examples:

```{code-cell}
# Count from 5 to 9
for i in range(5, 10):
    print("The variable i is:", i)
```

```{code-cell}
# Count from 0 to 8 by steps of 2
for i in range(0, 10, 2):
    print("The variable i is:", i)
```

```{code-cell}
# Count from 5 to 9 by steps of 2
for i in range(5, 10, 2):
    print("The variable i is:", i)
```

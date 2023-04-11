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


# Looping using **for** and **range**

A range is very similar to a [slice](python_lists_slicing.md), as it specifies a series of values using an (optional) initial value, a final value, and an (optional) increment. For example, `range(0, 9, 2)` creates a series of values from 0 (inclusive) to 9 (exclusive) by steps of 2. Thus, 0, 2, 4, 6 and 8.

A range makes an ideal counter, and it is often used with `for` loops to repeat a code block a given number of time:

```{code-cell}
for i in range(5):  # Repeat the following code block 5 times
    print("The variable i is:", i)

print("done.")
```

In this example, the `range` function creates a sequence of values from 0 (inclusive) to 5 (exclusive), and `i` takes each of these values sequentially.

Here are different syntaxes for creating ranges:

- `range(end)`
- `range(begin, end)`
- `range(begin, end, step)`

with some examples:

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

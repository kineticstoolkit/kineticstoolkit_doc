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

# Creating and indexing lists

:::{card} Summary
This section shows what is a list, how to define it and extracting values from it, using square brackets `[]`.
:::


## Creating a list

A list is, as it names implies, a list of values. It is defined using square brackets `[]` like this:

```{code-cell}
list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

A list can contain any kind of variable:

```{code-cell}
list_of_strings = [
    "first element",
    "second element",
    "third element",
    "fourth element",
    "fifth element",
    "sixth element",
    "seventh element",
    "eighth element",
    "ninth element",
    "last element",
]
```

It can even contain other lists (or any other container type such as dictionaries, tuples or sets):

```{code-cell}
list_of_lists = [
    [1, 2, 3],
    ["one", "two", "three"],
    [1, 2, 3, 4, 5],
]
```

And it can even contain different types:

```{code-cell}
list_of_anything = ["a string", 0, 4.5, (2 + 3j), False, [1, 2, 3]]
```


## Indexing a list

Every element of the list is accessible using an index. The first data is at index 0, the second at index 1, etc.

:::{note}
Zero-based addressing (first index is 0) is common in generic programming languages such as C, C++, Java, Go, PHP, Ruby, and Rust. Being a generic programming language itself, Python also uses zero-addressing. Other languages that are more aimed to mathematics, such as Matlab, R, Julia, and Mathematica, use one-based addressing (first index is 1). No convention is inherently better than another, but it may take time to adapt to zero-based addressing.
:::

We index a list using square brackets `[]`:

```{code-cell}
list_of_strings[0]
```

```{code-cell}
list_of_strings[1]
```

While you get used to zero-based addressing, this error may happen regularly:

```{code-cell}
:tags: ["raises-exception"]
# Get the last element
list_of_strings[10]
```

In this case, this error happened because while the list is indeed 10-element long, the last element is at index 9, not 10.

### Negative indexing

It is also possible to address a list from its last element, using negative indexing. The last element is directly available at index -1:

```{code-cell}
list_of_strings[-1]
```

the previous at index -2, etc.:

```{code-cell}
list_of_strings[-2]
```


:::{tip}
In the examples above, we indexed a list using a literal constant. We can also index it using a variable, in which case it needs to be an integer:
```
i = 3
list_of_strings[i]
```
:::

### Nested lists

There is no particular challenge in indexing nested lists (lists of lists). For example, to access the first element of the second list of `list_of_lists`:

```{code-cell}
list_of_lists
```

we first access the second list of `list_of_list`:

```{code-cell}
temp = list_of_lists[1]  # Second element of list_of_lists

temp
```

then we access the first element of this list:

```{code-cell}
temp[0]  # First element of the second element of list_of_lists
```

or, in one line:

```{code-cell}
list_of_lists[1][0]
```

where `list_of_lists[1]` returns the list `['one', 'two', 'three']`, and `[0]` addresses this new list.

## Getting the length of a list

The `len` function returns the length of the list (the number of elements it contains):

```{code-cell}
len(list_of_strings)
```

## Exercise 1

We measured spatial parameters of gait using an instrumented walkway, as illustrated in Figure 1. This particular instrumented walkway stores the (x, y) coordinates of each heel strike and returns these coordinates as two lists `x` and `y`. The first element of these lists corresponds to the first heel strike, the second to the second heel strike, etc.

![Instrumented walkway -width:full](_static/images/instrumented_walkway.png)

*Figure 1. Foot coordinates obtained via an instrumented walkway*

We are interested in assessing the step length, which is the distance between one heel strike and the next one by the opposite foot.

For a given participant, we recorded this `y` list:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

You are asked to write this function:

```
def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length.
    """
```

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length.
    """
    return y[step + 1] - y[step]

# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
```


## Exercise 2

You are happy with your last function, but sometimes, you obtain an IndexError:

```{code-cell}
:tags: ["raises-exception"]
calculate_step_length(y, 9)
```

**Question 1)** Find why this call produces an IndexError.

:::{toggle}
This happens because to calculate a step length, we need two heel strikes, one
and the next one. In a list of 10 heel strikes, the last element is 9; therefore,
the call above can extract the coordinates of the last heel strike, but not the
next one.

One way to avoid this error is to check that we won't index the list out of its
range, before calculating the step length.
:::

**Question 2)** Modify your function such that instead of producing this error, it simply returns 0.

:::{good-practice} Invalid data
For this example, we ask to return 0 for invalid data, but a better practice would be to return `np.nan`, which is defined in the [numpy](numpy.md) package. Simply return 0 for now since we didn't see NumPy yet.
:::

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length.
    """
    if step + 1 < len(y):
        return y[step + 1] - y[step]
    else:
        return 0.0

# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
print(calculate_step_length(y, 9))
```
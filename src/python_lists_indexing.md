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


# Indexing a list

Every element of a list is accessible using an index. The first data is at index 0, the second at index 1, etc.

:::{note}
Zero-based addressing (first index is 0) is common in generic programming languages such as C, C++, Java, Go, PHP, Ruby, and Rust. Being a generic programming language itself, Python also uses zero-addressing. Other languages that are usually more aimed to mathematics, such as Matlab, R, Julia, and Mathematica, use one-based addressing (first index is 1). No convention is inherently better than another, but for non-programmers, it may take a bit of time to adapt to zero-based addressing.
:::

We index a list using square brackets `[]`:

```{code-cell} ipython3
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

list_of_strings[0]
```

```{code-cell} ipython3
list_of_strings[1]
```

Until you get used to zero-based addressing, this error may happen regularly:

```{code-cell} ipython3
:tags: [raises-exception]

# Get the last element
list_of_strings[10]
```

In this case, this error happened because while the list is indeed 10-element long, the last element is at index 9, not 10.

## Negative indexing

We can address a list from its last element, using negative indexing. The last element is available at index -1:

```{code-cell} ipython3
list_of_strings[-1]
```

the previous at index -2, etc.:

```{code-cell} ipython3
list_of_strings[-2]
```

## Indexing using a variable

In the examples above, we indexed a list using a literal constant. We can also index it using a variable:
```{code-cell} ipython3
i = 3
list_of_strings[i]
```

In any case, the variable must be an integer. Indeed, a list element could not be halfway between two elements. This could cause some unintuitive errors, for example if the index is the result of a calculation that implies a division:


```{code-cell} ipython3
:tags: [raises-exception]
some_value = 6
list_of_strings[some_value / 2]
```

The division resulted in a float, which could not be used as an index. This code would correct this error:

```{code-cell} ipython3
some_value = 6
list_of_strings[int(some_value / 2)]
```


## Nested lists

As seen above, lists can be nested, which means that a list can contain another list. To access a specific element of the inner list, we start by indexing the outer list, then the inner list. For example, to access the first element of the second list of `list_of_lists`:

```{code-cell} ipython3
list_of_lists = [
    [1, 2, 3],
    ["one", "two", "three"],  # <--- "one"
    [1, 2, 3, 4, 5],
]
```

we first access the second list of `list_of_list`:

```{code-cell} ipython3
temp = list_of_lists[1]  # Second element of list_of_lists

temp
```

then we access the first element of this result:

```{code-cell} ipython3
temp[0]  # First element of the second element of list_of_lists
```

or, one one line:

```{code-cell} ipython3
list_of_lists[1][0]
```

where `list_of_lists[1]` returns the list `['one', 'two', 'three']`, and `[0]` addresses this new list.

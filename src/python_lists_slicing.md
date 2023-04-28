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

# Slicing lists

We already learned how to [index](python_lists_indexing.md) a list: using an integer between square brackets `[]` to extract one data from a list. Sometimes, we need to extract not only one data, but a sub-list containing multiple data. For instance, we may want to keep a certain portion of a list and discard the rest. This is done using slicing.

:::{important}
Everything on this page also applies to tuples.
:::

## Slicing syntax

The syntax for slicing is similar to indexing, the main difference being the use of a column operator `:`. To extract one element from a list, say for example the 3rd element (at index 2), we would use:

```{code-cell}
list_of_strings = [
    "string 0",
    "string 1",
    "string 2",
    "string 3",
    "string 4",
    "string 5",
    "string 6",
    "string 7",
    "string 8",
    "string 9",
]

list_of_strings[2]
```

To extract a list containing the elements at indexes 2, 3, 4, 5, and 6, we would use instead:

```{code-cell}
list_of_strings[2:7]  # From index 2 (inclusive) to index 7 (exclusive)
```

This means "return a list that includes elements from index 2 up to (**but excluding**) index 7".

:::{tip}
It can be counter-intuitive that the first index is inclusive, while the second is not. Here is a logical way to remember it:
- The first index is the first element that we want.
- The second index is the first element that we don't want.
:::

## Slicing increment

We can extract every other element, using a third integer that is the step to use in navigating the list. For instance, to extract a list containing the elements at indexes 2, 4, and 6:

```{code-cell}
# From index 2 (inclusive) to index 7 (exclusive), by steps of 2
list_of_strings[2:7:2]
```

To navigate a list backward, we would use an increment of -1. For instance, to extract a list containing elements at indexes 6, 5, 4, 3, and 2, we would use:

```{code-cell}
# From index 6 (inclusive) to index 1 (exclusive), by steps of -1
list_of_strings[6:1:-1]
```

:::{tip}
If this last example was harder to understand, let's reuse this tip.
- The first index is the first element that we want. This is index 6.
- The second index is the first element that we don't want. This is index 1.
:::

## Single bounds

Sometimes, we want to slice a list with only one bound. For example, to get every element from index 2 up to the end, we could use:

```{code-cell}
# From index 2 (inclusive) to the end of the list (exclusive)
list_of_strings[2:len(list_of_strings)]
```

There is however a simpler way: simply don't specify an "up to" index.

```{code-cell}
# From index 2 (inclusive)
list_of_strings[2:]
```

This means "return a list containing the elements beginning at index 2". Similarly:

```{code-cell}
# Up to index 8 (exclusive)
list_of_strings[:8]
```

means "return a list that containing the elements ending at index 8 (exclusive)". This also works with variable increments:

```{code-cell}
# From index 2 (inclusive), by steps of 2
list_of_strings[2::2]
```


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

# 📖 Slicing lists

:::{card} Summary
This section shows how to use slices (`[::]`) to extract multiple data from a list, in the form a subset of the original list.
:::

In the previous sections, we learned how to use square brackets `[]` to extract one data from a list. Sometimes, we dont want to extract only one data, but a sub-list containing multiple data (keeping a certain portion of a list and discarding the rest). This is done using slicing.

:::{important}
Everything on this page also applies to tuples.
:::

## 📄 Slicing syntax

The syntax for slicing is similar to indexing, the main difference being the column operator `:`. To extract one element from a list, say for example the 3rd element (at index 2), we would use:

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

## 📄 Slicing increment

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

## 📄 Single bounds

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


## 💪 Exercise 1

What would be the code to get a list identical to `list_of_strings`, but with every element reversed (the first becomes the last, the last becomes the first)?

```{code-cell} ipython3
:tags: [hide-cell]

# We start at the last element of list_of_strings.
# We can use negative indexing to get this element: -1
# Therefore, the first number of the slice (start index) is -1.

# We will go backward through the list.
# Therefore, the third number of the slice (increment) is -1.

# We go through all the list. There is no ending point.
# Therefore, there is no second number in the slice.

list_of_strings[-1::-1]
```


## 💪 Exercise 2

Let's get back to the spatial parameters of gait measured in last section. For a given participant, we recorded this `y` list:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

![Instrumented walkway -width:full](_static/images/instrumented_walkway.png)

*Figure 1. Foot coordinates obtained via an instrumented walkway*

If we know that the first element of `y` always corresponds to the right foot, write a 2-line code that separates `y` into two lists:
- `y_right`, which contains the y-coordinates of all heel strikes for the right foot
- `y_left`, which contains the y-coordinates all heel strikes for the left foot

```{code-cell} ipython3
:tags: [hide-cell]

y_right = y[0::2]
y_left = y[1::2]

# Print the results
print(f"Right foot: {y_right}")
print(f"Left foot: {y_left}")
```


## 📄 Indexing and slicing strings

We just saw how to index and slice lists. The exact same behaviour applies to strings: we can extract one or many characters from a string by slicing it:

```{code-cell} ipython3
string = "This is a sample string that we will index and slice"

# Get the first character
print(string[0])

# Get the last character
print(string[-1])

# Get the 10 first characters
print(string[:10])

# Get the 10 last characters
print(string[-10:])

# Get every other character
print(string[::2])
```


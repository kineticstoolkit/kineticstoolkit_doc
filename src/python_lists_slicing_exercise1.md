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

# 💪 Exercise 1

Here is a list:

```{code-cell} ipython3
list_of_strings = ["zero", "one", "two", "three", "four", "five"]
```

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

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

# Modifying a list while looping

In section [](python_for.md), we learned how to loop through every element of a list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for element in the_list:
    print(element)
```

Let's see if looping through the list element allows us to not only read the list but also modify it. In this example, we want to multiply every element of `the_list` by 100:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for element in the_list:
    element = element * 100

print(f"After: {the_list}")
```

Well, it didn't work, but why? Although it is not intuitive, the line `element = element * 100` in this code means:

> "Calculate `element` times 100, and put the result in a new variable that we'll call `element`".
 
In other words, at each iteration, the name `element` is overwritten and does not refer to the list anymore. Therefore, the list is not modified.

Instead of looping trough the list elements, we could loop through the list **indexes** using a range from 0 to the end of the list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

print(f"After: {the_list}")
```

It worked because at every iteration, we explicitly write to the ith element of `the_list`.

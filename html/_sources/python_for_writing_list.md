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
```

```{code-cell} ipython3
for element in the_list:
    print(element)
```

While looping through the list' elements is very practical to read the list, it could not be used to modify the list. Let's try out.

We want to multiply every element of this list by 100:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for element in the_list:
    element = element * 100

print(f"After: {the_list}")
```

Well, it didn't work, but why? Although it is not intuitive, the second line of this code means:

> "Calculate `element` times 100, and put the result in a new variable that we'll call `element`".
 
In other words, at each iteration, the name `element` is overwritten and does not refer to the list anymore. Therefore, the list is not modified.

Instead of looping trough the list elements, we could loop through the list **indexes** instead, using a range from 0 to the length of the list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i in range(len(the_list)):
    print(the_list[i])
```

While both methods seem equivalent at a first glance, in the second method we still refer to the whole list. This allows us to modify the list. Let's try our multiplication by 100 again:


```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

print(f"After: {the_list}")
```

It worked.

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

# Looping a list using **for** and **enumerate**

We learned two methods to [loop through a list](python_for_writing_list.md)): looping through the list elements, which is the simplest, and looping through the list indexes, which allows modifying the list.

The convenient `enumerate` function offers both advantages. When used to loop a list, it returns both the element and its index:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i_element, element in enumerate(the_list):
    print("The element index is", i_element)
    print("The element is", element)

```

::::{note}
This is the first time we see a function that has two return values. In reality, `enumerate` returns the tuple (`i_element`, `element`). The following code is equivalent:

```
the_list = [10, 20, 30, 40]

for one_element_tuple in enumerate(the_list):
    i_element = one_element_tuple[0]
    element = one_element_tuple[1]
    
    print("The element index is", i_element)
    print("The element is", element)

```

However, Python allows decomposing a tuple's contents into multiple variables simultaneously:

```
example_tuple = (1, 2, 3)
value1, value2, value3 = example_tuple
```

This is why the line

```
for i_element, element in enumerate(the_list):
```

works, and is much cleaner.

::::

Now, let's try [modifying a list](python_for_writing_list.md) using `enumerate`:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for i_element, element in enumerate(the_list):
    the_list[i_element] = element * 100

print(f"After: {the_list}")
```

It worked, and it is indeed a clean code.

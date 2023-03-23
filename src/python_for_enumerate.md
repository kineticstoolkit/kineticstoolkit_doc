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

# Looping though a list using `enumerate`

:::{card} Summary
This section shows how to loop through a list using `enumerate`, which allows both reading and modifying the list.
:::

## Iterating over the list vs the list indexes

There are two main ways to use `for` to iterate over a list. The first was shown previously, using `for` directly on the list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]
```

```{code-cell} ipython3
for element in the_list:
    print(element)
```

The second is to iterate over the list indexes, using a `range`:

```{code-cell} ipython3
for i in range(len(the_list)):
    print(the_list[i])
```

While both methods seem equivalent at a first glance, the first one is only useful to **read** a list. It cannot modify the elements of the list. Let's try out.

We want to multiply every element of this list by 100. Using the first method:

```{code-cell} ipython3
print(f"Before: {the_list}")

for element in the_list:
    element = element * 100

print(f"After: {the_list}")
```

Well, it didn't work, but why? Although it is not intuitive, the second line of this code means:

> "Calculate `element` times 100, and put the result in a new variable that we'll call `element`".
 
In other words, the name `element` is overwritten and do not refer to the list anymore. Therefore, the list is not modified.

Now, using the second method:

```{code-cell} ipython3
print(f"Before: {the_list}")

for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

print(f"After: {the_list}")
```

In this case, it worked well because we are explicitly asking to update the element `i` of the list.

## Enumerate

Since both iteration methods of previous section have advantages (the first being simpler, the second being more powerful), we can use both at the same time using the convenient `enumerate` function, that returns both the element and its index:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i_element, element in enumerate(the_list):
    print("The element index is", i_element)
    print("The element is", element)

```

:::{note}
This is the first time we see a function that returns two arguments. In reality, `enumerate` returns only one variable, which is a tuple (`i_element`, `element`). The following code would be perfectly fine:

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

works, and is much clearer.

:::

Now, let's try the previous example with `enumerate`:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]
print(f"Before: {the_list}")

for i_element, element in enumerate(the_list):
    the_list[i_element] = element * 100

print(f"After: {the_list}")
```

It worked.

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

# 📖 Looping though a list using `enumerate`

:::{card} Summary
This section shows how to avoid pitfalls when writing into a list that we are looping through. It also introduces the `enumerate` function that gives access to both an element and its index at the same time.
:::

## 📄 Iterating over a list, or over the list indexes

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

While both methods seem equivalent at a first glance, the first one is only useful to **read** a list, it cannot modify the elements of the list. Let's try out.

We want to multiply every element of this list by 100. Using the first method:

```{code-cell} ipython3
for element in the_list:
    element = element * 100

the_list
```

...well, it didn't work, but why? This is indeed very subtle. On the second line of this code, what we ask is: "calculate `element` times 100, and put the result in a variable that we'll call `element`. In other words, the name `element` is overwritten and do not refer to the list anymore, and thus the list is not modified.

Now, using the second method:

```{code-cell} ipython3
for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

the_list
```

In this case, it worked well because we are explicitly asking to update the element `i` of the list.

## 📄 Enumerate

Since both iteration methods of previous section have advantages (the first being simpler, the second being more powerful), we can use both at the same time using the convenient `enumerate` function, that returns both the element and its index:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i_element, element in enumerate(the_list):
    print("The element index is", i_element)
    print("The element is", element)

```

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
This section shows how to avoid pitfalls when writing into a list that we are looping through. It also introduces the `enumerate` function that gives access to an element and its index at the same time.
:::

## Iterating over a list, or over the list indexes

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

While both methods seem equivalent at a first glance, the second one is only useful to **read** a list, it cannot modify it. Let's try out.

We want to multiply every element of this list by 100. Using the first method:

```{code-cell} ipython3
for element in the_list:
    element = element * 100

the_list
```

...well, it didn't work, but why? On the second line of this code, what we ask is: "calculate `element` times 100, and put the result in a variable that we'll call `element`. In other words, at each iteration, it creates a new variable called `element` and assigns the result to it. But as we continue to the next iteration, the variable `element` is overwritten with the next list item. The list itself was never modified.

Now, using the second method:

```{code-cell} ipython3
for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

the_list
```

In this case, it worked well because we are explicitly asking to update the element `i` of the list. We are not creating a new `element` variable at each iteration.

## Enumerate

Since both iteration methods of previous section have advantages (the first being simpler, the second being more powerful), we can use both at the same time using the convenient `enumerate` function, that returns both the element and the element index:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i_element, element in enumerate(the_list):
    print("The element index is", i_element)
    print("The element is", element)

```

## Do not change the length of a list while looping through it

This section's title says it all. In any case, it is always a bad idea to decrease or increase the length of a list while we loop through it. Here is a bad example that demonstrates why.

In this bad example, we want to remove every element of a list that is not an integer.

```{code-cell} ipython3
:tags: [raises-exception]
some_list = [1, 2, 'three', 'four', 'five', 6, 7]

for i in range(len(some_list)):  # Loop through all indexes of this list
    
    item = some_list[i]
    
    if isinstance(item, int):
        print(f"Iteration #{i}: Item {item} is an integer. Do nothing.")
    else:
        print(f"Iteration #{i}: Item {item} is not an integer. Delete it.")
        some_list.pop(i)
        
some_list
```

The length of the list is 7, and therefore the `for` loop will increment i from 0 to 6. However, since we sometimes remove elements from the list, then at some point, it does not contain 7 elements anymore and we get an out of range error.

To perform this operation correctly, we must not modify the list that we loop through. To this effect, we progressively build a second list that will contain the end result.

```{code-cell} ipython3
some_list = [1, 2, 'three', 'four', 'five', 6, 7]
new_list = []

for item in some_list:
    
    if isinstance(item, int):
        print(f"Item {item} is an integer. Add it to a new list.")
        new_list.append(item)
        
new_list
```

:::{margin}
#todo Decide if we show list comprehension with `for` and `if`, and if this is the case, provide some link to a one-liner that does the same code.
:::

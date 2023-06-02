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

# Looping using **for**

We already learned to use [while](python_while.md) to repeat a code block as long as a condition is true. Whereas the `while` statement is very powerful and sufficient for any looping, it is sometimes clearer to use the `for` statement instead.

The `for` statement means: "repeat this code block for each element of this variable".

This means that we can easily iterate through each element of a list:

```
for variable_name in the_list:
    instruction1
    instruction2
    instruction3
    etc.
```

For example:

```{code-cell}
a_list = [0, 1, 2, 'three', 'four']

for item in a_list:
    print("The current item is:", item)

print("done.")
```

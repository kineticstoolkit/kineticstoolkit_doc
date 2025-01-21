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

# Conditional code

Now that we know how to make comparisons, we can control the flow of the program as a result of these comparisons, using `if`:

```
if condition:
    perform_task1()
    perform_task2()
    perform_task3()
```

The `if` checks if a condition is met. The code block that follows the `if` statement is executed only if the condition evaluates to `True`.

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

```

This code did nothing, because the condition evaluated to `False`.

Using the `else` keyword, it is possible to execute one action if the condition is `True` and another action if the condition is `False`:

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

else:
    print("Nothing to see here.")

```

It is also possible to evaluate different conditions in a same `if` series, using `elif`, which stands for "else if":

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

elif my_score == WORLD_RECORD:
    print("I matched the world record!")

else:
    print("Nothing to see here.")

```

There may be more than one `elif` in a same series of comparisons:

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

elif my_score == WORLD_RECORD:
    print("I matched the world record!")

elif my_score > WORLD_RECORD - 5:
    print("I am near the world record!")

else:
    print("Nothing to see here.")

```

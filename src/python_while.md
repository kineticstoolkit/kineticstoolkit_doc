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

# Looping using `while`

The `while` instruction repeats a code block as long as a condition is true. Its syntax is:

```
while condition:
    instruction1()
    instruction2()
    instruction3()
    ...
```

where `condition` is a [boolean variable](python_conditions.md). Each repetition of a code block is called an *iteration*.

Here is an example with five iterations of a code block:

```{code-cell}
i = 0

while i < 5:
    print(f"Now, the variable i is {i}.")
    i += 1
```

In the following example, we made some measurements in metres that we stored into a list. We want to convert this list to another list where the measurements are in millimetres instead:

```{code-cell}
# Measurements in meters:
meters = [0.329, 0.009, 0.210, 0.726, 0.686, 0.912, 0.285, 0.833, 0.334, 0.165]

# Create an empty list of the same measurements in millimeters, that we will
# fill up using a while loop.
millimeters = []

# Multiply each element of meters by 1000, and append it to the millimeters list.
i = 0
while i < len(meters):
    millimeters.append(meters[i] * 1000)
    i += 1

# Done.
millimeters
```

:::{good-practice} Looping
While this example works perfectly well and is indeed a correct demonstration of how `while` works, we will see in the next sections that for this specific example, other methods such as using [for](python_for.md) or [NumPy](numpy.md) would be less error-prone and faster.
:::

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

:::{card} Summary
This section shows how to repeat a code block using the `while` statement.
:::

## Syntax

The `while` instruction repeats a code block as long as a condition is true. Its syntax is:

```
while condition:
    instruction1()
    instruction2()
    isntruction3()
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

Here is a more practical example, where we convert a list of measurements from meters to mm:

```{code-cell}
# We have some measurements in meters:
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
While this example works perfectly well and is indeed a correct demonstration of how `while` works, we will see in the next sections that for this specific example, other methods sur as `for`, or even better using `numpy`, would be less error-prone and faster.
:::

## Exercise 1

We return to the example of the instrumented walkway. We recorded the following positions of heel strike, first for the right heel, second for the left heel, third for the right heel, etc.:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

![Instrumented walkway -width:full](_static/images/instrumented_walkway.png)

*Figure 1. Foot coordinates obtained via an instrumented walkway*

Write a program that creates a list named `step_lengths`, that contains the length of every step. The first step length would be `y[1] - y[0]`, the second would be `y[2] - y[1]`, etc. In this specific example, we recorded nine steps, but your code must work on any number of steps.

```{code-cell}
:tags: [hide-cell]

# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
i = 0
while i < n_steps:
    step_lengths.append(y[i + 1] - y[i])
    i += 1

# Done!
step_lengths
```

## Exercise 2

A therapist measures a patient's maximal shoulder flexion several times. Write a program that creates a list of all these measurements based on user input, following this example:

:::{admonition} Example of program output
```none
Enter max shoulder flexion (deg), or Enter to stop: <User enters 119>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 124>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 123>
Enter max shoulder flexion (deg), or Enter to stop: <User presses Enter>
Max shoulder flexion: [119.0, 124.0, 123.0]
```
:::

:::{tip}
The [`input`](python_strings.md) function returns an empty string `""` when the user simply presses Enter without entering a value.
:::

:::{toggle}
```
# Initialize an empty list of measurements
measurements = []

# Initialize a boolean variable that controls if we need to quit the loop
continue_asking = True

# Ask the values
while continue_asking:
    str_value = input("Enter max shoulder flexion (deg), or Enter to stop: ")
    if str_value == "":
        continue_asking = False
    else:
        measurements.append(float(str_value))

# Print the result
print("Max shoulder flexion:", measurements)
```
:::

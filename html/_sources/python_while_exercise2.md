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


# Exercise: Looping using **while** 2

A therapist measures a patient's maximal shoulder flexion angle several times. Write a program that creates a list of all these measurements based on [user input](python_strings_input.md), following this example:

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
The [input](python_strings_input.md) function returns an empty string `""` when the user simply presses Enter without entering a value.
:::

:::{toggle}
```
# Initialize an empty list of measurements
measurements = []

# Initialize a boolean variable that controls when we need to quit the loop
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

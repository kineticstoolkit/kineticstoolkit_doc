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


# Exercise: Looping using **for** and **range** 1

A therapist measures a patient's maximal shoulder flexion angle three times. Write a program that creates a list of these three measurements based on user input, following this example:

:::{admonition} Example of program output
```none
Enter max shoulder flexion (deg) [measurement 1]: <User enters 119>
Enter max shoulder flexion (deg) [measurement 2]: <User enters 124>
Enter max shoulder flexion (deg) [measurement 3]: <User enters 123>
Max shoulder flexion: [119.0, 124.0, 123.0]
```
:::

:::{toggle}
```
# Initialize an empty list of measurements
measurements = []

# Ask the values
for i in range(3):
    str_value = input(
        f"Enter max shoulder flexion (deg) [measurement {i}]: "
    )
    measurements.append(float(str_value))

# Print the result
print("Max shoulder flexion:", measurements)
```
:::

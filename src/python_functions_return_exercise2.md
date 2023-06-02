---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Function return values 2

Based on the function `print_info` that you created a [previous example](python_functions_arguments_exercise.md), create a new function `format_info` that, instead of printing the information, creates a string and returns it, so that:

```
print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```
    
prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============

Instead of calculating the BMI manually in the function, use a call to the `calculate_bmi` function that you wrote [previously](python_functions_return_exercise1.md).

:::{tip}
You may want to return section [](python_strings.md) for a refresh on how to include [line breaks in strings](python_strings_long_strings.md), how to create [long strings ](python_strings_long_strings.md), and how to [add variables in strings](python_strings_fstrings.md).
:::

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_bmi(height, weight):
    return weight / (height ** 2)


def format_info(i_participant, first_name, last_name, age, height, weight):

    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {calculate_bmi(height, weight):.2f}\n"
        "============="
    )
    return output


print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```

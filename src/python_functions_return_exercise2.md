---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# 💪 Exercise 2

Based on the function `print_info` that you created in a previous example, create a new function `format_info` that, instead of printing the information, creates an equivalent string and returns it, so that:

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

Instead of calculating the BMI manually in the function, use a call to the `calculate_bmi` function that you just wrote in the previous example.

:::{tip}
You may want to return to the section on [strings](python_strings.md) for a refresh on how to create long strings, f-strings, and how to add line breaks in strings.
:::

```{code-cell}
:tags: [hide-cell]

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

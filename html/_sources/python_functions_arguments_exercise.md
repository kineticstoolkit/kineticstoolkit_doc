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

# Exercise: Function arguments

Create a function named `print_info()` that, when it is called using:

```
print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```
    
prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============

Then try your function. Please use clear names for your function's arguments.

:::{note}
The body-mass index (BMI) is calculated using $\text{weight}/\text{height}^2$.
:::

```{code-cell}
:tags: [hide-cell]

def print_info(i_participant, first_name, last_name, age, height, weight):

    print("=============")
    print(f"Participant {i_participant}: {first_name} {last_name}")
    print(f"{age} years old")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {weight / (height ** 2):.2f}")
    print("=============")

print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```

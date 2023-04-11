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

# 💪 Function return values (1)

Write a function called `calculate_bmi` that takes a person's height and weight as arguments, and that returns the body-mass index, knowing that $\text{BMI} = \text{weight}/\text{height}^2$.

```{code-cell}
:tags: [hide-cell]

def calculate_bmi(height, weight):
    return weight / (height ** 2)


# Let's test the function:
print(calculate_bmi(1.5, 50.2))
```

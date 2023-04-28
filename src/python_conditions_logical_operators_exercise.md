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

# Exercise: Logical operators

Write a short code that checks the value of two integers named `dice1` and `dice2`, and that prints "You got double-six!", "You got one six!" or "You got no six." according to the dice values.

```{code-cell} ipython3
:tags: [hide-cell]

# Assign some values to dice1 and dice2
dice1 = 6
dice2 = 4

if (dice1 == 6) and (dice2 == 6):
    print("You got double-six!")
elif (dice1 == 6) or (dice2 == 6):
    print("You got one six!")
else:
    print("You got no six.")
```

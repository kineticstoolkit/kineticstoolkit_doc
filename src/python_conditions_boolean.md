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

# Boolean and comparisons

Comparisons are performed using the following operators:

| Operator | Meaning          |
| --------:|:---------------- |
|     `==` | Equal            |
|     `!=` | Unequal          |
|      `>` | Strictly greater |
|     `>=` | Greater or equal |
|      `<` | Strictly lower   |
|     `<=` | Lower or equal   |

For example, the following comparison gives `True`:

```{code-cell}
10 > 5
```

while this one gives `False`:

```{code-cell}
10 == 5
```

The result of a comparison is always a boolean variable. We already know the following types of variable: `string`, `int`, `float` and `complex`. Boolean variables, `bool`, are the simplest: they can be only either `True` or `False`.

Obviously, comparing a constant with another constant has little sense. However, comparing variables with constants, or variables with other variables, is very common and helpful:

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
my_score > WORLD_RECORD
```

:::{important}
You may note that the equality comparison is a double-equal `==` instead of a single one `=`. This is to avoid confusion between a comparison:

```
a == 5
```
which returns `True` or `False`

and an assignment:

```
a = 5
```
which assigns the value of 5 to variable `a`.
:::

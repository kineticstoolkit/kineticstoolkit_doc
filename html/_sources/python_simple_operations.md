---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Simple operations

{{ stub }}

## Addition, subtraction

```{code-cell}
print(4 + 3)
```

```{code-cell}
print(4 - 3)
```

:::{tip} Good practice
Put spaces between operators (PEP8)
:::

## Using variables

```{code-cell}
a = 4
b = 3
print(a + b)
```

```{code-cell}
c = a + b
print(c)
```

```{code-cell}
c = c + 1
print(c)
````

:::{admonition} Good practice
Use clear names for variables (PEP8) (distance, duration, speed).
:::

:::{admonition} Good practice
Use lowercase and underscores for variable names (PEP8).
:::

## Numbers: int, float

```{code-cell}
a = 1
print(a)
print(type(a))
```

Note that the `print` function can take several inputs:
```{code-cell}
a = 1; print(a, type(a))
a = 0.5; print(a, type(a))
a = 1.0; print(a, type(a))
```

## Inputing variables

```
a = input()
a = input("Enter a number: ")
```

We already saw a string in the Hello World example, we will see it in more details in the [python_strings](python_strings.md) section.

```
a = float(input("Enter a number: "))
```

## Multiplication, division

```{code-cell}
a = 4 * 3
print(a, type(a))

a = 4 / 3
print(a, type(a))

a = 4 + 3
print(a, type(a))
```

## Exponentiation and root

```{code-cell}
a = 4 ** 2
print(a, type(a))

a = 4 ** (1 / 2)
print(a, type(a))
```

## Integration exercise

:::{note}
Keep your exercices, since they will be continuously reused in the following exercices.
:::

### Speed calculation

#todo Use realistic values

Given the following variables:
  - time_gate1 = 0.0
  - time_gate2 = 5.4
  - distance_gates12 = 50.0

Write a program that prints the mean velocity of the sprinter between gates 1 and 2.

#todo Make a foldable block with answers.

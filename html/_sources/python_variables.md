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

# Variables

Variables are fundamental in programming. A variable is a space in memory to store a value. For example, we could create two variables, `a` and `b`, that both store a different number:

```{code-cell} ipython3
a = 4
b = 3
```

From there, we can refer to the value of a variable by referring to its name:

```{code-cell} ipython3
a + 1
```

```{code-cell} ipython3
a + b
```

We can even assign the result of an operation to a new variable:

```{code-cell} ipython3
c = a + b

c
```

:::{note}
Contrarily to other programming languages such as C/C++, we do not need to declare a variable before assigning a value to it. The variable is created as we assign its value.
:::

Keep in mind that in the last example, we did not instruct Python that `c` must always be equal to `a + b`. This is not how a sequential programming language such as Python works. Instead, we instructed Python, at this very instant, to calculate the result of `a + b` and to store it in a new variable named `c`. This sequential nature allows is illustrated in this example:

```{code-cell} ipython3
c = c + 1

c
```

where we instructed Python to calculate the result of `c + 1` and to store it in the variable `c`.

:::{tip}
The exemple above can be written in a shorter form using the increment `+=` operator. This notation is very common and may help avoid typographic errors in more complex statements.

These shorthands exist for every arithmetical operation:

```
a += b      # equivalent to a = a + b
a -= b      # equivalent to a = a - b
a *= b      # equivalent to a = a * b
a /= b      # equivalent to a = a / b
```
:::


:::{good-practice} Variable names
It is generally a good idea to use words rather than letters for variable names. For example, this code:

```
velocity = distance / duration
```

is clearer than:

```
v = d / t
```

In addition, the [standard Python coding style](https://pep8.org/) recommends to use all lower case for variables, and to generally separate multiple words by underscores (`_`), e.g., `power`, `mean_power`, `peak_power`.

:::

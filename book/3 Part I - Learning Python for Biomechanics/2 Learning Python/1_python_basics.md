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


# Python basics

This section covers the very basics of Python: how to perform arithmetic operations between variables and constants, how to print information on the console, and how to document code using comments.


## Arithmetic operations

Any arithmetic operation is performed simply by writing its equation. For example, the most common arithmetic operators are `+`, `-`, `*`, `/` and `**`. We use parentheses `()` to indicate operation priority.

```python
# Addition

4 + 3

# Subtraction

4 - 3

# Multiplication

4 * 3

# Division

4 / 3

# Exponent

4 ** 2

# Root: we can exponentiate to the inverse. For example, to calculate
# the square root of a number, we would write:

4 ** (1 / 2)
```


## 💪 Exercise 1

Type one line in the console that performs this operation:

$$\left( \frac{3+5}{6-4} \right)^2$$

```{code-cell}
:tags: [hide-cell]
((3 + 5) / (6 - 4)) ** 2
```


## Printing to the console

To print anything to the console, we use the `print` function:

```{code-cell} ipython3
print(1 + 2)
print(3 + 4)
```

The `print` function works with any content, be it numbers or words:

```{code-cell} ipython3
print("Hello world")
```


:::{important}
Python is case-sensitive. This means that `a` is not the same as `A`. Consequently,

```
Print("Hello world")
```

or

```
PRINT("Hello world")
```

would result in an error because neither `Print` or `PRINT` exists. However,

```
print("Hello world")
```

works.
:::

## Comments

Programs with only a few lines of code are generally easy to understand. As they grow in complexity, we need to document them, usually with comments.

Any text that follows `#` corresponds to a comment, and it is not executed by Python. Usually, we use comments to explain the objective of a section of code.

These codes are completely equivalent:

**Without comments**

```{code-cell}
print("Here is a calculation")
print(10 + 5)
```


**With comments**

```{code-cell}
# Demonstrate comments

print("Here is a calculation")  # Print some text
print(10 + 5)  # Print the result of an addition
```


## Variables

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
Unlike other programming languages such as C/C++, we do not need to declare a variable before assigning a value to it. The variable is created as we assign its value.
:::

Keep in mind that in the last example, we did not instruct Python that `c` must always be equal to `a + b`. This is not how a sequential programming language such as Python works. Instead, we instructed Python, at this very instant, to calculate the result of `a + b` and to store it in a new variable named `c`. This sequential nature is illustrated in this example:

```{code-cell} ipython3
c = c + 1

c
```

where we instructed Python to calculate the result of `c + 1` and to store it in the variable `c`.

:::{tip}
The example above can be written in a shorter form using the increment `+=` operator. This notation is very common and may help avoid typographic errors in more complex statements.

These shorthands exist for every arithmetical operation:

```
a += b      # equivalent to a = a + b
a -= b      # equivalent to a = a - b
a *= b      # equivalent to a = a * b
a /= b      # equivalent to a = a / b
```
:::


:::{tip} Variable names
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


## 💪 Exercise 2

A sprinter runs through two timing gates spaced by 50 m as shown in {numref}`fig_exercise_timing_gates`. Each timing gate records the time (in seconds) when the sprinter passes through it.

```{figure}
:label: fig_exercise_timing_gates
:width: 4in
![](_static/images/fig_exercise_timing_gates.png)

Two timing gates separated by 50 meters.
```

Given the following program:

```
time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters
```

Continue this program so that it calculates and prints the mean velocity of the sprinter between gates 1 and 2.

```{code-cell} ipython3
:tags: [hide-cell]

time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters

print(distance_gates12 / (time_gate2 - time_gate1))
```


## 💪 Exercise 3

A sprinter runs a given distance $x$ to the East, then a given distance $y$ to the North (in km), as pictured in {numref}`fig_exercise_pythagore`. Use the Pythagorean theorem to complete the following program so that it prints the distance $d$ between her starting point and her final destination.

```{figure}
:label: fig_exercise_pythagore
:width: 4in
![](_static/images/fig_exercise_pythagore.png)

Distance between the starting point and final destination.
```

```
x = 2.5  # in meters
y = 0.7  # in meters
```

```{code-cell} ipython3
:tags: [hide-cell]

x = 2.5  # in meters
y = 0.7  # in meters
d = (x**2 + y**2) ** (1 / 2)

print(d)
```

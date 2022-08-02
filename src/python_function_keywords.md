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

# 🚧 Keyword arguments

{{stub}}

Up to now, we only used list of arguments: each value from the function call is assigned to a function argument by its order. It is also possible to call functions with keyword arguments. This has the advantage of being still clearer in the code that calls the function. For example, this function:

```{code-cell}
def print_full_name(first_name, last_name):
    print(f"{first_name} {last_name}")
```

can be called either using a list of arguments:

```{code-cell}
print_full_name("Catherina", "Smith")
```

or keyword arguments, in either order:

```{code-cell}
print_full_name(first_name="Catherina", last_name="Smith")
```

```{code-cell}
print_full_name(last_name="Smith", first_name="Catherina")
```

:::{good-practice} No space between keyword-arguments and value
Note the absence of space between the argument name and its value. Although it would also work and be perfectly valid with spaces, this form is a common coding style that is defined in PEP8. 
:::

## Long lines of arguments

When a function has a lot of arguments, and that we assign these arguments using keywords, the resulting lines may become very long. It is possible to write a Python instruction on multiple lines. As long as a parenthesis is open, Python considers that the function is not terminated, and continues reading the next lines until the last parenthesis is closed.

For instance, the code you wrote in the last exercise could be called using keywords, on multiple lines, using:

```{code-cell}
print(
    format_info(
        i_participant=1,
        first_name="Catherina",
        last_name="Smith",
        age=20,
        height=1.5,
        weight=50.2,
    )
)
```

:::{tip}
This is the same concept that we saw in the [Strings section](python_strings.md), where long strings are created using multiple strings delimited by parentheses.
:::

- Default values: def print_addition(a, b, c=0): print(a + b + c);
    - print_addition(2, 4)
    - print_addition(2, 4, 6)
    - print_addition(a=2, b=4, c=6)
- Returning values
    - def print_addition(a, b, c=0): total = a + b + c; return total;
    - print(print_addition(2, 4, 6))
- Good practice in naming functions: active form and lowercase with underscores (PEP8).
- Integration exercise: speed calculation
    - Program a function that will make this code work as expected:
    - print(calculate_speed(0.0, 5.4, 50.0))
    - print(calculate_speed(time_gate1=0.0, time_gate2=5.4, distances_gates12=50.0))
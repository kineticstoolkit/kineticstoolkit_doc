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

# 🚧 Good practices with functions

We theoretically saw enough contents on functions to be able to follow with other concepts. However, although the solutions to the previous exercises do work, they are far from being clear.

For example, in the suggested answser for the function `format_info()` (exercise above):

- The aim of the function is not defined
- The list and order of the required arguments is not described
- The return value is not described

As consequence, using this function is very prone to error. Keep in mind that code is wrote once by often one programmer, but read many times by often many other programmers. An undocumented function is usually clear to the programmer while it is being written; but will it still be clear when read by another person, or even by the same programmer months later?

Before switching to other programming concept, it is important to know how to well define and document your functions. This is not just good practice, this is very important to avoid errors that may generate bad results and therefore bad conclusions.

## Argument names

The biggest issue with the function from the last exercise is the name of its arguments, that ranges from `var1` to `var6` instead of being meaningful. In reality, it is possible to give any name to these arguments. Appreciate how both the signature and implementation of the function are clearer:

```{code-cell}
def format_info(i_participant, first_name, last_name, age, height, weight):

    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {weight / (height ** 2)}\n"
        "============="
    )
    return output


print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```

:::{tip} Arguments vs Parameters
In the different references found on the web, we often see both the terms "argument" and "parameter" for function inputs. Both terms are equivalent and will be referred by both words from now on.
:::

## Docstring

The docstring is literally a **string** that **doc**uments your function. While any code without a docstring will stay run, it is almost mandatory in any code other than very simple scripts, because this is what really tells what the function does, what its parameters are, and what it returns. Docstrings usually use triple-double-quote strings, and are placed just below the function signature. A good docstring for the last function would be:

```{code-cell}
def format_info(i_participant, first_name, last_name, age, height, weight):
    """
    Format the provided information into a human-readable string.

    Parameters
    ----------
    i_participant (int)
        Identifier for the participant
    first_name (str)
        First name (given name) of the participant
    last_name (str)
        Last name (surname) of the participant
    age (float)
        Age of the participant, in years
    height (float)
        Height of the participant, in meters
    weight (float)
        Weight of the participant, in kg

    Returns
    -------
    str
        A human-readable string based on the provided information.

    """
    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {weight / (height ** 2)}\n"
        "============="
    )
    return output
```

As you notice, we now have more lines of documentation than lines of code. This is not unusual, and this is not a bad practice. After all, a well-documented, simple code is much better than an undocumented, complex code!

You do not need to search your function's code to read its docstring. As soon as the function is defined, its docstring becomes available using the diverses methods to consult help. Try executing the last function definition, then:

1. Type `format_info` in Spyder's help browser. Our docstring appears, all well-formatted:

![Spyder help -width:wider](_static/images/python_function_spyder_help.png)

2. Type `format_info?` in the console. The signature and docstring appear:

```{code-cell}
format_info?
```

## Typing

#todo 

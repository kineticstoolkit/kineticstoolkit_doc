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

# Docstrings

We theoretically know enough on functions to follow on with other concepts. However, although the solutions to the previous exercises do work, they could be much more documented. Keep in mind that code is wrote once by often one programmer, but is read many times after, by many users and other programmers. An undocumented function is usually clear to the programmer while it is being written; but will it still be clear when read by another person, or even by the same programmer months later?

Docstrings may be the best thing to document functions and reduce the risk of long-term error.

A docstring is literally a **string** that **doc**uments a function. While being facultative, it is almost mandatory in any code other than very simple scripts, because this is what really tells what the function does, what its parameters are, and what it returns. A standard docstrings is a triple-quote string placed just below the function signature. A good docstring for the `format_info` function of the last section would be:

```{code-cell} ipython3
def format_info(i_participant, first_name, last_name, age, height, weight):
    """
    Format the provided information into a human-readable string.

    Parameters
    ----------
    i_participant : int
        Identifier for the participant
    first_name : str
        First name (given name) of the participant
    last_name : str
        Last name (surname) of the participant
    age : float
        Age of the participant, in years
    height : float
        Height of the participant, in meters
    weight : float
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
        f"BMI: {weight / (height ** 2):.2f}\n"
        "============="
    )
    return output
```

:::{note}
The style used for this docstring is [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html). There is no real need to follow this specific style over another one, but since it is used by most major Python packages in numerical analysis (NumPy, Pandas, Matplotlib, SciPy), then we chose to also follow this style in Kinetics Toolkit and in this book.
:::

As you notice, we now have more lines of documentation than lines of code. This is not unusual, and this is not a bad practice. After all, a well-documented, simple code is much better than an undocumented, complex code!

## Consulting docstrings

Since they are so ubiquitous, docstrings can be read without having to open the function's source code. Try executing the last function definition, then:

1. Type `format_info` in Spyder's help browser. The docstring appears, all well-formatted:

![Spyder help -width:wider](_static/images/python_function_spyder_help.png)

2. Or type `help(format_info)` in the console:

```{code-cell} ipython3
help(format_info)
```

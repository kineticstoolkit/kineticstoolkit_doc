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

# Docstrings

We theoretically know enough on functions to follow on with other concepts. However, although the solutions to the previous exercises do work, they could be much more documented.

:::{tip}
Keep in mind that code is wrote once, often by only one programmer, but it is read many times after, often by other people. An undocumented function is usually clear to the programmer while it is being written, but will it be months later?
:::

Docstrings are the most important way to document functions. A docstring is literally a **string** that **doc**uments a function. While being facultative, it is almost mandatory in any code other than very simple scripts. A standard docstrings is a [triple-quote string](python_strings_triple_quotes.md) placed just below the function signature. Minimally, a docstring clearly indicates:

1. What the function does, on one single line.
2. What are the types and contents of every expected parameter.
3. What are the type and contents of the return value, if any.

Here is what a good docstring looks like:

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
The style used for this docstring is [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html). There is no requirement to follow this specific style over another one, but since it is used by most major Python packages in numerical analysis (NumPy, Pandas, Matplotlib, SciPy), then the Kinetics Toolkit package also follows this style.
:::

As you notice in the example above, there is more lines of documentation than lines of code. This is not unusual, and this is not a bad practice. After all, a well-documented, simple code is much better than an undocumented, complex code!

Since they are so ubiquitous, docstrings can be read without having to open the function's source code. Try executing the last function definition, then:

- Type `format_info` in Spyder's help browser. The docstring appears, all well-formatted, as pictured in {numref}`fig_python_function_spyder_help`.

```{figure-md} fig_python_function_spyder_help
:width: 5in
![](_static/images/fig_python_function_spyder_help.png)

Reading a docstring in Spyder's help pane.
```

- Or type `help(format_info)` in the console:

```{code-cell} ipython3
help(format_info)
```

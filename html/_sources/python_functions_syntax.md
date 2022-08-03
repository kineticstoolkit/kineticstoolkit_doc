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

# 🚧 Function syntax

In Python, functions are defined using this syntax:

```
def function_name(arg1, arg2, ...):
    # operation1
    # operation2
    # operation3
    # etc.
    return the_result
```

This reads as "Define the function `function_name`, which takes `arg1`, `arg2`, ... as input. This function will process these inputs and return `the_result` as an output.

Here is a very basic example of a function that prints its input values and their sum:

```{code-cell}
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

Once a function is defined (using the `def` keyword), it can then be called as many times as we want:

```{code-cell}
print_sum(1, 4)
print_sum(3, 10)
```

## Signature and implementation

Note that the function definition (the line that starts with `def`) is terminated by a colon (`:`). This line is the **function signature**. It tells how to use the function. We now know that the function is called `print_sum`, that it takes two arguments, and that it returns nothing.

A colon signifies that the following lines will be a code block, which is simply a series of lines that belong to a same group. In the case of a function, this code block is the **function implementation**. This is the lines to be executed when the function is called.

In Python, code blocks are delimited by their indentation. Every line of a code block must be indented with the same number of spaces.

:::{tip}
Since indentation is so important in Python, practically all Python editors include keyboard shortcuts to indent or outdent code blocks. Check in the settings of your editor to learn or change these shortcut following your tastes.
:::

:::{good-practice} Number of spaces
Try to be coherent with the number of space you use for defining code blocks. Although you can select either tabs or spaces, and the number of spaces you want, a common practice is to always use four spaces for indents, which is the default in Spyder.
:::

:::{exercise} Printing information
Using the function `print_sum()` as an example, create a function `print_info()` which, when it is called using:

```
print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```
    
then it prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============
    
Note that the body-mass index (BMI) is calculated using $\text{weight}/\text{height}^2$.

:::

:::{margin}
#todo Add float formatting in f-strings
:::

```{code-cell}
:tags: [hide-cell]

def print_info(arg1, arg2, arg3, arg4, arg5, arg6):
    print("=============")
    print(f"Participant {arg1}: {arg2} {arg3}")
    print(f"{arg4} years old")
    print(f"Height: {arg5} m")
    print(f"Weight: {arg6} kg")
    print(f"BMI: {arg6 / (arg5 ** 2)}")
    print("=============")


print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```

## Return values

Most functions do not print results in the console. Instead, they calculate something and return the result as an output. This is done using the `return` statement. Although the following function is not that useful, it illustrates how it works:

```{code-cell}
def calculate_sum(arg1, arg2):
    result = arg1 + arg2
    return result
```

If a code line contains a function call, the function is executed and its return value replaces the function call. These examples better explain this behaviour:

### Example 1

```{code-cell}
print(calculate_sum(2, 6))
```

The function `calculate_sum()` is called with arguments 2 and 6. It executes and returns 8. The `print()` function therefore prints 8.

### Example 2

```{code-cell}
print(calculate_sum(calculate_sum(2, 6), 5))
```

The inner function call calls `calculate_sum()` with arguments 2 and 6. The function executes and returns 8. Then, the outer function call calls `calculate_sum()` with arguments 8 and 5. The function executes again and this time returns 13. The `print()` function therefore prints 13.

:::{exercise} Printing information (cont'd)
Based on the function `print_sum()` that you created in the last example, create a function `format_info()` which does not print the information, but instead creates an equivalent string and returns it, so that:

```
print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```
    
prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============

Tip: you may want to return to the section on [strings](python_strings.md) for a refresh on how to create long strings, and how to add line breaks in strings.

:::

```{code-cell}
:tags: [hide-cell]

def format_info(arg1, arg2, arg3, arg4, arg5, arg6):

    output = (
        "=============\n"
        f"Participant {arg1}: {arg2} {arg3}\n"
        f"{arg4} years old\n"
        f"Height: {arg5} m\n"
        f"Weight: {arg6} kg\n"
        f"BMI: {arg6 / (arg5 ** 2)}\n"
        "============="
    )
    return output


print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))

```

:::{note}
Please note that although the solutions to these exercises do work, they are far from being clear and do not respect good practices in programming. Be sure to read the [next section](python_functions_good_practice.md) to know how to write **good** code, that works both now **and** in the future.
:::

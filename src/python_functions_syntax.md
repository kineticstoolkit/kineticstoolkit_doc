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

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Function syntax

Functions are defined using this syntax:

```
def function_name(arg1, arg2):
    operation1()
    operation2()
    operation3()
    return the_result
```

This reads as "Define the function `function_name`, which takes `arg1`, `arg2` as inputs. This function will process these inputs and return `the_result` as an output.

:::{note}
- The inputs of a functions are called **arguments** or **parameters**. Both terms are used interchangeably.
- The output of a function is called a **return value**.
:::

:::{note}
There is no minimal or maximal limit in the number of arguments. We could very well have a function with five arguments:

```
def function_name(arg1, arg2, arg3, arg4, arg5):
```
:::

Here is an example of a function that prints its arguments values and their sum to the console and that returns nothing:

```{code-cell}
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

The first line of the function definition is called the **function signature**. It defines how to use the function. By reading the signature of `print_sum`, we know that the function is named `print_sum` and that it expects two arguments.

Note the colon `:` that terminates the function signature. A colon indicates that the following indented lines are a code block, which is simply a series of lines that belong to a same group. In the case of a function, this code block is the **function implementation**. This is the lines to be executed when the function is called. In Python, code blocks are delimited by their indentation. Every line of a code block must be indented with the same number of spaces.

:::{tip}
Since indentation is so important in Python, practically all Python editors include keyboard shortcuts to indent or outdent code blocks. In Spyder, select a group of lines, then press `Tab` to indent these lines altogether, or `Shift+Tab` to outdent.
:::


Once a function is defined (using the `def` keyword), it can be called as many times as needed:

```{code-cell}
print_sum(1, 4)
print_sum(3, 10)
```

:::{good-practice} Function naming
Usually, function names start with an active verb that tells what action is performed. Usually in Python, function names are written in `lower_case` style, with words separated by underscores.
:::

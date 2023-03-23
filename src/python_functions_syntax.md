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

In python, functions are defined using this syntax:

```
def function_name(arg1, arg2, ...):
    # operation1
    # operation2
    # operation3
    # etc.
    return the_result
```

This reads as "Define the function `function_name`, which takes `arg1`, `arg2`, ... as input. This function will process these inputs and return `the_result` as an output.

Here is an example of a function that prints its input values and their sum:

```{code-cell}
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

Once a function is defined (using the `def` keyword), it can be called as many times as we want:

```{code-cell}
print_sum(1, 4)
print_sum(3, 10)
```

:::{good-practice} Function naming
Usually, function names start with an active verb that tells what action is performed. Usually in Python, function names are written in `lower_case` style, with words separated by underscores, like variables.
:::

The first line of the function definition is called the **function signature**. It defines how to use the function. By reading the signature of our example, we know that the function is called `print_sum` and that it takes two arguments.

:::{note}
In the different references found on the web, we often see both the terms "argument" and "parameter" for function inputs. Both terms are equivalent and will be used interchangeably.
:::

Note the colon `:` that terminates the function signature. A colon indicates that the following indented lines are a code block, which is simply a series of lines that belong to a same group. In the case of a function, this code block is the **function implementation**. This is the lines to be executed when the function is called. In python, code blocks are delimited by their indentation. Every line of a code block must be indented with the same number of spaces.

:::{tip}
Since indentation is so important in python, practically all python editors include keyboard shortcuts to indent or outdent code blocks. In Spyder, select a group of lines that you want to indent or outdent, then press `Tab` to indent, or `Shift+Tab` to outdent.
:::

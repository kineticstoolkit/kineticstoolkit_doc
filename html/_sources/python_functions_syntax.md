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

# Function syntax

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

:::{good-practice} Function naming
Usually, function names start with an active verb that tells what action is performed by the function. PEP8 also recommends that function names be written in lower_case with words separated by underscores, like with variables.
:::

## Signature and implementation

The first line of the function definition is called the **function signature**. It defines how to use the function. We now know that the function is called `print_sum`, that it takes two arguments, and that it returns nothing.

:::{note}
In the different references found on the web, we often see both the terms "argument" and "parameter" for function inputs. Both terms are equivalent and will be referred by both words from now on.
:::

Note the colon `:` that terminates the function signature. A colon signifies that the following lines will be a code block, which is simply a series of lines that belong to a same group. In the case of a function, this code block is the **function implementation**. This is the lines to be executed when the function is called. In Python, code blocks are delimited by their indentation. Every line of a code block must be indented with the same number of spaces.

:::{tip}
Since indentation is so important in Python, practically all Python editors include keyboard shortcuts to indent or outdent code blocks. In Spyder, select a group of lines that you want to indent or outdent, then press `Tab` to indent, or `Shift+Tab` to outdent.
:::

## Argument names

In the `print_sum` example, we used `arg1` and `arg2` as argument names. In reality, any name will work equally. For instance, we could also use `first` and `second`, as long as we refer to these names in the implementation:

```{code-cell}
def print_sum(first, second):
    print("Hi!")
    print(f"The first variable is {first}.")
    print(f"The second variable is {second}.")
    print(f"The sum of both variables is {first + second}.")
```

:::{good-practice} Clear argument names
It is very important to use clear names for function arguments. Argument names are selected using the same best practices as standard [variable](python_arithmetics_and_variables.md) names.
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

Please use clear names for your function's arguments.

:::

```{code-cell}
:tags: [hide-cell]

def print_info(i_participant, first_name, last_name, age, height, weight):

    print("=============")
    print(f"Participant {i_participant}: {first_name} {last_name}")
    print(f"{age} years old")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {weight / (height ** 2):.2f}")
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


:::{exercise} Calculating Body-Mass Index (BMI)
Program a function called `calculate_bmi` that takes a person's height and weight as arguments, and that returns the body-mass index, knowing that $\text{BMI} = \text{weight}/\text{height}^2$.
:::

```{code-cell}
:tags: [hide-cell]

def calculate_bmi(height, weight):
    return weight / (height ** 2)


# Let's test the function:
print(calculate_bmi(1.5, 50.2))
```

:::{exercise} Printing information (cont'd)
Based on the function `print_info` that you created in a previous example, create a new function `format_info` which does not print the information, but instead creates an equivalent string and returns it, so that:

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

Instead of calculating the BMI manually in the function, use a call to the `calculate_bmi` function that you just wrote in the previous example.

Tip: you may want to return to the section on [strings](python_strings.md) for a refresh on how to create long strings, and how to add line breaks in strings.

:::

```{code-cell}
:tags: [hide-cell]

def format_info(i_participant, first_name, last_name, age, height, weight):

    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {calculate_bmi(height, weight):.2f}\n"
        "============="
    )
    return output


print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))

```

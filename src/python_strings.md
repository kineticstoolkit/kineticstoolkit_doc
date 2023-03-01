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

# 📖 Strings basics

:::{card} Summary
This section introduces the `string` type and how to define it, including single/double quotes, triple quotes, and f-strings. It also shows the `input` function for user input of strings.
:::

In the previous section, we introduced two types to express numbers: `int` and `float`. To express letters, words and sentences, we use the `string` type. You already created a string in your first ["Hello world"](python_using_spyder.md) program.

## 📄 Single and double quotes

A string is created by enclosing characters between quotes. Python does not make a difference between single-quotes `'` and double-quotes `"`. Therefore, the following strings are equivalent:

```
"Hello world!"
'Hello world!'
```

Normally, we will use `"` if the string contains apostrophes `'`; inversely, we will use `'` if the string contains double-quotes `"`. For instance, both these strings are correctly defined:

```
"It's time to lunch."
'I would not call it "results"...'
```

but the following ones generate syntax errors, because the apostrophe or double-quote closes the string before reaching the ending delimiter:

```
'It's time to lunch'
"I would not call it "results"..."
```

## Backslash

Backslash tells Python that the character following the backslash is a special character. It may be used to enter quotes, line breaks and backslash itself in a string.

### Single-quote `\'` and double-quote `\"`

If a same string needs to include both `'` and `"`, then it is impossible to select a correct delimiter. Backslashing a quote character (`\'`, `\"`) tells python that this really is a character, and not a delimiter. For instance:

```{code-cell} ipython3
example1 = "I didn't found \"E = mc2\", Einstein did."
example2 = 'I didn\'t found "E = mc2", Einstein did.'

print(example1)
print(example2)
```

### Line break: `\n`

Newline characters are inserted using `\n`:

```{code-cell} ipython3
example_string = "I ate your sandwich.\nIt was good."

print(example_string)
```

### Backslash: `\\`

To include a backslash in the string, we need to backslash it so that Python sees it as a backslash character, and as a backslash command:

```{code-cell} ipython3
file_path = "C:\\Windows\\important_driver.dll"

print(file_path)
```

## 📄 Triple-quotes

Python provides another type string delimiter: the triple-quote. A string defined by triple-quotes can integrate both single and double quotes in a same string without using backslash. Line breaks are also saved in the string.

```
"""I didn't invent "E = mc2", that's Einstein's thing."""
```

The most popular use for triple-quotes are [docstrings](python_functions_docstrings.md) docstrings, which will be seen later.

```{code-cell} ipython3
example_string = """I ate your sandwich.
It was good."""

print(example_string)
```

## 💪 Exercise

Create a code that creates the variable `str` in such a way that `print(str)` gives:

a)

    I won't have difficulty solving this problem.

b)

    Centre of mass of the "arm + forearm" segment.

c)

    Measured force: 150 N
    Measured moment: 34 Nm

d)

    I received this strange message:
    "ValueError('C:\temp unfound')"

Try different ways to create each variable.

```{code-cell} ipython3
:tags: [hide-cell]

# a)

str = "I won't have difficulty solving this problem."

# b)

str = 'Centre of mass of the "arm + forearm" segment.'

# c)

str = "Measured force: 150 N\nMeasured moment: 34 Nm"

# d) (some examples):

str = "I received this strange message:\n\"ValueError('C:\\temp unfound')\""

str = 'I received this strange message:\n"ValueError(\'C:\\temp unfound\')"'

str = '''I received this strange message:
"ValueError('C:\\temp unfound')"'''
```

## 📄 Creating long strings

Normally, we want our code to fit in a given width and avoid lines that are too long. Many code style conventions limit the width of a code line to 80 characters. Following this advice may be difficult when creating long strings. There is however a way to express a continuous string on multiple lines, by enclosing multiple strings in parentheses.

```{code-cell} ipython3
long_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
    "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
    "aliquip ex ea commodo consequat."
)

print(long_string)
```

## 📄 Combining strings and variables using f-strings

We often use strings to report results. For instance, one way of reporting the ankle moment would be to use two `print` calls:

```{code-cell} ipython3
ankle_moment = 100.1  # (for instance)

print("The calculated moment at the ankle in Nm is:")
print(ankle_moment)
```

A single string that includes both the definition and the result would be more readable:

> "The calculated ankle moment is 100.1 Nm."

Including variables into strings is easily done using f-strings. F-strings' name comes from their `f` prefix. With f-strings, Python evaluates the content between curly braces `{}` and replaces this content by its evaluation.

```{code-cell} ipython3
# Here, we create the sentence above.
the_string = (
    f"The calculated ankle moment is {ankle_moment} Nm."
)

# And here, we print it.
print(the_string)
```

When an f-string contains a float, we can print it to a given precision, using `:.xf` just after the expression in braces, where `x` is the number of digits after the decimal point. For instance:

```{code-cell}
print(f"The calculated ankle moment is {ankle_moment:.0f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.2f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.5f} Nm.")
```

## 📄 User input

To conclude this section, we can also create strings using user input:

```
the_string = input()
```

This allows the user to type some text right in the console, until they press Enter. It is possible and usually a good idea to provide some text to the user:

```
the_string = input("Please enter your name: ")
```

Note that the input function always create a string. If you want the user to input a float, then you need to convert the string to a float:

```
str_height = input("What is the participant's height in meters? ")
```

User enters "1.45"

```{code-cell}
:tags: ["remove-cell"]
str_height = "1.45"
str_cycle = "4"
```

```{code-cell}
height = float(str_height)

print(height)
print(type(height))
```

The same thing applies if we need the user to enter an integer:

```
str_cycle = input("Which gait cycle do we keep? ")
```

User enters "4"

```{code-cell}
i_cycle = int(str_cycle)

print(i_cycle)
print(type(i_cycle))
```

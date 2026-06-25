# Strings

In the previous section, we introduced two types of variables that express numbers: `int` and `float`. To express letters, words, and sentences, we use the `string` type. This section explains different methods to create strings, and to combine strings and numbers.


## Creating strings using quotes

A string is created by enclosing characters between quotes. Python does not make a difference between single-quotes `'` and double-quotes `"`. Therefore, the following strings are equivalent:

```{code-cell}
s1 = "Hello world!"
s2 = 'Hello world!'
```

Normally, we use double-quotes if the string contains apostrophes `'`; conversely, we use single-quotes if the string contains double-quotes `"`. For instance, both these strings are correctly defined:

```{code-cell}
s3 = "It's time for lunch."
s4 = 'I would not call it "results"...'
```

but the following ones generate syntax errors, because the apostrophe or double-quote closes the string before reaching the ending delimiter:

```{code-cell}
:tags: [raises-exception]
s5 = 'It's time for lunch'
s6 = "I would not call it "results"..."
```


## Backslash

Inserting a backslash `\` in a string tells Python that the following character is a special character. It may be used to enter quotes, line breaks or backslashes in a string.

### Single-quote `\'` and double-quote `\"`

If a single string needs to include both apostrophes and double-quotes, then it is impossible to select a correct delimiter. Backslashing a quote character (`\'`, `\"`) tells Python that this really is a character, and not a delimiter. For instance:

```{code-cell} ipython3
example1 = "I didn't write \"E = mc2\", Einstein did."
example2 = 'I didn\'t write "E = mc2", Einstein did.'

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

To include a backslash in the string, we need to backslash it so that Python sees it as a character instead of a backslash command:

```{code-cell} ipython3
file_path = "C:\\Windows\\important_driver.dll"

print(file_path)
```


## Creating strings using triple-quotes

Python provides another type of string delimiter: the triple-quote. A string defined using triple-quotes can integrate both single and double quotes in the same string without using backslash. Line breaks are also saved in the string.

```{code-cell}
s1 = """I didn't write "E = mc2", that's Einstein's thing."""

print(s1)
```

The most common use for triple-quotes are docstrings, which will be seen later in [4_python_functions](4_python_functions.md).

```{code-cell} ipython3
s2 = """I ate your sandwich.
It was good."""

print(s2)
```


## Creating long strings

Normally, we want to avoid writing very long code lines. For instance, it is common to limit the width of a line to 80 characters.

Following this limit may be difficult when creating long strings. To achieve this, we can split a long string on multiple lines, by enclosing multiple sub-strings between parentheses.

```{code-cell} ipython3
long_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
    "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
    "aliquip ex ea commodo consequat."
)

print(long_string)
```


## Including variable contents in strings using f-strings

We often use strings to report results. For instance, we could print a calculated ankle moment to the console using two `print` calls:

```{code-cell} ipython3
ankle_moment = 100.1  # (for instance)

print("The calculated moment at the ankle in Nm is:")
print(ankle_moment)
```

A single string that includes both the definition and the result would be more readable:

> "The calculated ankle moment is 100.1 Nm."

Including variables into strings is easily done using f-strings. The name "f-strings" comes from their `f` prefix. With f-strings, Python evaluates the result of any instruction placed between curly braces `{}`:

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


## 💪 Exercise

For these two variables:

```{code-cell}
force = 150
moment = 34
```

Create a code that creates the variable `str` in such a way that:

```
print(str)
```

gives:

a)

    I won't have difficulty solving this problem.

b)

    Centre of mass of the "arm + forearm" segment.

c) (use the `force` variable)

    Measured force: 150 N


d) (use the `force` and `moment` variables)

    Measured force: 150 N
    Measured moment: 34 Nm

e)

    I received this strange message:
    "ValueError('C:\temp unfound')"

f) (use the `force` and `moment` variables, and limit the width of your code lines to 80 characters)

    We calculated a total force of 150 newton, while the calculated moment was 34 newton-meter.


```{code-cell} ipython3
:tags: [hide-cell]

# a)

str = "I won't have difficulty solving this problem."
print(str)

# b)

str = 'Centre of mass of the "arm + forearm" segment.'
print(str)

# c)

str = f"Measured force: {force} N"
print(str)

# d)

str = f"Measured force: {force} N\nMeasured moment: {moment} Nm"
print(str)

# e) (some examples):

str = "I received this strange message:\n\"ValueError('C:\\temp unfound')\""

str = 'I received this strange message:\n"ValueError(\'C:\\temp unfound\')"'

str = '''I received this strange message:
"ValueError('C:\\temp unfound')"'''

print(str)

# f) 

str = (
    f"We calculated a total force of {force} newton, "
    f"while the calculated moment was {moment} newton-meter."
)
print(str)
```


## User input

We can create strings interactively from user input:

```
the_string = input()
```

This allows the user to type some text right in the console. It is usually a good idea to provide some text to the user:

```
the_string = input("Please enter your name: ")
```

Note that the input function always creates a string. If you want the user to input a float, then you need to convert the string to a float:

```
height = float(input("What is the participant's height in meters? "))
```

Or if we need the user to enter an integer:

```
i_cycle = int(input("Which gait cycle do we keep? "))
```

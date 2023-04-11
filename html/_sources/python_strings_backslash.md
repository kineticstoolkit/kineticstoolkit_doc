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

# Backslash

Inserting a backslash `\` in a string tells Python that the following character is a special character. It may be used to enter quotes, line breaks or backslashes in a string.

## Single-quote `\'` and double-quote `\"`

If a same string needs to include both apostrophes and double-quotes, then it is impossible to select a correct delimiter. Backslashing a quote character (`\'`, `\"`) tells python that this really is a character, and not a delimiter. For instance:

```{code-cell} ipython3
example1 = "I didn't write \"E = mc2\", Einstein did."
example2 = 'I didn\'t write "E = mc2", Einstein did.'

print(example1)
print(example2)
```

## Line break: `\n`

Newline characters are inserted using `\n`:

```{code-cell} ipython3
example_string = "I ate your sandwich.\nIt was good."

print(example_string)
```

## Backslash: `\\`

To include a backslash in the string, we need to backslash it so that Python sees it as a character instead of a backslash command:

```{code-cell} ipython3
file_path = "C:\\Windows\\important_driver.dll"

print(file_path)
```

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


# Indexing and slicing strings

We just saw how to index and slice lists. The exact same behaviour applies to strings: we can extract one or many characters from a string by slicing it:

```{code-cell} ipython3
string = "This is a sample string that we will index and slice"

# Get the first character
print(string[0])

# Get the last character
print(string[-1])

# Get the 10 first characters
print(string[:10])

# Get the 10 last characters
print(string[-10:])

# Get every other character
print(string[::2])
```

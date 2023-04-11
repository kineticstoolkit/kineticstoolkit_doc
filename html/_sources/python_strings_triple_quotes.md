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

# Creating strings using triple-quotes

Python provides another type string delimiter: the triple-quote. A string defined using triple-quotes can integrate both single and double quotes in a same string without using backslash. Line breaks are also saved in the string.

```{code-cell}
s1 = """I didn't write "E = mc2", that's Einstein's thing."""

print(s1)
```

The most common use for triple-quotes are [docstrings](python_functions_docstrings.md), which will be seen later.

```{code-cell} ipython3
s2 = """I ate your sandwich.
It was good."""

print(s2)
```

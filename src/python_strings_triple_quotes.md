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

# Triple-quotes

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

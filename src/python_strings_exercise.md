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

# 💪 Exercise

#todo add f-strings and long strings

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

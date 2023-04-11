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

# 💪 Strings

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

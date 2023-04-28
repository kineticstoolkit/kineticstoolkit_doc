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


# Exercise: Adding entries to dictionaries

Here is a list of dictionaries that contain personal information about the participants of a research project:

```{code-cell} ipython3
participants = [
    {"ID": 101, "Sex": "F", "Height": 1.45, "Weight": 56.0},
    {"ID": 125, "Sex": "M", "Height": 1.72, "Weight": 72.0},
    {"ID": 126, "Sex": "M", "Height": 1.85, "Weight": 94.0},
    {"ID": 132, "Sex": "F", "Height": 1.82, "Weight": 80.0},
]
```

Write a code that adds a new key `BMI` to each of these dictionaries, that is the body-mass index.

```{math}
\text{BMI} = \text{weight}/\text{height}^2
```

```{code-cell} ipython3
:tags: [hide-cell]

for participant in participants:
    participant["BMI"] = participant["Weight"] / (participant["Height"] ** 2)

# Show the result
participants
```

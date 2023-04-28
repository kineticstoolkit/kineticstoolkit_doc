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


# Exercise: Creating and accessing dictionaries 1

Here is a list of dictionaries that contain personal information about the participants of a research project:

```{code-cell} ipython3
participants = [
    {"ID": 101, "Sex": "F", "Height": 1.45, "Weight": 56.0},
    {"ID": 125, "Sex": "M", "Height": 1.72, "Weight": 72.0},
    {"ID": 126, "Sex": "M", "Height": 1.85, "Weight": 94.0},
    {"ID": 132, "Sex": "F", "Height": 1.82, "Weight": 80.0},
]
```

Write a code that calculates the average height among all participants. The number of participants may vary; therefore, your function should work for a list of any length.

```{code-cell} ipython3
:tags: [hide-cell]

# Calculate the sum
total = 0
for participant in participants:
    total += participant["Height"]

# Divide by the number of participants
average = total / len(participants)

# Show the result
print(f"The average height is {average} m.")
```

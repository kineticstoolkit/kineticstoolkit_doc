# Type annotations

In addition to [docstrings](python_functions_docstrings.md), type annotations are increasingly popular to document the types of a function's parameters and return value. Like docstrings, type annotations are facultative, but are generally helpful to clearly design and document functions.

The syntax for type annotations is `:` for the parameters, and `->` for return values (see the `->` as a right-arrow). In the `format_info` function above, we documented the parameters and return types in the docstring. Using type annotations, we could instead document those directly in the signature:

```
def format_info(
    i_participant: int,
    first_name: str,
    last_name: str,
    age: float,
    height: float,
    weight: float
) -> str:
    """
    Format the provided information into a human-readable string.

    Parameters
    ----------
    i_participant
        Identifier for the participant
    first_name
        First name (given name) of the participant
    last_name
        Last name (surname) of the participant
    age
        Age of the participant, in years
    height
        Height of the participant, in meters
    weight
        Weight of the participant, in kg

    Returns
    -------
    str
        A human-readable string based on the provided information.

    """
```

:::{note}
Writing a good docstring is way more important than using type annotations. The choice of using type annotations or not is strictly up to you, but it is important to know that it exists, if only to understand others' code.
:::

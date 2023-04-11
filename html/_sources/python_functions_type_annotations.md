# Type annotations

In addition to [docstrings](python_functions_docstrings.md), type annotations (also called type hints) are increasingly popular to document the types of a function's parameters and return value.

:::{good-practice} Docstring vs type annotations
Always write a good docstring in the first place. Type annotation are definitely facultative, and at this point, knowing about type annotations is important mainly to understand external documentation.
:::

Type annotations use `:` to document parameter types, and `->` to document return value types (see the `->` as a right-arrow). Type annotation allows documenting the types directly in the function signature instead of the docstring:

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

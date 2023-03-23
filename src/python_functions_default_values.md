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

# Default values

::::{margin}
```
pandas.read_csv(
    filepath_or_buffer,
    sep=NoDefault.no_default,
    delimiter=None,
    header='infer',
    names=NoDefault.no_default,
    index_col=None,
    usecols=None,
    squeeze=None,
    prefix=NoDefault.no_default,
    mangle_dupe_cols=True,
    dtype=None,
    engine=None,
    converters=None,
    true_values=None,
    false_values=None,
    skipinitialspace=False,
    skiprows=None,
    skipfooter=0,
    nrows=None,
    na_values=None,
    keep_default_na=True,
    na_filter=True,
    verbose=False,
    skip_blank_lines=True,
    parse_dates=None,
    infer_datetime_format=False,
    keep_date_col=False,
    date_parser=None,
    dayfirst=False,
    cache_dates=True,
    iterator=False,
    chunksize=None,
    compression='infer',
    thousands=None,
    decimal='.',
    lineterminator=None,
    quotechar='"',
    quoting=0,
    doublequote=True,
    escapechar=None,
    comment=None,
    encoding=None,
    encoding_errors='strict',
    dialect=None,
    error_bad_lines=None,
    warn_bad_lines=None,
    on_bad_lines=None,
    delim_whitespace=False,
    low_memory=True,
    memory_map=False,
    float_precision=None,
    storage_options=None
)
```
::::

In the `pandas.read_csv` example (on the right), the only mandatory argument is the name of the csv file to read. Every other argument has a default value, and exists only to modify the default behaviour of the function.

Let's examine this concept with a simpler function. We define the following function that calculates the ground reaction force based on the acceleration and mass of a person's center of mass:

```{code-cell} ipython3
GRAVITATIONAL_CONSTANT = 9.81  # m/s2


def calculate_reaction_force(mass, acceleration):
    """
    Calculate the vertical reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * GRAVITATIONAL_CONSTANT)


# Test the function
print(calculate_reaction_force(mass=60, acceleration=3.5))
```

:::{good-practice} Constants
Note these conventions used for GRAVITATIONAL_CONSTANT:

**No magic constants**: Instead of writing plainly 9.81 in the function's return statement, we defined the gravity using a name, and we used that name in the equation. We generally want to avoid "magical" constants dispersed around the code: we call them "magical" because after time, we tend to not remember what these values are for, other than making the function work "magically". Using named constants is a good way to auto-document the code and better understanding it later.

**Top of the file**: It is common practice to define all the constants once and at a same obvious place, which is the top of the file.

**CAPITAL_CASE**: In Python, a constant is simply a variable that we agree to never modify. To emphasize that it should never be modified, it is common practice to user CAPITAL_CASE to define constants, and lower_case to define standard variables.
:::

Although this function works very well as is, we may want to generalize it for different gravitational constants, to simulate a similar task in a different gravity. In this case, the gravitational constant could become a parameter of the function:

```{code-cell} ipython3
def calculate_reaction_force(mass, acceleration, gravitational_constant):
    """
    Calculate the ground reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.
    gravitational_constant : float
        Gravitational constant, in m/s2.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * gravitational_constant)


# Test the function:
print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=9.81
    )
)

print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=5.2
    )
)
```

However, since most of the time, the gravitational constant really is 9.81 m/s², the function would be clearer with a default value for `gravitational_constant`. This is done by using an equal `=` sign in the signature:

```{code-cell} ipython3
def calculate_reaction_force(mass, acceleration, gravitational_constant=9.81):
    """
    Calculate the ground reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.
    gravitational_constant : float
        Gravitational constant, in m/s2. Default is 9.81.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * gravitational_constant)
```

Now, on earth at sea level, the function works exactly as the original one, without having to specify a gravitational constant:

```{code-cell} ipython3
print(calculate_reaction_force(mass=60, acceleration=3.5))
```

but it also adds the possibility to use other gravitational constants, using the same function:

```{code-cell} ipython3
print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=5.2
    )
)
```

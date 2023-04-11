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

# Positional and keyword arguments

Up to now, we called functions using an ordered list of arguments: each argument was assigned using its position. For instance, in this function:

```{code-cell} ipython3
def print_full_name(first_name, last_name):
    """Print the full name of a person."""
    print(f"{first_name} {last_name}")
```

We know that the first argument should be the first name, followed by the last name. This is known as **positional arguments**. We would call this function using:

```{code-cell} ipython3
print_full_name("Catherina", "Smith")
```


::::{margin}
```
pandas.read_csv(
    filepath_or_buffer,
    *,
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

In Python, it is also possible to call functions using **keyword arguments**. To do so, we directly assign values to the argument names using `=` signs. This can make the code still clearer:

```{code-cell} ipython3
print_full_name(first_name="Catherina", last_name="Smith")
```

Note that keyword arguments can be assigned in any order:

```{code-cell} ipython3
print_full_name(last_name="Smith", first_name="Catherina")
```

For very simple functions, using keyword arguments is not that useful. However, some functions may have lots of arguments, with many of them being optional. For example, let's look at the signature of Pandas' {{pd_read_csv}} function (we will use Pandas later), on the right. →

It has an awful lot of arguments, most of them being optional. In this case, it makes no sense to remember their order: using keyword arguments is much preferred.

:::{tip}
It is possible to use both lists of arguments and keyword arguments in a same function call. We begin with the list of arguments, which are being assigned based on their order, and end with keyword arguments:

```
pandas.read_csv(filename, delimiter=',')
```
:::

:::{note}
In some function signatures, you may sometimes see these symbols: `/` and `*`.
- Any argument that comes before a `/` symbol must be a positional argument.
- Any argument that comes after a `*` symbol must be a keyword argument.
:::

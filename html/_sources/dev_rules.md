# Development rules

This page is an attempt to guide future collaborators in co-developing Kinetics Toolkit. We will start with the first and most important rule:

## Rule 1: Code of conduct

Developing should be fun for everyone, and anybody who wants to contribute should be welcomed, guided and respected. As for any collective developement, ideas can clash, friction can happen, and compromises can or cannot be done. However, despite this possible friction, it is of the utmost importance to stay polite, inclusive and respectful.

## Rule 2: Consider writing tutorials instead of code

Before even starting to develop a new function, one should ask this important question: **Should this feature really be developed, or should I write a tutorial instead?**

We remind that Kinetics Toolkit aims to provide tools for the user to achieve their needs in biomechanical research. Often, the best way to control our data is by learning how to do it instead of using a function performs it for us. In that view, any new feature should start with a discussion on a [feature request issue](https://github.com/felixchenier/kineticstoolkit/issues).

- If a new tutorial is needed, then please contribute to the [kineticstoolkit_doc](https://github.com/felixchenier/kineticstoolkit_doc) repository, that version this website's code.
- If a new function or module is needed, then continue with this guide.

## Rule 3: Life cycle of a function, from development to deprecation

New public functions appear and live in the following order:

### Unstable

These functions are currently being developed. They are decorated with the `@unstable` decorator. This decorator has two main functions:

- They include the function in the module's or class' `__dir__` in the development version, but not in the stable version;
- They automatically add an unstable warning to their docstring.

```
from kineticstoolkit.decorators import unstable


@unstable
def name_of_the_unstable_function(arguments: str) -> None:
    """Docstring of the unstable function."""
    ...

```

### Experimental

These objects are part of the API but are not considered stable yet. They are documented accordingly in their docstring, with the following text just before the parameters section (replace the version number):

```
    Warning
    -------
    This function, which has been introduced in 0.4, is still experimental and
    may change signature or behaviour in the future.
```

They don't have a dedicated decorator.

### Stable

Standard production function, without specific decorator or warning.

### Deprecated

These deprecated functions are decorated with the `@deprecated` decorator, which has two functions:

- They automatically add a deprecated warning to their docstring;
- They generate a `FutureWarning` when the deprecated functions are used.

```
from kineticstoolkit.decorators import deprecated


@deprecated(since='0.1', until='0.2',
            details='It has been replaced by `better_function` because '
                    'the latter is much better.')
def deprecated_function_name(arguments: str) --> None:
    """Deprecated function docstring"""
    ...

```


## Rule 4: Forks and branches

### Fork and create a feature branches

To start the developemnt of a feature, please fork the repository. Then, in your fork, create a feature branch: `feature/[FEATURE_NAME]` from the `master` branch.

### Document and test your feature

All of the above should be done before making a pull request:

- The new code must match Kinetics Toolkit's [coding style](dev_coding_style.md).
- The feature should be finished, or logical and documented parts of the feature should be finished.
- The feature's docstring must match its current completion state.
- The feature's docstring can include examples. If this is the case, they should be testable with `doctest`.
- The feature includes unit tests.

While on the feature branch, `ktk.dev.run_tests()` should run with success. This function runs `autopep8`, `mypy`, and every unit test. It is okay to have some warnings (some tests target edge cases that trigger warnings), but no error.

### Create a pull request

When everything is done and passes, it is time to create a pull request. I will then test your feature. If everything is good, I'll merge your pull request and merge the feature into the `master` branch.

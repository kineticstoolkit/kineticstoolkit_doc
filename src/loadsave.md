---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# 📖 Saving and loading

Contrarily to Matlab with its mat file, python does not come with a single standard way to save data. To ease saving and sharing data, Kinetics Toolkit provides two functions that load and save its own ktk.zip format:

- [](api/ktk.save.rst)
- [](api/ktk.load.rst)

These functions are straightforward to use:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

variable = {
    "some_array": np.arange(0, 5, 0.5),
    "some_text": "hello",
}
```

Saving the variable:

```{code-cell} ipython3
ktk.save("filename.ktk.zip", variable)
```

Loading back the variable:

```{code-cell} ipython3
loaded_variable = ktk.load("filename.ktk.zip")

loaded_variable
```

## 📄 File format and supported types

The `ktk.zip` file format is built to be as portable and simple as possible. It is a standard zip file that contains two JSON files:

- `metadata.json`: File metadata such as the save date, the computer's operating system, the version of the ktk.zip format, etc.
- `data.json`: The data. Data types that are not natively supported by the JSON file format (e.g., numpy, pandas, kineticstoolkit TimeSeries) are converted to supported objects so that they are fully readable in other environments such as Matlab.

The `ktk.zip` file format supports any combination of the following types:

| Already supported by JSON          | Extended for Kinetics Toolkit |
| ---------------------------------- | ----------------------------- |
| dict containing any supported type | numpy.array                   |
| list containing any supported type | pandas.DataFrame              |
| str                                | pandas.Series                 |
| int                                | kineticstoolkit.TimeSeries    |
| float                              |                               |
| True, False, None                  |                               |

Tuples can also be saved but will be loaded back as lists.

## 📄 Loading a ktk.zip file in Matlab

Here are how to load a ktk.zip file in Matlab, using only four instructions.

    % Create a temporary folder to unzip to
    mkdir('temp');
    unzip(filename, 'temp');

    % Load the file contents
    data = jsondecode(fileread('temp/data.json'));
    metadata = jsondecode(fileread('temp/metadata.json'));

Since the types are not the same between python, JSON and Matlab, then some conversion will happen. For instance, a list of floats in python becomes an array of double in Matlab, whereas a list of strings in python becomes a cell array of chars in Matlab. For this reason, there is no official mechanism to transfer data back and forth between python and Matlab using ktk.zip files.

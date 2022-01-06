# Coding style

## Standard Python conventions

We try, when possible, to match the guidelines presented in these documents:

- [Style Guide for Python Code (PEP8)](https://pep8.org);
- [Numpy Docstring](https://numpydoc.readthedocs.io/en/latest/format.html).

Those are precious references and all other sections are additions to these references. Integrated desktop environments may help programmers to follow these conventions. For example, in Spyder, one could enable:

- In `Preferences : Completion in linting : Code style and formatting : Code style`, check `Enable code style linting` to enable PEP8 linting;
- In `Preferences : Completion in linting : Code style and formatting : Code formatting`, Select `autopep8` and check `Autoformat files on save` to ensure minimal PEP8 compliance at all times;
- In `Preferences : Completion in linting : Docstring style`, check `Enable Docstring style linting` and select `Numpy`  to enable Numpy docstring linting.

## Quote style

Strings are single-quoted or double-quoted following their meaning:

- Most strings, particularly strings that behave as identifiers, have single quotes:
    - `kinetics['Forces'] = [0, 0, 0, 0]`
- Strings that contain text in the form of readable sentences have double quotes:
    - `warnings.warn("This sample contains missing data")`
    - `dictionary['key'] = "Please select an option."`

### Naming conventions

The following PEP8 conventions are used:

- All code, comments and documentation are in **English**.
- **Function names** are active (begin by a verb), and are in snake_case (lowercase words separated by underscores):
    - close()
    - calculate_power()
    - detect_cycles()
- **Variable names** are passive, and are also in snake_case:
    - forces
    - detected_markers
- **Class names** are passive, and are in CapitalCase (Capital first letters):
    - TimeSeries
    - Player
- **Constants** are passive, and are in UPPER_SNAKE (uppercase words separated by underscores):
    - CALIBRATION_MATRIX
    - WHEEL_RADIUS

In addition, the following convention is used:

- For strings that are used as identifiers (e.g., keys, signal names), **strings contents** are in CapitalCase:
    - contents['Forces'], kinematics.data['UpperArmR']
    - dataframe.columns = ['SolidTire', 'InflatableTire']

### Type hints

Kinetics Toolkit is type-hinted, with static type checking performed by `mypy`. It does not use python 3.9 contained types yet, and therefore relies on the standard `typing` library.

```
import pandas as pd
import numpy as np
from typing import Dict

def dataframe_to_dict_of_arrays(
        dataframe: pd.DataFrame
) -> Dict[str, np.ndarray]:
    ...

```

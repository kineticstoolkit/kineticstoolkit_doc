# Coding style

## 📄 Standard Python conventions

Coding style is [black](https://black.readthedocs.io/en/stable) with 79-character lines. Docstrings style is [Numpy Docstring](https://numpydoc.readthedocs.io/en/latest/format.html).

## 📄 Naming conventions

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

## 📄 Type hints

Kinetics Toolkit is type-hinted, with static type checking performed by `mypy`. It uses python 3.9 annotations using `__future__`:

```
import pandas as pd
import numpy as np
from __future__ import annotations


def dataframe_to_dict_of_arrays(
        dataframe: pd.DataFrame
) -> dict[str, np.ndarray]:
    ...

```

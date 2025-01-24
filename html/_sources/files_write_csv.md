---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Writing CSV files

To export a TimeSeries to a CSV file, we do the opposite sequence. We first convert the TimeSeries to a DataFrame, then we use the DataFrame's {{dataframe_to_csv}} method to create a CSV file.

In this example, we read some 3D marker positions from a sample C3D file and export these positions as a CSV file. Let's first download and read a sample C3D file. This file is provided by https://www.c3d.org as a test suite for C3D software development. For conciseness, we will only keep the following markers: "RFT1" and "RFT2".

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import pandas as pd

filename = ktk.doc.download("c3d_test_suite_sample.c3d")
c3d_contents = ktk.read_c3d(filename, convert_point_unit=True)
markers = c3d_contents["Points"].get_subset(["RFT1", "RFT2"])

markers
```

```{code-cell} ipython3
markers.data
```

To convert this TimeSeries to a CSV file, we first create a DataFrame:

```{code-cell} ipython3
df = markers.to_dataframe()

df
```

Then we export this DataFrame to a CSV file. Let's print the first 3 lines of this file:

```{code-cell} ipython3
df.to_csv("output.csv", index_label="Time")
```

Here are the first lines of the exported CSV file, ready to be processed in another software:

```{code-cell} ipython3
:tags: [remove-input]

!head -5 output.csv
```

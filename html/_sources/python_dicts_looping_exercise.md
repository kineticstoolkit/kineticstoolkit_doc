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

# Exercise: Looping through a dictionary

We affix an inclinometer on a person's arm. We ask the person to reach different positions in the sagittal plane as shown in {numref}`python_dicts_looping_exercise`. Each position is reached twice.

```{figure-md} fig_shoulder_flexion_inclinometer
:width: 7in
![](_static/images/fig_shoulder_flexion_inclinometer.png)

Different shoulder flexion angles.
```

The inclinometer's readings are stored in a dictionary as follows:

```{code-cell} ipython3
incline = {
    "Reference": -5.0,
    "TargetA_Repetition1": 32.3,
    "TargetB_Repetition1": 73.9,
    "TargetC_Repetition1": 112.1,
    "TargetA_Repetition2": 35.7,
    "TargetB_Repetition2": 82.1,
    "TargetC_Repetition2": 105.8,
}
```

Write a code that creates a new dictionary named `flexion`, that calculates the shoulder flexion angle for each repetition of TargetA, TargetB and TargetC. This new dictionary (`flexion`), will have this form:

```
{
    "TargetA_Repetition1": (flexion angle),
    "TargetB_Repetition1": (flexion angle),
    "TargetC_Repetition1": (flexion angle),
    "TargetA_Repetition2": (flexion angle),
    "TargetB_Repetition2": (flexion angle),
    "TargetC_Repetition2": (flexion angle),
}
```

The flexion angle is calculated as the incline in the target position, minus the incline in the reference position. Your code must adapt to any number of target positions, and any number of repetitions.

```{code-cell} ipython3
:tags: [hide-cell]

# Create an empty dictionary
flexion = {}

for key in incline:
    if key != "Reference":
        flexion[key] = incline[key] - incline["Reference"]

# Show the result
flexion
```

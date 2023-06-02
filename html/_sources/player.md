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

:::{caution}
If you arrived here straight from the home page, you may want to read a bit on the TimeSeries class ([tutorial](timeseries.md), [API](api/ktk.TimeSeries.rst)) to fully understand this tutorial.
:::


# Visualizing 3d markers interactively

## Visualizing the markers

Now we'll take a look at this acquisition using [](api/ktk.Player.rst), a matplotlib-based interactive user interface aimed at visualizing markers, rigid bodies and segments in three dimensions.

Note that for the `Player` class to be interactive, you must select an interactive backend for IPython. See [](getting_started_installing.md) for more information.

```{code-cell} ipython3
:tags: [remove-output]

import kineticstoolkit.lab as ktk

# Set an interactive backend
%matplotlib qt5

# Download and read markers from a sample C3D file
filename = ktk.doc.download("kinematics_tennis_serve.c3d")
markers = ktk.read_c3d(filename)["Points"]

# In this file, the up axis is z:
ktk.Player(markers, up="z")
```

```{code-cell} ipython3
:tags: [remove-input]

temp = markers.get_ts_between_times(6, 8)

viewing_options = {
    "zoom": 1.5,
    "azimuth": 0.8,
    "elevation": 0.16,
    "translation": (-0.2, -1.0),
    "up": "z",
}

ktk.Player(temp, **viewing_options)._to_animation()
```

In the interactive Player window, press space to start the video, zoom and drag with the mouse, or press `h` in the Player window for additional help.

Note the colored global reference frame on the bottom. This reference frame and every other (as we will create in the next tutorial) follow the same standard color scheme:

- x = Red
- y = Green
- z = Blue

## Interconnecting the markers

To ease the visualization, it is often practical to interconnect markers with lines. Here, we create those links as a dictionary.

```{code-cell} ipython3
interconnections = dict()  # Will contain all segment definitions

interconnections["LLowerLimb"] = {
    "Color": [0, 0.5, 1],  # In RGB format (here, greenish blue)
    "Links": [  # List of lines that span lists of markers
        ["Derrick:LTOE", "Derrick:LHEE", "Derrick:LANK", "Derrick:LTOE"],
        ["Derrick:LANK", "Derrick:LKNE", "Derrick:LASI"],
        ["Derrick:LKNE", "Derrick:LPSI"],
    ],
}

interconnections["RLowerLimb"] = {
    "Color": [0, 0.5, 1],
    "Links": [
        ["Derrick:RTOE", "Derrick:RHEE", "Derrick:RANK", "Derrick:RTOE"],
        ["Derrick:RANK", "Derrick:RKNE", "Derrick:RASI"],
        ["Derrick:RKNE", "Derrick:RPSI"],
    ],
}

interconnections["LUpperLimb"] = {
    "Color": [0, 0.5, 1],
    "Links": [
        ["Derrick:LSHO", "Derrick:LELB", "Derrick:LWRA", "Derrick:LFIN"],
        ["Derrick:LELB", "Derrick:LWRB", "Derrick:LFIN"],
        ["Derrick:LWRA", "Derrick:LWRB"],
    ],
}

interconnections["RUpperLimb"] = {
    "Color": [1, 0.5, 0],
    "Links": [
        ["Derrick:RSHO", "Derrick:RELB", "Derrick:RWRA", "Derrick:RFIN"],
        ["Derrick:RELB", "Derrick:RWRB", "Derrick:RFIN"],
        ["Derrick:RWRA", "Derrick:RWRB"],
    ],
}

interconnections["Head"] = {
    "Color": [1, 0.5, 1],
    "Links": [
        ["Derrick:C7", "Derrick:LFHD", "Derrick:RFHD", "Derrick:C7"],
        ["Derrick:C7", "Derrick:LBHD", "Derrick:RBHD", "Derrick:C7"],
        ["Derrick:LBHD", "Derrick:LFHD"],
        ["Derrick:RBHD", "Derrick:RFHD"],
    ],
}

interconnections["TrunkPelvis"] = {
    "Color": [0.5, 1, 0.5],
    "Links": [
        ["Derrick:LASI", "Derrick:STRN", "Derrick:RASI"],
        ["Derrick:STRN", "Derrick:CLAV"],
        ["Derrick:LPSI", "Derrick:T10", "Derrick:RPSI"],
        ["Derrick:T10", "Derrick:C7"],
        ["Derrick:LASI", "Derrick:LSHO", "Derrick:LPSI"],
        ["Derrick:RASI", "Derrick:RSHO", "Derrick:RPSI"],
        [
            "Derrick:LPSI",
            "Derrick:LASI",
            "Derrick:RASI",
            "Derrick:RPSI",
            "Derrick:LPSI",
        ],
        [
            "Derrick:LSHO",
            "Derrick:CLAV",
            "Derrick:RSHO",
            "Derrick:C7",
            "Derrick:LSHO",
        ],
    ],
}
```

Now we can load a Player again with the segments we just defined:

```{code-cell} ipython3
:tags: [remove-output]

ktk.Player(markers, up="z", interconnections=interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]

player = ktk.Player(
    markers.get_ts_between_times(6, 8),
    interconnections=interconnections,
    **viewing_options
)

player._to_animation()
```

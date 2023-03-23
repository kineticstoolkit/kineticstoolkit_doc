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

# Reading and visualizing markers in 3D

:::{card} Summary
In this tutorial, we will read a `c3d` file that contains tennis serve kinematics, and visualize it in an interactive interface, as shown on the [home page](index.md).
:::

:::{caution}
If you arrived here straight from the home page, you may want to read a bit on the TimeSeries class ([tutorial](timeseries.md), [API](api/ktk.TimeSeries.rst)) to fully understand this tutorial.
:::


## 📄 Reading marker trajectories

We first download the sample data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

filename = ktk.doc.download("kinematics_tennis_serve.c3d")
```

:::{credits}
These data were kindly offered by Ms Fraje Watson, Prof Steve Taylor, and Mr Jin (Derrick) Gaokuang, from [University College London](https://www.ucl.ac.uk/), [Aspire CREATe lab](https://ucl.ac.uk/aspire-create).
:::

Then we can read it using [ktk.read_c3d](api/ktk.read_c3d.rst), which returns the file contents as a dictionary with two keys:
- `Point`: the point data (markers)
- `Analogs`: only when applicable. Contains the analog data from force platforms, EMG or other analog signals recorded into the c3d file.

```{code-cell} ipython3
c3d_contents = ktk.read_c3d(filename)
markers = c3d_contents["Points"]
```

The result is a [TimeSeries](api/ktk.TimeSeries.rst) where each marker corresponds to a data key:

```{code-cell} ipython3
markers
```

We see that this acquisition has 1092 samples and 39 markers:

```{code-cell} ipython3
markers.data
```

## 📄 Visualizing the markers

Now we'll take a look at this acquisition using [](api/ktk.Player.rst), a matplotlib-based interactive user interface aimed at visualizing markers, rigid bodies and segments in three dimensions.

Note that for the `Player` class to be interactive, you must select an interactive backend for IPython. See [](getting_started_installing.md) for more information. It is also possible to generate non-interactive animations in Jupyter-based environments, like on this website. Here, we show both methods; we will subsequently only show the commands for the interactive player.

::::{tab-set}

:::{tab-item} Interactive player
```
# Set an interactive backend
# https://kineticstoolkit.uqam.ca/doc/ktk_installing.html
# for more information
%matplotlib qt5

# In this file, the up axis is z:
ktk.Player(markers, up="z")
```
:::

:::{tab-item} Non-interactive animation (Jupyter)
```
# Non-interactive, inline backend
%matplotlib inline

# Create the player and set a viewpoint
player = ktk.Player(
    markers,
    up="z",
    zoom=1.5,
    azimuth=0.8,
    elevation=0.16,
    translation=(-0.2, -1.0),
)

# Create an html video to be included in the Jupyter Notebook
player.to_html5(
    start_time=6,
    stop_time=8
)
```

:::
::::

```{code-cell} ipython3
:tags: [remove-input]

viewing_options = {
    "zoom": 1.5,
    "azimuth": 0.8,
    "elevation": 0.16,
    "translation": (-0.2, -1.0),
    "up": "z",
}

player = ktk.Player(markers, **viewing_options)

player.to_html5(
    start_time=6, stop_time=8
)  # Show only one second of acquisition
```

In the interactive Player window, press space to start the video, zoom and drag with the mouse, or press `h` in the Player window for additional help.

Note the colored global reference frame on the bottom. This reference frame and every other (as we will create in the next tutorial) follow the same standard color scheme:

- x = Red
- y = Green
- z = Blue

## 📄 Interconnecting the markers

To ease the visualization, it is often practical to interconnect markers with lines. Here, we create those links as a dictionary.

```{code-cell} ipython3
interconnections = dict()  # Will contain all segment definitions

interconnections["LLowerLimb"] = {
    "Color": [0, 0.5, 1],  # In RGB format (here, greenish blue)
    "Links": [             # List of lines that span lists of markers
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
    markers, interconnections=interconnections, **viewing_options
)

player.to_html5(
    start_time=6, stop_time=8
)  # Show only one second of acquisition
```

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

%matplotlib qt5
```

# Interconnecting the points

In the previous section, we learned how to show markers in the Player:

```{code-cell} ipython3
:tags: [remove-output]
import kineticstoolkit.lab as ktk

# Download and read markers from a sample C3D file
filename = ktk.doc.download("kinematics_tennis_serve_2players.c3d")
markers = ktk.read_c3d(filename)["Points"]
p = ktk.Player(markers, up="z", anterior="-y")
```

```{code-cell} ipython3
:tags: [remove-input]
p.set_contents(markers.get_ts_between_times(6, 8))
p._to_animation()
```


## Interconnection dictionary

To ease the visualization, it is often practical to interconnect markers with lines. We create these links as a dictionary of this form:

:::{figure-md} fig_player_interconnections
:width: 5in
![Player custom viewpoint](_static/images/player_interconnections.png)

Interconnection dictionary.
:::

Let's see the list of point names we have in this example:

```{code-cell} ipython3
markers.data.keys()
```

To create interconnections for Derrick's left lower limb, we would need to connect these points:

- Foot: draw a line that starts at `Derrick:LTOE`, then `Derrick:LHEE`, then `Derrick:LANK`, then back to `Derrick:LTOE`.
- Shank and thigh: draw a line that starts at `Derrick:LANK`, then `Derrick:LKNE`, then `Derrick:LASI`. Also, draw a line between `Derrick:LKNE` and `Derrick:LPSI`.

This translates to this code:

```{code-cell} ipython3
interconnections = dict()

interconnections["LLowerLimb"] = {
    "Color": (0, 0.5, 1),  # In (R,G,B) format (here, greenish blue)
    "Links": [  # List of lines that span lists of markers
        ["Derrick:LTOE", "Derrick:LHEE", "Derrick:LANK", "Derrick:LTOE"],
        ["Derrick:LANK", "Derrick:LKNE", "Derrick:LASI"],
        ["Derrick:LKNE", "Derrick:LPSI"],
    ],
}
```

Let's see the result:

```{code-cell} ipython3
p.set_interconnections(interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]
p._to_animation()
```


We continue with Derrick's other segments:

```{code-cell} ipython3
interconnections["RLowerLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["Derrick:RTOE", "Derrick:RHEE", "Derrick:RANK", "Derrick:RTOE"],
        ["Derrick:RANK", "Derrick:RKNE", "Derrick:RASI"],
        ["Derrick:RKNE", "Derrick:RPSI"],
    ],
}

interconnections["LUpperLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["Derrick:LSHO", "Derrick:LELB", "Derrick:LWRA", "Derrick:LFIN"],
        ["Derrick:LELB", "Derrick:LWRB", "Derrick:LFIN"],
        ["Derrick:LWRA", "Derrick:LWRB"],
    ],
}

interconnections["RUpperLimb"] = {
    "Color": (1, 0.5, 0),
    "Links": [
        ["Derrick:RSHO", "Derrick:RELB", "Derrick:RWRA", "Derrick:RFIN"],
        ["Derrick:RELB", "Derrick:RWRB", "Derrick:RFIN"],
        ["Derrick:RWRA", "Derrick:RWRB"],
    ],
}

interconnections["Head"] = {
    "Color": (1, 0.5, 1),
    "Links": [
        ["Derrick:C7", "Derrick:LFHD", "Derrick:RFHD", "Derrick:C7"],
        ["Derrick:C7", "Derrick:LBHD", "Derrick:RBHD", "Derrick:C7"],
        ["Derrick:LBHD", "Derrick:LFHD"],
        ["Derrick:RBHD", "Derrick:RFHD"],
    ],
}

interconnections["TrunkPelvis"] = {
    "Color": (0.5, 1, 0.5),
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

p.set_interconnections(interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]
p._to_animation()
```


## Wildcards

We could do the same for Viktor, by replacing every occurrence of "Derrick:" by "Viktor:" in `interconnections`. However, a more generic way is to use wildcards (`*`). A wildcard mean "assign any name in place of `*`". According to the naming scheme, we may choose to use wildcards as a prefix or as a suffix. Here, we use it as a prefix:

```{code-cell} ipython3
interconnections = dict()  # Will contain all segment definitions

interconnections["LLowerLimb"] = {
    "Color": (0, 0.5, 1),  # In RGB format (here, greenish blue)
    "Links": [  # List of lines that span lists of markers
        ["*LTOE", "*LHEE", "*LANK", "*LTOE"],
        ["*LANK", "*LKNE", "*LASI"],
        ["*LKNE", "*LPSI"],
    ],
}

interconnections["RLowerLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["*RTOE", "*RHEE", "*RANK", "*RTOE"],
        ["*RANK", "*RKNE", "*RASI"],
        ["*RKNE", "*RPSI"],
    ],
}

interconnections["LUpperLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["*LSHO", "*LELB", "*LWRA", "*LFIN"],
        ["*LELB", "*LWRB", "*LFIN"],
        ["*LWRA", "*LWRB"],
    ],
}

interconnections["RUpperLimb"] = {
    "Color": (1, 0.5, 0),
    "Links": [
        ["*RSHO", "*RELB", "*RWRA", "*RFIN"],
        ["*RELB", "*RWRB", "*RFIN"],
        ["*RWRA", "*RWRB"],
    ],
}

interconnections["Head"] = {
    "Color": (1, 0.5, 1),
    "Links": [
        ["*C7", "*LFHD", "*RFHD", "*C7"],
        ["*C7", "*LBHD", "*RBHD", "*C7"],
        ["*LBHD", "*LFHD"],
        ["*RBHD", "*RFHD"],
    ],
}

interconnections["TrunkPelvis"] = {
    "Color": (0.5, 1, 0.5),
    "Links": [
        ["*LASI", "*STRN", "*RASI"],
        ["*STRN", "*CLAV"],
        ["*LPSI", "*T10", "*RPSI"],
        ["*T10", "*C7"],
        ["*LASI", "*LSHO", "*LPSI"],
        ["*RASI", "*RSHO", "*RPSI"],
        ["*LPSI", "*LASI", "*RASI", "*RPSI", "*LPSI"],
        ["*LSHO", "*CLAV", "*RSHO", "*C7", "*LSHO"],
    ],
}

p.set_interconnections(interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]
p._to_animation()
```

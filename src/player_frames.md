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


# Visualizing frames

In the last sections, we only visualized points. The Player can also draw [frames](geometry_frames.md), expressed as TimeSeries data with a shape of (N, 4, 4). For instance, let's create two series of frames that revolve around the x and z axes:

```{code-cell} ipython3
:tags: [remove-output]

import numpy as np
import kineticstoolkit.lab as ktk

# Create a TimeSeries with two rotating frames
frames = ktk.TimeSeries(time=np.linspace(0, 5, 100))

frames.data["RotationAroundX"] = ktk.geometry.create_transforms(
    angles=np.linspace(0, 2 * np.pi, 100),
    translations=[[0.2, 0.0, 0.0]],
    seq="x",
)

frames.data["RotationAroundZ"] = ktk.geometry.create_transforms(
    angles=np.linspace(0, 2 * np.pi, 100),
    translations=[[0.0, 0.0, 0.2]],
    seq="z",
)

# Show these frames in the Player
p = ktk.Player(frames)
```

```{code-cell} ipython3
:tags: [remove-input]
p.azimuth = 0.8
p.elevation = 0.16
p.zoom = 10
p._to_animation()
```

---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib qt5
```

# Player basics

:::{note}
The Player is an interactive class that needs an interactive Matplotlib backend. See section [](getting_started_installing.md) for more information.
:::

In this section, we will use kinematic data of [tennis serves](dataset_kinematics_tennis_serve.md) as a [TimeSeries](timeseries.md) of marker positions.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

# Set an interactive backend, not required if already enabled in Spyder
%matplotlib qt5

# Download and read markers from a sample C3D file
filename = ktk.doc.download("kinematics_tennis_serve_2players.c3d")
markers = ktk.read_c3d(filename)["Points"]
```

To visualize these markers, we instantiate a [Player](api/ktk.Player.rst) using one of these methods:

```
p = ktk.Player(markers)

# or

p = ktk.Player()
p.set_contents(markers)
```

Then we can start playback by pressing `space bar`, or using:

```
p.play()
```

```{code-cell} ipython3
:tags: [remove-input]

p = ktk.Player()
p.set_contents(markers.get_ts_between_times(6, 8))
p._to_animation()
```

Press `h` to print a help overlay on how to control the Player using the keyboard:

```{code-cell} ipython3
:tags: [remove-input]

print(ktk.player.HELP_TEXT)
```

Note the coloured global reference frame on the bottom. This reference frame and every other follow the same standard colour scheme:

- x = Red
- y = Green
- z = Blue

Once a player has been instantiated, many properties can be modified to control or customize it:

```{code-cell} ipython3
p
```

We will learn how to use these properties in the following sections.

:::{note}
Every property can be set directly at creation time, for example:

```
p = ktk.Player(markers, up="z", anterior="-y")
```
:::

## Orienting the data

We clearly see that these data do not match the orientation of the Player's ground plane. In these data, the vertical axis is z, and the antero-posterior axis is y, pointing backward. To align the Player correctly to the data:

```{code-cell} ipython3
p.up = "z"
p.anterior = "-y"
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

## Setting the viewpoint

Use the mouse to change the viewpoint interactively.

In addition, once the Player is correctly aligned to the data, we can set the viewpoint using the keyboard (numbers 1-6) or [ktk.Player.set_view](api/ktk.Player.set_view.rst):

```{code-cell} ipython3
p.set_view("front")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

```{code-cell} ipython3
p.set_view("top")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

To revert to the initial view (at the instantiation of the Player):

```{code-cell} ipython3
p.set_view("initial")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

It is also possible to set a custom viewpoint, using these properties (some of them are illustrated in {numref}`fig_player_view_point`):
- `target`: where the camera looks
- `azimuth`: from what angle in the transverse plane
- `elevation`: from what angle relative to the transverse plane
- `pan`: panning in (x, y), in the camera's point of view
- `zoom`: zoom, in the camera's point of view

:::{figure-md} fig_player_view_point
:width: 4.5in
![Player custom viewpoint](_static/images/player_view_point.png)

Visual representation of `target`, `azimuth` and `elevation`.
:::

For example:

```{code-cell} ipython3
p.target = (0.0, 0.0, 1.0)
p.azimuth = 3.1416 / 4  # pi/4 = 45 deg
p.elevation = 3.1416 / 6  # pi/6 = 30 deg
p.zoom = 0.75
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

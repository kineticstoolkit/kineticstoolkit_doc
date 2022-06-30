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

# Reconstructing probed points

In the previous tutorial, we learned how to reconstructed "virtual" markers that are not physically attached to a bony landmark, but that were during a previous acquisition. Sometimes, it is completely impossible to affix a marker on a landmark, for example if the landmark is obstructed with clothes or other objects. In these situation, it may be possible to use a digitizing probe (image below, from optitrack.com) to point landmarks during short acquisitions of a few seconds, and use these probed points to reconstruct the landmarks trajectory during other acquisitions.

![Digitizing probe -height:short](_static/images/probe-kit.png)

The whole process is a bit more complex than in the previous tutorials, but the tools provided by Kinetics Toolkit will help. The following example represents such a situation, where the following acquisitions were performed:
- With a rigid body of three markers affixed to the right arm, an acquisition of a few seconds was recorded while another person touched the medial elbow epicondyle with the tip of the probe. Both were barely moving.
- A wheelchair propulsion acquisition was then recorded.
- We want to reconstruct the trajectory of the right medial elbow epicondyle during the propulsion acquisition, even if it was not present during the acquisition.

## Loading sample data

We will create two TimeSeries, one representing the markers available during the probing acquisition, and the other representing the markers available during the propulsion acquisition.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt
import numpy as np

# Probing acquisition
markers_probing = ktk.kinematics.read_c3d_file(
    ktk.doc.download("kinematics_racing_probing_medial_epicondyle_R.c3d")
)
markers_probing = markers_probing.get_subset(
    ["ArmR1", "ArmR2", "ArmR3", "Probe1", "Probe2", "Probe3", "Probe4"]
)

markers_probing.data
```

```{code-cell} ipython3
# Propulsion acquisition
markers_propulsion = ktk.kinematics.read_c3d_file(
    ktk.doc.download("kinematics_racing_propulsion.c3d")
)
markers_propulsion = markers_propulsion.get_subset(["ArmR1", "ArmR2", "ArmR3"])

markers_propulsion.data
```

## Defining the probe calibration

Before beginning with this tutorial, we must know the configuration of the probe. What we need is the position of the probe markers in the probe's local coordinate system, assuming that this coordinate system's origin is at the probe tip. These positions are generally found in rigid body configuration files or in calibration certificates. In this tutorial, our probe has four markers with the following local coordinates:

- Probe1: (0.0021213, -0.0158328, 0.0864285) m
- Probe2: (0.0021213, 0.0158508, 0.0864285) m
- Probe3: (0.0020575, 0.0160096, 0.1309445) m
- Probe4: (0.0021213, 0.0161204, 0.1754395) m

We will use these known coordinates to create a cluster as in the previous tutorials, but here we do it manually since we already know the coordinates.

```{code-cell} ipython3
probe = {
    "ProbeTip": np.array([[0.0, 0.0, 0.0, 1.0]]),
    "Probe1": np.array([[0.0021213, -0.0158328, 0.0864285, 1.0]]),
    "Probe2": np.array([[0.0021213, 0.0158508, 0.0864285, 1.0]]),
    "Probe3": np.array([[0.0020575, 0.0160096, 0.1309445, 1.0]]),
    "Probe4": np.array([[0.0021213, 0.0161204, 0.1754395, 1.0]]),
}
```

## Tracking the probe in the probing acquisition

In the probing acquisition, since the probe tip points on the medial epicondyle, we can consider the probe tip as if it was a real marker affixed on the medial epicondyle. The first step is therefore to track the probe tip during the probing acquisition, using the four markers of the probe.

```{code-cell} ipython3
reconstructed_probe_markers_during_probing = ktk.kinematics.track_cluster(
    markers_probing,
    probe,
)

reconstructed_probe_markers_during_probing.data
```

Since we reconstructed the trajectory of the probe tip during the probing acquisition, we can now consider that this trajectory is the same as if a real marker had been affixed on the medial epicondyle.

```{code-cell} ipython3
markers_probing.data[
    "MedialEpicondyleR"
] = reconstructed_probe_markers_during_probing.data["ProbeTip"]

markers_probing.data
```

## Creating a cluster of markers

We are now in the same situation as the beginning of the previous tutorial. We can now create a cluster that includes the three rigid body markers, **and** the medial epicondyle.

```{code-cell} ipython3
cluster = ktk.kinematics.create_cluster(
    markers_probing, ["ArmR1", "ArmR2", "ArmR3", "MedialEpicondyleR"]
)

# Print the cluster contents
print(cluster["ArmR1"])
print(cluster["ArmR2"])
print(cluster["ArmR3"])
print(cluster["MedialEpicondyleR"])
```

## Tracking the cluster to reconstruct a "virtual" marker for the epicondyle

Now, exactly like on the previous tutorial, we use this cluster to reconstruct the whole set of four "markers" during the propulsion acquisitions.

```{code-cell} ipython3
reconstructed_markers_propulsion = ktk.kinematics.track_cluster(
    markers_propulsion,
    cluster,
)

# Plot the results
plt.subplot(2, 2, 1)
reconstructed_markers_propulsion.plot("ArmR1")
plt.subplot(2, 2, 2)
reconstructed_markers_propulsion.plot("ArmR2")
plt.subplot(2, 2, 3)
reconstructed_markers_propulsion.plot("ArmR3")
plt.subplot(2, 2, 4)
reconstructed_markers_propulsion.plot("MedialEpicondyleR")
plt.tight_layout()
```

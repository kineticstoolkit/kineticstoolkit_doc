"""Kinetics Toolkit Demonstration - 2. Kinematics analysis."""

# %% Import KTK

import numpy as np

import kineticstoolkit.lab as ktk

# %% Start with the geometry tutorial on the website

# %% Load C3D data

markers = ktk.kinematics.read_c3d_file(
    ktk.doc.download('kinematics_racing_full.c3d')
)

# - markers.data
# - markers.plot

# %% Player

ktk.Player(markers)

# %% Interconnections

interconnections = dict()  # Will contain all segment definitions

interconnections['ArmR'] = {
    'Color': [1, 0, 0],
    'Links': [['AcromionR', 'MedialEpicondyleR'],
              ['AcromionR', 'LateralEpicondyleR'],
              ['AcromionR', 'OlecraneR']]
}

interconnections['ForearmR'] = {
    'Color': [0, 1, 0],
    'Links': [['MedialEpicondyleR', 'RadialStyloidR'],
              ['MedialEpicondyleR', 'UlnarStyloidR'],
              ['LateralEpicondyleR', 'RadialStyloidR'],
              ['LateralEpicondyleR', 'UlnarStyloidR'],
              ['OlecraneR', 'RadialStyloidR'],
              ['OlecraneR', 'UlnarStyloidR'],
              ['UlnarStyloidR', 'RadialStyloidR']]
}

ktk.Player(markers, interconnections=interconnections)

# %% Create the Arm local coordinate systems, following the ISB recommendations

# The origin is GH
origin = markers.data['AcromionR']  # approx GH

# Y axis = Elbow center to GH
y = (markers.data['AcromionR'] -
     0.5 * (
         markers.data['LateralEpicondyleR'] +
         markers.data['MedialEpicondyleR']
))

# X axis = normal to the GH-LE-ME plane, pointing forward
# Z axis normal to the XY plane, pointing approx from ME to LE
yz = markers.data['LateralEpicondyleR'] - markers.data['MedialEpicondyleR']

arm_lcs = ktk.geometry.create_frames(
    origin=origin, y=y, yz=yz
)

# - arm_lcs

# %% Create the Forearm local coordinate systems

# The origin is the US
origin = markers.data['UlnarStyloidR']

# Y axis = US to elbow center
y = (
    0.5 * (markers.data['LateralEpicondyleR'] +
           markers.data['MedialEpicondyleR'])
    - markers.data['UlnarStyloidR'])

# X axis = normal to the Elbow-US-RS plane, pointing forward
# Z axis normal to the XY plane, pointing approx from US to RS
yz = markers.data['RadialStyloidR'] - markers.data['UlnarStyloidR']

forearm_lcs = ktk.geometry.create_frames(
    origin=origin, y=y, yz=yz
)

# - forearm_lcs

# %% Create a TimeSeries for local coordinate systems

frames = ktk.TimeSeries(
    time=markers.time,
    data={
        'Arm': arm_lcs,
        'Forearm': forearm_lcs,
    })

# - ktk.Player(frames)
# - ktk.Player(markers, frames, interconnections=interconnections)

# %% Calculating angles

elbow_transform = ktk.geometry.get_local_coordinates(
    forearm_lcs, arm_lcs
)

euler = ktk.geometry.get_angles(elbow_transform, seq='ZXY', degrees=True)

# - angles

# %% Back to a TimeSeries

angles = ktk.TimeSeries(
    time=markers.time,
    data={
        'Flexion': euler[:, 0],
        'Pronation': euler[:, 2],
    }
)

angles.plot()

# %% With filtering

filtered_markers = ktk.filters.butter(markers, fc=15)

# Redo the processing with filtered markers
# Arm LCS
origin = filtered_markers.data['AcromionR']  # approx GH
y = (filtered_markers.data['AcromionR'] -
     0.5 * (
         filtered_markers.data['LateralEpicondyleR'] +
         filtered_markers.data['MedialEpicondyleR']
))
yz = (filtered_markers.data['LateralEpicondyleR']
      - filtered_markers.data['MedialEpicondyleR'])
arm_lcs = ktk.geometry.create_frames(
    origin=origin, y=y, yz=yz
)

# Forearm LCS
origin = filtered_markers.data['UlnarStyloidR']
y = (
    0.5 * (filtered_markers.data['LateralEpicondyleR'] +
           filtered_markers.data['MedialEpicondyleR'])
    - filtered_markers.data['UlnarStyloidR'])
yz = (filtered_markers.data['RadialStyloidR'] -
      filtered_markers.data['UlnarStyloidR'])
forearm_lcs = ktk.geometry.create_frames(
    origin=origin, y=y, yz=yz
)

# Transform and angles
elbow_transform = ktk.geometry.get_local_coordinates(
    forearm_lcs, arm_lcs
)
euler = ktk.geometry.get_angles(elbow_transform, seq='ZXY', degrees=True)
angles = ktk.TimeSeries(
    time=filtered_markers.time,
    data={
        'Flexion': euler[:, 0],
        'Pronation': euler[:, 2],
    }
)

angles.plot()

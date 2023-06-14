
# Extracting angles

Up to now, we learned how to create homogeneous transforms based on known angles, which is easily done using Kinetics Toolkit's [ktk.geometry.create_transforms](api/ktk.geometry.create_transforms.rst) function. In Biomechanics, it is often useful to do the inverse: calculating frames and transforms from measured kinematics (e.g., using markers or inertial measurement units), and then extracting joint angles from those transforms.

Unfortunately, extracting tridimensional angles from a given homogeneous transform is something that is notoriously difficult to understand, and that is often overlooked. Understanding how to communicate angles is very important, because similar angles can lead to completely different poses if the rotations are not performed in the same order, and around the same set of axes. This section will tackle this concept and will show how to work with 3d rotations, starting with 2d rotations.

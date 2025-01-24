# Local coordinate system

While points and vectors are generally relatively easy to express in a given coordinate system, the orientation of a segment is more complex. For instance, to express the orientation of the upper arm, we explicitly need this information:

- What is the initial, non-rotated orientation of the upper arm?
- By how many degrees has it been rotated from its initial orientation?
- Around which axes?
- In what order?

The first step to answer these questions is to create a **local coordinate system** for the upper arm. This local coordinate system will be attached to the upper arm, and thus will move with it. To create such a coordinate system, we need to define where is the origin and orthonormal axes of the upper arm, in respect to the upper arm. In this example, we use the anatomical position as a reference to define this coordinate system ({numref}`fig_geometry_local_coordinates`):

- The origin of the upper arm coordinate system is located at the shoulder;
- Its x axis points forward;
- Its y axis is aligned with the arm, pointing upward;
- Its z axis points to the right.

:::{figure-md} fig_geometry_local_coordinates
:width: 2in
![](_static/images/fig_geometry_local_coordinates.png)

Local coordinate system of the upper arm.
:::


Now that we defined this local coordinate system, we can come back to the position of interest of {numref}`fig_geometry_intro`. Look in {numref}`fig_geometry_local_coordinates_rotated` how the upper arm coordinate system is attached to the upper arm and thus moves with it.

:::{figure-md} fig_geometry_local_coordinates_rotated
:width: 3in
![](_static/images/fig_geometry_local_coordinates_rotated.png)

Expressing the position and orientation of the upper arm.
:::

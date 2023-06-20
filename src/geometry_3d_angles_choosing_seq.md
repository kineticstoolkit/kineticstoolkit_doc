# Choosing a rotation sequence

After reading this section, the normal reaction is to be confused about which sequence of rotations to choose to express specific joint angles. This is a very interesting topic that may never settle completely, but a good starting point is to consult the 2002 and 2005 recommendations of the International Society of Biomechanics:

- Wu, G., Siegler, S., Allard, P., Kirtley, C., Leardini, A., Rosenbaum, D., Whittle, M., D’Lima, D.D., Cristofolini, L., Witte, H., Schmid, O., Stokes, I., 2002. *ISB recommendation on definitions of joint coordinate system of various joints for the reporting of human joint motion—part I: ankle, hip, and spine.* Journal of Biomechanics 35, 543–548. [https://doi.org/10.1016/S0021-9290(01)00222-6](https://doi.org/10.1016/S0021-9290(01)00222-6)
- Wu, G., Van Der Helm, F.C.T., Veeger, H.E.J.D., Makhsous, M., Van Roy, P., Anglin, C., Nagels, J., Karduna, A.R., McQuade, K., Wang, X., Werner, F.W., Buchholz, B., Others, 2005. *ISB recommendation on definitions of joint coordinate systems of various joints for the reporting of human joint motion - Part II: shoulder, elbow, wrist and hand.* Journal of Biomechanics 38, 981–992. [https://doi.org/10.1016/j.jbiomech.2004.05.042](https://doi.org/10.1016/j.jbiomech.2004.05.042)

These papers propose standard ways to:

1. define most body segments' local coordinate systems based on bony landmarks;
2. define rotation sequences from a proximal segment to a distal segment to express joint angles.

Later in section [](kinematics_joint_angles.md), we will use the different Kinetics Toolkit's functions introduced in this section to calculate joint angles from skin markers by following these recommendations.

In any case, and as a main message for this section, we insist on the importance of communicating how angles were calculated in any scientific communication, since these angles are often much variable between different conventions.

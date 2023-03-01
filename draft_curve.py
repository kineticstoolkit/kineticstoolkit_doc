"""
Interactively draft a curve to build examples with nice-looking, fake curves.

Author: Félix Chénier
Date: 2023
"""

import matplotlib.pyplot as plt
import numpy as np
import limitedinteraction as li
import kineticstoolkit.lab as ktk


def ui_draft_curve(
    bounds: np.ndarray = np.array([0.0, 1.0, 0.0, 1.0])
) -> ktk.TimeSeries:
    """
    Interactively draft a curve.

    Parameters
    ----------
    bounds
        [xmin, xmax, ymin, ymax]

    Returns
    -------
    np.array
        A Nx2 array with x in first column, y in second column, with all data
        sorted along x.

    """
    li.message(
        "Draft a curve shape by clicking on the figure.\n"
        "Left-click: add a point\n"
        "Right-click: remove a point\n"
        "Middle-click: done.",
        right=10,
        top=10,
    )

    plt.figure()
    plt.plot(
        [
            float(bounds[0]),
            float(bounds[0]),
            float(bounds[1]),
            float(bounds[1]),
            float(bounds[0]),
        ],
        [
            float(bounds[2]),
            float(bounds[3]),
            float(bounds[3]),
            float(bounds[2]),
            float(bounds[2]),
        ],
        "y",
    )

    points = np.array(plt.ginput(n=1e6))
    li.message("")

    ts = ktk.TimeSeries(time=points[:, 0], data={"data": points[:, 1]})

    plt.close()

    return ts.resample(np.sort(ts.time))


if __name__ == "__main__":
    print(ui_draft_curve().data['data'])

# np.sort(points, axis=0)

# Kinetics Toolkit

*An Open-Source Python Package to Facilitate Research in Biomechanics*

```{div}
<a href="https://doi.org/10.21105/joss.03714"><img src="https://joss.theoj.org/papers/10.21105/joss.03714/status.svg" alt="JOSS"></a>
<a href="https://anaconda.org/conda-forge/kineticstoolkit"><img src="https://anaconda.org/conda-forge/kineticstoolkit/badges/version.svg" alt="Anaconda"></a>
<a href="https://anaconda.org/conda-forge/kineticstoolkit"><img src="https://anaconda.org/conda-forge/kineticstoolkit/badges/latest_release_date.svg" alt="Latest release"></a>
```


````{margin}
```{div}

<img src="_static/images/github-logo.png" alt="GitHub logo" width="20px"/>

<a href="https://github.com/orgs/kineticstoolkit/discussions/categories/announcements">
Announcements
</a>

<br/>

<img src="_static/images/github-logo.png" alt="GitHub logo" width="20px"/>

<a href="https://github.com/orgs/kineticstoolkit/discussions/categories/1-users-q-a">
Users Q&A
</a>

<br/>

<img src="_static/images/rss-icon.png" alt="RSS/Atom icon" width="20px"/>

<a href="https://kineticstoolkit.uqam.ca/announcements.atom">
RSS/Atom
</a>

<br/>

<img src="_static/images/linkedin-logo.png" alt="LinkedIn logo" width="20px"/>

<a href="https://www.linkedin.com/in/felixchenier/">
Félix Chénier
</a>

```
````


![](_static/images/frontpage.gif)


Kinetics Toolkit is an open-source Python package to facilitate research in biomechanics. It provides tools for:
- [Analyzing timeseries](timeseries.md), including [data](timeseries_data_management.md), [time](timeseries_time_management.md) and [event](timeseries_event_management.md) management, [time-domain and frequency-domain noise filtering](filters.md), and [cycle management](cycles.md);
- [Managing files](files.md), including reading/writing C3D, CSV and any file supported by {{pandas}};
- [Performing rigid body geometry operations](geometry.md), including manipulation of series of [points, vectors](geometry_points_vectors.md), [frames](geometry_frames.md) and [homogeneous transforms](geometry_transform_moving_coordinates.md), [coordinate system changes](geometry_transform_changing_coordinate_system.md), and [3D angle extraction](geometry_angles.md);
- [Visualizing 3D points and frames interactively](player.md);
- [Performing kinematic operations](kinematics.md) such as reconstructing [occluded](kinematics_reconstructing_occluded_markers.md), [removed](kinematics_reconstructing_removed_markers.md) or [probed](kinematics_reconstructing_probed_points.md) markers;
- And more using [extensions](extensions.md).

It is a programming library, and programming can be hard for new users. Therefore, we also provide the free, electronic book [Biomechanical Analysis using Python and Kinetics Toolkit](getting_started_intro.md), which guides new programmers from the basics to advanced, generic 3D biomechanical analysis. This book covers:
- [The Python programming language](python_intro.md), including [arithmetics](python_arithmetics.md), [variables](python_variables.md), [numbers](python_numbers.md), [strings](python_strings.md), [functions](python_functions.md), [conditions](python_conditions.md), [lists](python_lists.md), [loops](python_looping.md) and [dictionaries](python_dicts.md);
- [Matplotlib](matplotlib.md), to generate print-quality graphics and to analyze curves interactively;
- [NumPy](numpy.md) basics, including [n-dimensional arrays](numpy_ndarray.md), [arithmetics](numpy_arithmetics.md), [trigonometry](numpy_trigonometry.md), [infinity/nan](numpy_inf_nan.md), [statistical functions](numpy_statistics.md), [comparisons](numpy_comparisons.md), [logical operators](numpy_logical_operators.md), [indexing, slicing](numpy_indexing_slicing_1d.md) and [filtering arrays](numpy_filtering_nd.md).

It also covers all the features of Kinetics Toolkit, with reproducible examples based on real, downloadable data.





```{div} style="align:center;"
<a href="https://felixchenier.uqam.ca"><img width=30% src="_static/images/logo_mosa.png"></a>
&nbsp;&nbsp;&nbsp;<a href="https://uqam.ca"><img width=20% src="_static/images/logo_uqam.png"></a>
&nbsp;&nbsp;&nbsp;<a href="https://crir.ca"><img width=20% src="_static/images/logo_crir.jpg"></a>
```

# Kinetics Toolkit

::::{grid}
:gutter: 2

:::{grid-item-card} 
**is a free online resource** for students and researchers to learn about 3D biomechanical data processing using Python.

- [](getting_started.md)
- [](python_for_biomechanics.md)
- [](kineticstoolkit.md)
:::

:::{grid-item-card}
**is an open-source Python package** to analyze biomechanical data with the users knowing what they are doing. No magical black box.

- [](timeseries.md)
- [](files.md)
- [](geometry.md)
- [](kinematics.md)
:::

::::


::::{grid}
:::{grid-item}
```
import kineticstoolkit.lab as ktk
markers = ktk.read_c3d("filename.c3d")["Points"]
ktk.Player(markers, interconnections=interconnections)
```



[![example_result](_static/images/frontpage.gif)](kinematics_load_visualize.md)
[Click here for a complete tutorials on marker visualization](kinematics_load_visualize.md)
:::

:::{grid-item}

```{div}
<div style="max-height:900px">

<div align="left">
<a href="https://doi.org/10.21105/joss.03714"><img src="https://joss.theoj.org/papers/10.21105/joss.03714/status.svg" alt="JOSS"></a>
<a href="https://anaconda.org/conda-forge/kineticstoolkit"><img src="https://anaconda.org/conda-forge/kineticstoolkit/badges/version.svg" alt="Anaconda"></a>
<a href="https://anaconda.org/conda-forge/kineticstoolkit"><img src="https://anaconda.org/conda-forge/kineticstoolkit/badges/latest_release_date.svg" alt="Latest release"></a>
</div>

<h3>
<a href="https://github.com/felixchenier/kineticstoolkit/discussions">Announcements <img src="_static/images/github-logo.png" alt="Follow on GitHub" width="20px"></a>
<a href="https://github.com/felixchenier/kineticstoolkit/discussions/categories/announcements.atom"><img src="_static/images/rss-icon.png" alt="Subscribe to RSS/Atom Feed" width="20px"></a>
<a href="https://twitter.com/KineticsToolkit"><img src="_static/images/twitter-logo.png" alt="Follow on Twitter" width="20px"></a>
</h3>
<?php include("/home/kinetics/public_html/rss/rss.php");?>
</div>
<link rel="alternate" type="application/rss+html" title="Subscribe to Kinetics Toolkit Announcements" href="https://github.com/felixchenier/kineticstoolkit/discussions/categories/announcements.atom" />
```

:::
::::

[Questions, suggestions, discussions and collaborations](https://github.com/felixchenier/kineticstoolkit/discussions) are highly welcome. Please see the numerous ways you can [contribute](dev_contributing.md) to this project.

-----------

<div align="center">
<a href="https://felixchenier.uqam.ca"><img alt="-width:narrow" src="_static/images/logo_mosa.png"></a>
&nbsp;&nbsp;&nbsp;<a href="https://uqam.ca"><img alt="-width:narrower" src="_static/images/logo_uqam.png"></a>
&nbsp;&nbsp;&nbsp;<a href="https://crir.ca"><img alt="-width:narrower" src="_static/images/logo_crir.jpg"></a>
</div>

# Table of contents
####### This pseudo-markdown file will be converted to `_toc.yml` during building.

format: jb-book
root: [](index.md)
parts:

  ## Manual
  - caption: "Manual"
    chapters:

      ### Getting started
      - file: [](getting_started_ktk.md)
        sections:
          - file: [](what_is_kinetics_toolkit.md)
          - file: [](getting_started_with_python.md)
          - file: [](installing_kinetics_toolkit.md)

      ### Tutorials
      - file: [](tutorials.md)
        sections:
          #### TimeSeries
          - file: [](timeseries.md)
            sections:
              - file: [](timeseries_basics.md)
              - file: [](timeseries_manipulating.md)
              - file: [](timeseries_dataframes.md)
          #### Load/Save
          - file: [](loadsave.md)
          #### Filters
          - file: [](filters.md)
            sections:
              - file: [](filters_butter.md)
              - file: [](filters_smooth.md)
              - file: [](filters_savgol.md)
              - file: [](filters_median.md)
          #### Cycles
          - file: [](cycles.md)
          #### Geometry
          - file: [](geometry.md)
            sections:
              - file: [](geometry_basics.md)
              - file: [](geometry_dimension_conventions.md)
          #### Kinematics
          - file: [](kinematics.md)
            sections:
              - file: [](kinematics_load_visualize.md)
              - file: [](kinematics_joint_angles.md)
              - file: [](kinematics_reconstructing_occluded_markers.md)
              - file: [](kinematics_reconstructing_removed_markers.md)
              - file: [](kinematics_reconstructing_probed_points.md)
          #### Wheelchair kinetics
          - file: [](pushrimkinetics.md)
          - file: [](ktk_conventions.md)

      ### In depth
      - file: [](ktk_in_depth.md)
        sections:
          - file: [](ktk_lab_mode.md)
          - file: [](ktk_release_notes.md)
          - file: [](python_learning.md)

  ## API Reference
  - caption: "API Reference"
    chapters:
      - file: [](99_api_reference/01_classes.md)
      - file: [](99_api_reference/02_functions.md)
      - file: [](99_api_reference/03_modules.md)

  ## Links
  - caption: "Links"
    chapters:
      - url: https://github.com/felixchenier/kineticstoolkit
        title: GitHub repository

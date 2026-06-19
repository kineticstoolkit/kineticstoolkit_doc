version: 1
project:
  title: Kinetics Toolkit
  copyright: Félix Chénier, 2020-2026
  github: kineticstoolkit/kineticstoolkit_doc
  authors:
    Félix Chénier
  exports:
    - format: pdf
      template: plain_latex_book
      output: exports/book.pdf
    - format: tex
      template: plain_latex_book
      output: exports/book.tex
  numbering:
    title: false
    figure:
      continue: true
  plugins:
    - https://github.com/myst-contrib/myst-substitutions/releases/download/v0.1/index.mjs
  substitutions:
    matplotlib: "[Matplotlib](https://matplotlib.org)"
    pyplot: "[pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)"
    plt_plot: "[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)"
    plt_scatter: "[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)"
    plt_fill_between: "[plt.fill_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html)"
    plt_imshow: "[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)"
    plt_errorbar: "[plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)"
    plt_bar: "[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)"
    plt_show: "[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)"
    plt_xlabel: "[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)"
    plt_ylabel: "[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)"
    plt_title: "[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)"
    plt_legend: "[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)"
    plt_subplot: "[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)"
    plt_tight_layout: "[plt.tight_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html)"
    plt_figure: "[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html)"
    plt_clf: "[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html)"
    plt_axis: "[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html)"
    plt_grid: "[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)"
    plt_ginput: "[plt.ginput](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html)"

    numpy: "[NumPy](https://numpy.org)"
    np_array: "[np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)"
    np_ones: "[np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)"
    np_zeros: "[np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)"
    np_nonzero: "[np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)"
    np_arange: "[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)"
    np_linspace: "[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)"
    np_ix_: "[np.ix_](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html)"
    np_broadcasting: "[broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)"
    np_sin: "[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html)"
    np_cos: "[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html)"
    np_tan: "[np.tan](https://numpy.org/doc/stable/reference/generated/numpy.tan.html)"
    np_arcsin: "[np.arcsin](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html)"
    np_arccos: "[np.arccos](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html)"
    np_arctan: "[np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html)"
    np_arctan2: "[np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html)"
    np_sqrt: "[np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html)"
    np_abs: "[np.abs](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html)"
    np_rad2deg: "[np.rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html)"
    np_deg2rad: "[np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html)"
    np_pi: "[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi)"
    np_nan: "[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan)"
    np_inf: "[np.inf](https://numpy.org/doc/stable/reference/constants.html#numpy.inf)"
    np_isnan: "[np.isnan](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)"
    np_isinf: "[np.isinf](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html)"
    np_sum: "[np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)"
    np_mean: "[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)"
    np_min: "[np.min](https://numpy.org/doc/stable/reference/generated/numpy.amin.html)"
    np_max: "[np.max](https://numpy.org/doc/stable/reference/generated/numpy.amax.html)"
    np_std: "[np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html)"
    np_median: "[np.median](https://numpy.org/doc/stable/reference/generated/numpy.median.html)"
    np_quantile: "[np.quantile](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html)"
    np_nansum: "[np.nansum](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html)"
    np_nanmean: "[np.nanmean](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html)"
    np_nanmin: "[np.nanmin](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html)"
    np_nanmax: "[np.nanmax](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html)"
    np_nanstd: "[np.nanstd](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html)"
    np_nanmedian: "[np.nanmedian](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html)"
    np_nanquantile: "[np.nanquantile](https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html)"
    np_newaxis: "[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis)"

    ndarray: "[ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)"
    ndarray_shape: "[shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)"
    ndarray_tolist: "[tolist](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html)"
    ndarray_copy: "[copy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html)"

    pandas: "[Pandas](https://pandas.pydata.org/)"
    pd_dataframe: "[DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)"
    pd_read_csv: "[pd.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)"
    dataframe_to_csv: "[to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)"

    ezc3d: "[ezc3d](https://github.com/pyomeca/ezc3d)"
  toc:
    - file: [](index.md)
    - file: [](title.md)
    - title: Part I. Getting Started
      children:
        - file: [](getting_started_intro.md)
        - file: [](getting_started.md)
          children:
            - file: [](getting_started_installing.md)
            - file: [](getting_started_configuring_spyder.md)
            - file: [](getting_started_using_spyder.md)
    - title: Part II. Learning Python for Biomechanics
      children:
        - file: [](python_intro.md)
          children:
            - file: [](python_basics.md)
              children:
                - file: [](python_arithmetics.md)
                - file: [](python_print.md)
                - file: [](python_comments.md)
                - file: [](python_variables.md)
                - file: [](python_basics_exercise1.md)
                - file: [](python_basics_exercise2.md)
            - file: [](python_numbers.md)
              children:
                - file: [](python_int_float.md)
                - file: [](python_int_float_exercise.md)
                - file: [](python_int_float_arithmetics.md)
            - file: [](python_strings.md)
              children:
                - file: [](python_strings_quotes.md)
                - file: [](python_strings_backslash.md)
                - file: [](python_strings_triple_quotes.md)
                - file: [](python_strings_long_strings.md)
                - file: [](python_strings_fstrings.md)
                - file: [](python_strings_exercise.md)
                - file: [](python_strings_input.md)
            - file: [](python_functions.md)
              children:
                - file: [](python_functions_syntax.md)
                - file: [](python_functions_arguments.md)
                - file: [](python_functions_arguments_exercise.md)
                - file: [](python_functions_return.md)
                - file: [](python_functions_return_exercise1.md)
                - file: [](python_functions_return_exercise2.md)
                - file: [](python_functions_docstrings.md)
                - file: [](python_functions_type_annotations.md)
                - file: [](python_functions_positional_keywords.md)
                - file: [](python_functions_default_values.md)
                - file: [](python_functions_default_values_exercise.md)
            - file: [](python_conditions.md)
              children:
                - file: [](python_conditions_boolean.md)
                - file: [](python_conditions_if_elif_else.md)
                - file: [](python_conditions_if_elif_else_exercise.md)
                - file: [](python_conditions_logical_operators.md)
                - file: [](python_conditions_logical_operators_exercise.md)
            - file: [](python_lists.md)
              children:
                - file: [](python_lists_creating.md)
                - file: [](python_lists_indexing.md)
                - file: [](python_lists_indexing_exercise1.md)
                - file: [](python_lists_indexing_exercise2.md)
                - file: [](python_lists_slicing.md)
                - file: [](python_lists_slicing_exercise1.md)
                - file: [](python_lists_slicing_exercise2.md)
                - file: [](python_strings_slicing.md)
                - file: [](python_lists_modify.md)
                - file: [](python_lists_modify_exercise1.md)
                - file: [](python_lists_modify_exercise2.md)
            - file: [](python_looping.md)
              children:
                - file: [](python_while.md)
                - file: [](python_while_exercise1.md)
                - file: [](python_while_exercise2.md)
                - file: [](python_while_exercise3.md)
                - file: [](python_for.md)
                - file: [](python_for_exercise.md)
                - file: [](python_for_range.md)
                - file: [](python_for_range_exercise1.md)
                - file: [](python_for_range_exercise2.md)
                - file: [](python_for_range_exercise3.md)
                - file: [](python_for_range_exercise4.md)
                - file: [](python_for_writing_list.md)
                - file: [](python_for_enumerate.md)
            - file: [](python_dicts.md)
              children:
                - file: [](python_dicts_creating_accessing.md)
                - file: [](python_dicts_creating_accessing_exercise1.md)
                - file: [](python_dicts_creating_accessing_exercise2.md)
                - file: [](python_dicts_creating_accessing_exercise3.md)
                - file: [](python_dicts_modifying.md)
                - file: [](python_dicts_modifying_exercise.md)
                - file: [](python_dicts_looping.md)
                - file: [](python_dicts_looping_exercise.md)
            - file: [](python_exercises.md)
        - file: [](matplotlib.md)
          children:
            - file: [](matplotlib_import.md)
            - file: [](matplotlib_plot.md)
            - file: [](matplotlib_plot_multiple.md)
            - file: [](matplotlib_titles_labels.md)
            - file: [](matplotlib_plot_titles_labels_exercise1.md)
            - file: [](matplotlib_plot_titles_labels_exercise2.md)
            - file: [](matplotlib_subplot.md)
            - file: [](matplotlib_style.md)
            - file: [](matplotlib_style_exercise.md)
            - file: [](matplotlib_axis.md)
            - file: [](matplotlib_ginput.md)
            - file: [](matplotlib_ginput_exercise.md)
            - file: [](matplotlib_exercises.md)
        - file: [](numpy.md)
          children:
            - file: [](numpy_import.md)
            - file: [](numpy_ndarray.md)
              children:
                - file: [](numpy_ndarray_introduction.md)
                - file: [](numpy_ndarray_dimensions.md)
                - file: [](numpy_ndarray_creating_from_lists.md)
                - file: [](numpy_ndarray_creating_zeros_ones.md)
                - file: [](numpy_ndarray_creating_zeros_ones_exercise1.md)
                - file: [](numpy_ndarray_creating_zeros_ones_exercise2.md)
                - file: [](numpy_ndarray_creating_linspace.md)
                - file: [](numpy_ndarray_creating_linspace_exercise.md)
            - file: [](numpy_arithmetics.md)
            - file: [](numpy_arithmetics_exercise.md)
            - file: [](numpy_matmul.md)
            - file: [](numpy_trigonometry.md)
            - file: [](numpy_trigonometry_exercise1.md)
            - file: [](numpy_trigonometry_exercise2.md)
            - file: [](numpy_inf_nan.md)
            - file: [](numpy_statistics.md)
            - file: [](numpy_statistics_exercise.md)
            - file: [](numpy_comparisons.md)
            - file: [](numpy_comparisons_exercise.md)
            - file: [](numpy_logical_operators.md)
            - file: [](numpy_indexing_slicing_1d.md)
            - file: [](numpy_indexing_slicing_1d_exercise.md)
            - file: [](numpy_filtering_1d.md)
            - file: [](numpy_indexing_slicing_filtering_1d_exercise1.md)
            - file: [](numpy_indexing_slicing_filtering_1d_exercise2.md)
            - file: [](numpy_indexing_slicing_filtering_1d_exercise3.md)
            - file: [](numpy_nd.md)
              children:
                - file: [](numpy_indexing_nd.md)
                - file: [](numpy_slicing_nd.md)
                - file: [](numpy_filtering_nd.md)
                - file: [](numpy_filtering_nd_exercise.md)
            - file: [](numpy_exercises.md)
    - title: Part III. Going further with Kinetics Toolkit
      children:
        - file: [](ktk_importing.md)
        - file: [](timeseries.md)
          children:
            - file: [](timeseries_basics.md)
              children:
                - file: [](timeseries_basics_exercise.md)
            - file: [](timeseries_manipulating.md)
              children:
                - file: [](timeseries_converting_copy.md)
                - file: [](timeseries_data_management.md)
                - file: [](timeseries_time_management.md)
                - file: [](timeseries_event_management.md)
                - file: [](timeseries_indexing.md)
                  children:
                    - file: [](timeseries_indexing_exercise.md)
                - file: [](timeseries_segmenting.md)
                  children:
                    - file: [](timeseries_segmenting_exercise.md)
                - file: [](timeseries_missing_data.md)
            - file: [](filters.md)
              children:
                - file: [](filters_butter.md)
                  children:
                    - file: [](filters_butter_exercise.md)
                - file: [](filters_smooth_savgol.md)
                - file: [](filters_median.md)
            - file: [](cycles.md)
            - file: [](timeseries_exercises.md)
        - file: [](files.md)
          children:
            - file: [](files_read_c3d.md)
            - file: [](files_write_c3d.md)
            - file: [](files_read_csv.md)
            - file: [](files_write_csv.md)
            - file: [](files_loadsave.md)
        - file: [](geometry.md)
          children:
            - file: [](geometry_basics.md)
              children:
                - file: [](geometry_global_coordinates.md)
                - file: [](geometry_points_vectors.md)
                - file: [](geometry_local_coordinates.md)
                - file: [](geometry_transforms.md)
                  children:
                    - file: [](geometry_basics_exercise.md)
            - file: [](geometry_dimension_conventions.md)
              children:
                - file: [](geometry_creating_point_series.md)
                - file: [](geometry_creating_vector_series.md)
                - file: [](geometry_creating_transform_series.md)
                - file: [](geometry_dimension_conventions_exercise1.md)
                - file: [](geometry_dimension_conventions_exercise2.md)
                - file: [](geometry_dimension_conventions_exercise3.md)
            - file: [](geometry_transform_moving_coordinates.md)
              children:
                - file: [](geometry_transform_moving_points.md)
                - file: [](geometry_transform_rotating_vectors.md)
                - file: [](geometry_transform_moving_frames.md)
                  children:
                    - file: [](geometry_moving_coordinates_exercise1.md)
                    - file: [](geometry_moving_coordinates_exercise2.md)
                    - file: [](geometry_moving_coordinates_exercise3.md)
            - file: [](geometry_transform_changing_coordinate_system.md)
              children:
                - file: [](geometry_transform_local_to_global_coordinates.md)
                - file: [](geometry_transform_global_to_local_coordinates.md)
                - file: [](geometry_transform_changing_coordinate_system_example.md)
            - file: [](geometry_kinematic_chains.md)
            - file: [](geometry_angles.md)
              children:
                - file: [](geometry_2d_angles.md)
                - file: [](geometry_3d_angles.md)
                - file: [](geometry_3d_angles_ktk.md)
                - file: [](geometry_3d_angles_choosing_seq.md)
            - file: [](geometry_exercises.md)
        - file: [](player.md)
          children:
            - file: [](player_basics.md)
            - file: [](player_interconnections.md)
            - file: [](player_frames.md)
            - file: [](player_vectors.md)
            - file: [](player_styling_exporting.md)
        - file: [](kinematics.md)
          children:
            - file: [](kinematics_joint_angles.md)
            - file: [](kinematics_reconstructing_occluded_markers.md)
            - file: [](kinematics_reconstructing_removed_markers.md)
            - file: [](kinematics_reconstructing_probed_points.md)
    - title: Appendix
      children:
        - file: [](datasets.md)
          children:
            - file: [](dataset_kinematics_tennis_serve.md)
            - file: [](dataset_kinetics_wheelchair_propulsion.md)
            - file: [](dataset_emg.md)
        - file: [](ktk_citing.md)
        - file: [](dev_contributors.md)
          children:
            - file: [](dev_rules.md)
            - file: [](dev_code_of_conduct.md)
            - file: [](dev_installing_from_github.md)
            - file: [](dev_coding_style.md)
    - title: API Reference
      children:
        - file: [](ktk_conventions.md
        - file: [](extensions.md)
        - url: https://github.com/felixchenier/kineticstoolkit
          title: GitHub repository

site:
  nav:
    - title: Reference Book
      url: /index
    - title: Kinetics Toolkit API
      url: https://kineticstoolkit.uqam.ca/docs/api
    - title: GitHub
      url: https://github.com/kineticstoolkit
  options:
    analytics_google: ''
    hide_authors: true
    folders: true
    style: _static/css/style.css
    logo: _static/logo.png

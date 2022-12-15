# 📖 An overview of Kinetics Toolkit

Kinetics Toolkit is designed to play well with other softwares and packages, to be used as an addition and not as a replacement to existing workflows. Most of the data processing is done via the [](api/ktk.TimeSeries.rst) class, which is a container for time (`np.array`), data (`dict[np.array]`), events and metadata. This [tutorial](timeseries.md) on TimeSeries will help to understand this class and its associated methods.

## 📄 Getting your data in

(orange in figure below)

Kinetics Toolkit does not ties to specific instruments. Using your recording instrumentation, you need to get your data in a compatible file, be it very generic such as `csv` or `txt` files, or more specialized such as `c3d`.

Any data that can be read as a pandas DataFrame (e.g., `csv`, `txt`, Excel, SQL) can be converted to a TimeSeries using [](api/ktk.TimeSeries.from_dataframe.rst). This [tutorial](timeseries_dataframes.md) shows an example. To import motion data from a `c3d` file, use the [](api/ktk.read_c3d.rst) function.

In addition to importing and exporting, Kinetics Toolkit offers [](api/ktk.load.rst) and [](api/ktk.save.rst) functions, which store standard python types, numpy arrays, basic pandas DataFrames and Series, and kineticstoolkit TimeSeries in a portable zipped `json` format. See this [tutorial](loadsave.md) for more information.

![Kinetics Toolkit dataflow -width:full](_static/images/ktk_dataflow.png)

## 📄 Processing and visualizing your data

(blue in figure above)

Once your data are read as TimeSeries, you can use:

- the [TimeSeries methods](api/ktk.TimeSeries.rst) to add and edit events, to sync, split, subset, merge, resample TimeSeries, etc. ([tutorials](timeseries.md))
- the [filters](api/ktk.filters.rst) module to filter data using butterworth filters, smoothing filters, deriving filters, etc. ([tutorials](filters.md));
- the [cycles](api/ktk.cycles.rst) module to detect, time-normalize, combine cycles, find most repeatable cycles, etc. ([tutorials](cycles.md));
- the [geometry](api/ktk.geometry.rst) module to create rigid transforms, frames, convert between local and global coordinates, extract angles, etc. ([tutorials](geometry.md));
- the [kinematics](api/ktk.kinematics.rst) module to create and track marker clusters, reconstruct virtual markers, etc. ([tutorials](kinematics.md));
- the [Player](api/ktk.Player.rst) class to visualize animated, interconnected markers and frames in an interactive 3D environment ([tutorial](kinematics_load_visualize.md));
- the [TimeSeries.plot](api/ktk.TimeSeries.plot.rst) method to plot 2D graphes of your TimeSeries contents, including the events.

If applicable, you can also use your current functions:

- that use numpy arrays: by working directly on the TimeSeries' `data` attribute;
- that use pandas DataFrames: using [](api/ktk.TimeSeries.from_dataframe.rst) and [](api/ktk.TimeSeries.to_dataframe.rst).

## 📄 Getting your data out

(red in figure above)

Once your data are processed, you can export it to other formats to process it further with other software, using a similar method that you took to import those in a first place: use [](api/ktk.write_c3d.rst) for `c3d`, or pandas' `to_` methods for saving `csv`, `txt`, Excel, etc., via the [](api/ktk.TimeSeries.to_dataframe.rst) method. You can also save your variables using [](api/ktk.save.rst) for short-term to long-term storage.

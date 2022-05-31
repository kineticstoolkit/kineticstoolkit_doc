# Integrating Kinetics Toolkit in your workflow

{{ incomplete }}

Kinetics Toolkit is designed to play well with other softwares and packages, to be used as an addition and not as a replacement to existing workflows. Most of the processing is done via the [TimeSeries](api/kineticstoolkit.TimeSeries.rst) class, which is simply a container time and data expressed as numpy ndarrays. This [tutorial](timeseries.md) on TimeSeries will help to understand this class and its associated methods.

This page shows how to import instrumentation data to a TimeSeries, how to work with other data processing softwares, and how to work with other python packages.

## Instrumentation and other data processing software

Kinetics Toolkit does not ties to specific instruments. Using your recording instrumentation, you need to get your data in a compatible file, be it very generic such as csv or txt files, or more specialized such as c3d.

To import tabular data such as csv, txt or Excel files, you will first use the [Pandas](https://pandas.pydata.org/) package to open the data in a DataFrame format. Then, you can import the DataFrame as a TimeSeries using [TimeSeries.from_dataframe()](api/kineticstoolkit.TimeSeries.from_dataframe.rst). This [tutorial](timeseries_dataframes.md) shows such an example.

To import motion data from a c3d or n3d file, you will directly use the [ktk.kinematics.read_c3d_file()](api/kineticstoolkit.kinematics.read_c3d_file.rst) or [ktk.kinematics.read_n3d_file()](api/kineticstoolkit.kinematics.read_n3d_file.rst) function, which automatically creates a TimeSeries.

:::{note}
To use [ktk.kinematics.read_c3d_file()](api/kineticstoolkit.kinematics.read_c3d_file.rst), you must have installed Kinetics Toolkit from conda-forge, or installed the [ezc3d](https://github.com/pyomeca/ezc3d) package manually (this package is not available via pip).
:::

You can also export TimeSeries to these file formats, using similar methods. These import/export methods also make it possible to integrate Kinetics Toolkit with other data processing software.

In addition to importing and exporting, Kinetics Toolkit offer [ktk.load()](api/kineticstoolkit.load.rst) and [ktk.save()](api/kineticstoolkit.save.rst) functions that store every standard python types, numpy's ndarray, pandas's DataFrame and Series, and ktk's TimeSeries, in a portable zipped JSON format. See this [tutorial](loadsave.md) for more information on these functions.

The figure belows is a data flow summary of the import, export, load and save methods to transfer data between different file formats.


```{mermaid}
flowchart TB

classDef default fill:#fff, stroke:#aaa, text-align:left;
classDef top_level fill:#fff, stroke:#aaa, stroke-width:2px;
classDef no_outline fill:#fff, stroke-width:0px;
classDef kineticstoolkit fill:#96cdea, stroke:#000;
classDef junction fill:#777, stroke-width:1px, stroke:#000;

%% ----------------------------------------
%% BLOCKS

instruments[Instruments]:::no_outline
software1[Other data processing software]:::no_outline

subgraph graph_allfiles1[ ]
    subgraph graph_files1[Common files]
        csv1[(csv)]
        txt1[(txt)]
        excel1[(Excel)]
        c3d1[(c3d)]
        n3d1[(n3d)]
    end
    
    subgraph graph_ktkzip1[Previously saved data]
        ktkzip1[(ktk.zip)]:::kineticstoolkit
    end
end
class graph_allfiles1 no_outline

subgraph graph_importing_loading[ ]
    subgraph graph_importing[Importing data]
        pandas_read["
            Pandas' read functions:
            - pd.read_csv()
            - pd.read_excel()
            - etc."]
            
        subgraph graph_ktk_read[ ]
            ktk_import_dataframe["ktk.TimeSeries.from_dataframe()"]:::kineticstoolkit
            ktk_read["
                ktk's read functions:
                - ktk.kinematics.read_c3d()
                - ktk.kinematics.read_n3d()
                "]:::kineticstoolkit
        end
        class graph_ktk_read no_outline
        
        node_timeseries1(( )):::junction

    end

    subgraph graph_loading[Loading data]
        ktk_load["ktk.load()"]:::kineticstoolkit
    end

end
class graph_importing_loading no_outline

subgraph graph_data[ ]
    data[Working variables]
end
class graph_data no_outline
class data no_outline


subgraph graph_exporting_saving[ ]
    subgraph graph_exporting[Exporting data]
    
        node_timeseries2(( )):::junction
    
        ktk_export_dataframe["ktk.TimeSeries.to_dataframe()"]:::kineticstoolkit        
        pandas_write["
            Pandas' write functions:
            - pd.write_csv()
            - pd.write_excel()
            - etc."]
        ktk_write["ktk.kinematics.write_c3d()"]:::kineticstoolkit
    end
    
    subgraph graph_saving[Saving data]
        ktk_save["ktk.save()"]:::kineticstoolkit    
    end

end
class graph_exporting_saving no_outline

subgraph graph_allfiles2[ ]

    subgraph graph_files2[Common files]
        csv2[(csv)]
        txt2[(txt)]
        excel2[(Excel)]
        c3d2[(c3d)]
    end

    ktkzip2[(ktk.zip)]:::kineticstoolkit

end
class graph_allfiles2 no_outline

software2[Other data processing software]:::no_outline



%% ----------------------------------------
%% CONNECTIONS


instruments --> node_graph_files1(( )):::junction --> graph_files1
software1 --> node_graph_files1
pandas_read -- DataFrame --> ktk_import_dataframe
csv1 -- file --> pandas_read
txt1 -- file --> pandas_read
excel1 -- file --> pandas_read
c3d1 -- file --> ktk_read
n3d1 -- file --> ktk_read
ktkzip1 -- file --> ktk_load
ktk_import_dataframe --- node_timeseries1
ktk_read --- node_timeseries1
node_timeseries1 -- TimeSeries --> data
ktk_load -- Python types\nndarray\nSeries\nDataFrame\nTimeSeries --> data
data -- TimeSeries --- node_timeseries2
node_timeseries2 --> ktk_export_dataframe
node_timeseries2 --> ktk_write
data -- Python types\nndarray\nSeries\nDataFrame\nTimeSeries --> ktk_save
ktk_export_dataframe -- DataFrame --> pandas_write
pandas_write -- file --> csv2
pandas_write -- file --> txt2
pandas_write -- file --> excel2
ktk_write -- file --> c3d2
ktk_save -- file --> ktkzip2
graph_files2 --> software2

```

## Integration with other Python packages



```{mermaid}
flowchart LR

classDef default fill:#fff, stroke:#aaa, text-align:left;
classDef top_level fill:#fff, stroke:#aaa, stroke-width:2px;
classDef no_outline fill:#fff, stroke-width:0px;
classDef kineticstoolkit fill:#96cdea, stroke:#000;
classDef junction fill:#777, stroke-width:1px, stroke:#000;

%% ----------------------------------------
%% BLOCKS

subgraph graph_processing_timeseries[Processing TimeSeries directly]
    direction LR

    filters["
        Filtering:
        - ktk.filters.butter()
        - ktk.filters.smooth()
        - ktk.filters.deriv()
        - etc.
    "]:::kineticstoolkit
    
    timeseries["
        TimeSeries operations:
        - TimeSeries.add_event()
        - TimeSeries.merge()
        - TimeSeries.get_subset()
        - TimeSeries.get_ts_before_event()
        - TimeSeries.get_ts_after_event()
        - TimeSeries.get_ts_between_events()
        - TimeSeries.ui_sync()
        - TimeSeries.ui_edit()
        - etc.
    "]:::kineticstoolkit
    
    cycles["
        Cycles:
        - ktk.cycles.detect_cycles()
        - ktk.cycles.time_normalize()
        - etc.
    "]:::kineticstoolkit
    
    kinematics["
        Kinematics:
        - ktk.kinematics.create_cluster()
        - ktk.kinematics.extend_cluster()
        - ktk.kinematics.track_cluster()
        - etc.
    "]:::kineticstoolkit
    
    subgraph graph_processing_pandas[Any operation on pandas' DataFrame via:]
        to_from_dataframe["
            - ktk.TimeSeries.to_dataframe()
            - ktk.TimeSeries.from_dataframe()"]:::kineticstoolkit
    end
    
end

subgraph graph_processing_timeseries_data[Processing TimeSeries' data attribute]
    direction LR

    geometry["
        Geometrical operations:
        - ktk.geometry.create_frames()
        - ktk.geometry.get_local_coordinates()
        - ktk.geometry.get_global_coordinates()
        - ktk.geometry.get_angles()
        - etc.
    "]:::kineticstoolkit
    
    processing_ndarray["
        Any operation on numpy's ndarray:
        - numpy
        - scipy
        - lots of other packages
    "]
    
end

data[Working variables]:::no_outline

subgraph graph_visualizing[Visualizing data]
direction LR

    subgraph graph_visualizing_timeseries[Visualizing TimeSeries directly]
        direction LR
        
        visualize_plot["
            Plot with events
            using Matplotlib:
            - ktk.TimeSeries.plot()
        "]:::kineticstoolkit

        visualize_player["
            Interconnected markers
            in 3D viewer:
            - ktk.Player
        "]:::kineticstoolkit
    end
    
    subgraph graph_visualizing_timeseries_data[Visualizing TimeSeries' data attribute]
        direction LR

        visualize_matplotlib["
            Plot using Matplotlib:
            - plt.plot()
            - plt.fill_between()
            - etc.
        "]

        visualize_other["
            Visualize ndarray
            using other packages:
            - plotly
            - bokeh
            - etc.
        "]
    end

end


%% ----------------------------------------
%% CONNECTIONS

graph_processing_timeseries -- TimeSeries <--> data

graph_processing_timeseries_data -- "
    TimeSeries.data
    (ndarray)
    " <--> data

data -- TimeSeries --> graph_visualizing_timeseries

data -- "
    TimeSeries.data
    (ndarray)
    " --> graph_visualizing_timeseries_data

```
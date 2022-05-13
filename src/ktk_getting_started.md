# Getting started

% 🟡

```{mermaid}
flowchart TB

classDef default fill:#fff, stroke:#aaa, text-align:left;
classDef top_level fill:#fff, stroke:#aaa, stroke-width:2px;
classDef no_outline fill:#fff, stroke-width:0px;
classDef kineticstoolkit fill:#aaffaa;

recording[["Recording and loading data"]] --> data

data[(Data)]

data <--> processing[["Processing data"]]
data <--> visualizing[["Visualizing data"]]
data --> saving[["Saving and exporting data"]]

click recording "#recording-and-loading-data"
click processing "#processing-data"
click visualizing "#visualizing-data"
click saving "#saving-and-exporting-data"

```

## Recording and loading data

```{mermaid}
flowchart TB

classDef default fill:#fff, stroke:#aaa, text-align:left;
classDef top_level fill:#fff, stroke:#aaa, stroke-width:2px;
classDef no_outline fill:#fff, stroke-width:0px;
classDef kineticstoolkit fill:#aaffaa;


subgraph graph_recording[Recording data]
    kinematics([Kinematics]) --> recording
    kinetics([Kinetics]) --> recording
    emg([EMG]) --> recording
    etc0([...]) --> recording

    recording[Recording instrumentation + pre-processing]
end
class graph_recording top_level


subgraph graph_files[ ]
    recording -- file --> csv1
    recording -- file --> txt1
    recording -- file --> excel1
    recording -- file --> c3d1
    recording -- file --> n3d1
    recording -- file --> etc1
    ktkzip1[(ktk.zip)]
end
class graph_files no_outline


csv1[(csv)] -- file --> pandas1
txt1[(txt)] -- file --> pandas1
excel1[(Excel)] -- file --> pandas1
c3d1[(c3d)] -- file --> ktk_read
n3d1[(n3d)] -- file --> ktk_read
etc1[(...)]
ktkzip1:::kineticstoolkit -- file --> ktk_load


%%---------------------------------------------------
%% LOADING DATA

subgraph graph_loading[Loading data]

    pandas1["
        Pandas' read functions:
        - pd.read_csv()
        - pd.read_excel()
        - etc."]
    
    pandas1 -- DataFrame --> ktk_import_dataframe

    subgraph graph_ktk_load[ ]

        ktk_import_dataframe["TimeSeries.from_dataframe()"]:::kineticstoolkit
        ktk_read["
            ktk's read functions:
            - ktk.kinematics.read_c3d()
            - ktk.kinematics.read_n3d()
            "]:::kineticstoolkit
        ktk_load["ktk.load()"]:::kineticstoolkit

    end
    class graph_ktk_load no_outline


end
class graph_loading top_level


ktk_import_dataframe -- TimeSeries --> data1
ktk_read -- TimeSeries --> data1
ktk_load -- Python types\nndarray\nSeries\nDataFrame\nTimeSeries --> data1

data1[(Data)]

```


## Processing data

```{mermaid}
flowchart TB

classDef default fill:#fff, stroke:#aaa, text-align:left;
classDef top_level fill:#fff, stroke:#aaa, stroke-width:2px;
classDef no_outline fill:#fff, stroke-width:0px;
classDef kineticstoolkit fill:#aaffaa;

data[(Data)]


data -- TimeSeries <--> graph_processing_ktk
data -- "TimeSeries.data (ndarray)" <--> ktk_geometry
data -- "
    TimeSeries.data (ndarray)
    ndarray
    Series
    DataFrame" <--> graph_processing_others

subgraph graph_processing_ktk[ ]
    direction LR
    ktk_sync["
        TimeSeries operations:
        - add_event()
        - get_ts_before_event()
        - get_ts_after_event()
        - get_ts_between_events()
        - get_subset()
        - merge()
        - ui_sync()
        - ui_edit_events()
        - etc.
    "]:::kineticstoolkit
    ktk_filters["
        Filtering:
        - ktk.filters.butter()
        - ktk.filters.smooth()
        - ktk.filters.deriv()
        - etc.
    "]:::kineticstoolkit
    ktk_cycles["
        Cycles:
        - ktk.cycles.detect_cycles()
        - ktk.cycles.time_normalize()
        - etc.
    "]:::kineticstoolkit
    ktk_kinematics["
        Kinematics reconstruction:
        - ktk.kinematics.create_cluster()
        - ktk.kinematics.extend_cluster()
        - ktk.kinematics.track_cluster()
        - etc.
    "]:::kineticstoolkit
end

ktk_geometry["
    Geometrical operations:
    - ktk.geometry.create_transforms()
    - ktk.geometry.get_local_coordinates()
    - ktk.geometry.get_global_coordinates()
    - ktk.geometry.get_angles()
    "]:::kineticstoolkit

subgraph graph_processing_others[ ]
    direction LR
    numpy1[Numpy]
    pandas3[Pandas]
    scipy1[SciPy]
end


```
%%---------------------------------------------------
%% VISUALIZING DATA

subgraph graph_visualizing[Visualizing data]
    direction LR
    
    visualization_node(( )) -- TimeSeries --> graph_visualizing_ktk
    visualization_node(( )) -- "
        TimeSeries.data (ndarray)
        ndarray
        Series
        DataFrame" --> graph_visualizing_others

    subgraph graph_visualizing_ktk[ ]
        direction LR
        ktk_plot[Plotting]:::kineticstoolkit
        ktk_player[Visualizing markers in 3d]:::kineticstoolkit
    end

    subgraph graph_visualizing_others[ ]
        direction LR
        matplotlib_plot[Matplotlib]
    end


end

    subgraph graph_exporting_ktk
        direction LR
        ktk_export_dataframe[Export to Dataframes]:::kineticstoolkit
        ktk_write_c3d[Write to c3d]:::kineticstoolkit
    end

%%---------------------------------------------------
%% SAVING DATA


data2 --> graph_saving

subgraph graph_saving[Saving data]



    ktk_export_dataframe --> pandas2[Pandas]
    ktk_write_c3d --> c3d2[(c3d)]

end

```


Depending on your background, you may want to start your journey on this website at different points. Feel free to go back and forth in the following sections, or jump already to the [tutorials](tutorials.md).

```{tableofcontents}
```

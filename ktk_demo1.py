"""Kinetics Toolkit Demonstration - 1. Fundamentals"""

# %% Import KTK

import numpy as np
import pandas as pd

import kineticstoolkit as ktk

# %% Load a sample TimeSeries

ts1 = ktk.load(
    ktk.doc.download('timeseries_example.ktk.zip')
)

# - time and data
# - plot()

# %% Import KTK in lab mode

import kineticstoolkit.lab as ktk  # noqa

# - data
# - plot()

# %% Calculate other data

ts1.data['Ftot'] = np.sqrt(np.sum(ts1.data['Forces'] ** 2, axis=1))

# - plot()
# - plot only selected signals

# %% Detect cycles

ts2 = ktk.cycles.detect_cycles(
    ts1, 'Ftot',
    event_names=['push', 'recovery'],
    thresholds=[10, 5]
)

ts2.plot(['Forces', 'Ftot'])

# - help on the website and in the help browser
# - events

# %% Detect cycles with min durations

ts2 = ktk.cycles.detect_cycles(
    ts1,
    'Ftot',
    event_names=['push', 'recovery'],
    thresholds=[10, 5],
    min_durations=[0.2, 0.2]
)

ts2.plot(['Forces', 'Ftot'])

# %% Synchronization

ts3 = ts2.ui_sync()

# %% get_ts_...

ts4 = ts3.get_ts_after_event('push')
ts4.plot()

# %%

ts5 = ts3.get_ts_between_events('push', '_', 0, 4, inclusive=True)
ts5.plot()

# %%

ts6 = ts5.trim_events()
ts6.plot()

# %% get_event_time...

for i_cycle in range(0, 5):
    print(f"Cycle {i_cycle}:")

    push_time = (
        ts6.get_event_time('recovery', i_cycle)
        - ts6.get_event_time('push', i_cycle)
    )

    recovery_time = (
        ts6.get_event_time('_', i_cycle)
        - ts6.get_event_time('recovery', i_cycle)
    )

    cycle_time = push_time + recovery_time

    print(f"Push time = {push_time} s")
    print(f"Recovery time = {recovery_time} s")
    print(f"Cycle time = {cycle_time} s")
    print("")

# %% dir(ts6)


# %% save/load/export

ktk.save('tempfile.ktk.zip', ts6)

# %%

ts7 = ktk.load('tempfile.ktk.zip')

# Load in Matlab: unzip the file, then
# ts = jsondecode(fileread('data.json'))
# plot(ts.time, ts.data.Forces)


# %% Export to Excel

df = ts7.to_dataframe()

# %%

df.to_excel('tempfile.xlsx')

# df = pd.read_excel('tempfile.xlsx', index_col=0)

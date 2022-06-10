"""Kinetics Toolkit Demonstration - 1. Fundamentals"""

# %% Import KTK

import numpy as np
import kineticstoolkit as ktk

# %% Load a sample TimeSeries

ts = ktk.load(
    ktk.doc.download('timeseries_example.ktk.zip')
)

# - time and data
# - plot()

# %% Import KTK in lab mode

import kineticstoolkit.lab as ktk  # noqa

# - time and data
# - plot()

# %% Calculate other data

ts.data['Ftot'] = np.sqrt(np.sum(ts.data['Forces'] ** 2, axis=1))

# - plot()
# - plot only selected signals

# %% Detect cycles

test = ktk.cycles.detect_cycles(
    ts, 'Ftot',
    event_names=['push', 'recovery'],
    thresholds=[10, 5]
)

test.plot(['Forces', 'Ftot'])

# - help on the website and in the help browser
# - events

# %% Detect cycles with min durations

ts = ktk.cycles.detect_cycles(
    ts,
    'Ftot',
    event_names=['push', 'recovery'],
    thresholds=[10, 5],
    min_durations=[0.2, 0.2]
)

ts.plot(['Forces', 'Ftot'])

# %% Synchronization

ts = ts.ui_sync()

# %% get_ts_...

ts1 = ts.get_ts_after_event('push')
ts1.plot()

# %%

ts2 = ts.get_ts_between_events('push', '_', 0, 4, inclusive=True)
ts2.plot()

# %%

ts2 = ts2.trim_events()
ts2.plot()

# %% get_event_time...

for i_cycle in range(0, 5):
    print(f"Cycle {i_cycle}:")

    push_time = (
        ts.get_event_time('recovery', i_cycle)
        - ts.get_event_time('push', i_cycle)
    )

    recovery_time = (
        ts.get_event_time('_', i_cycle)
        - ts.get_event_time('recovery', i_cycle)
    )

    cycle_time = push_time + recovery_time

    print(f"Push time = {push_time} s")
    print(f"Recovery time = {recovery_time} s")
    print(f"Cycle time = {cycle_time} s")
    print("")

# %% dir(ts)

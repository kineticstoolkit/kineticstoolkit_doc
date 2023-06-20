---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# Removing artefacts using a median filter

Sometimes, a TimeSeries contains some bad measurements that really stand out from other data. If such artefacts are impossible to remove at the source and there are not many of them, then the median filter is a simple way to filter them out.

Let's first load some noisy data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

ts.plot(["clean", "artefacts"], ".-")
```

Using a median filter with a window length of 3 gives, for each point, the average of the two points that are the closest together.

```{code-cell} ipython3
filtered = ktk.filters.median(ts, window_length=3)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("artefacts", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "artefacts", "filtered"], '.-')
```

Most artefacts were removed, but not the ones at 30 and 31 seconds. This is because there were two consecutive artefacts, and as such the median filter considers that at these times, the clean signal is the artefact. A filter with a larger window length could be used, at the expense of more signal loss.

```{code-cell} ipython3
filtered = ktk.filters.median(ts, window_length=5)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("artefacts", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "artefacts", "filtered"], '.-')
```
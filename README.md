# pandas-montecarlo

Simple Monte Carlo-style simulation utilities for `pandas.Series`.

This package shuffles the observed series values across multiple simulations, computes cumulative sums, and provides summary statistics and an optional plot helper.

## Installation

From source (this repo):

```bash
pip install -e .
```

## Usage

### Python API

```python
import pandas as pd
from pandas_montecarlo import montecarlo

s = pd.Series([1, -2, 3, -1, 2, -3, 4, -2, 1])
res = montecarlo(s, sims=1000, bust=-3, goal=5)
print(res.stats)
# res.plot()  # optional plot
```

You can also call it as a method once the module is imported (it attaches to `pandas.core.base.PandasObject`):

```python
import pandas as pd
from pandas_montecarlo import montecarlo  # noqa: F401, side effect registration

s = pd.Series([1, 2, -1, 3])
res = s.montecarlo(sims=500)
print(res.stats)
```

### CLI Demo

After installing, a small demo CLI is available:

```bash
pandas-montecarlo-sample
```

Optionally provide a CSV file path (single numeric column) to use your own data:

```bash
pandas-montecarlo-sample path/to/series.csv
```

## API

`montecarlo(series, sims=100, bust=-1, goal=0)`

- **series**: `pandas.Series` of numeric values
- **sims**: number of simulated shuffles to run
- **bust**: threshold for computing bust probability (drawdown below `-abs(bust)`)
- **goal**: threshold for computing probability of reaching at least `abs(goal)` without busting

Returns an object with:

- **data**: `pd.DataFrame` of all simulated runs (cumulative sums)
- **stats**: dict with `min`, `max`, `mean`, `median`, `std`, `maxdd`, `bust`, `goal`
- **maxdd**: dict summarizing drawdowns across simulations
- **plot()**: function to render a quick matplotlib plot

## Notes

- This is a permutation resampling (shuffle) approach, not bootstrap with replacement.
- Requires `pandas` and `matplotlib`.

## License

LGPL-3.0
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas as pd
from pandas_montecarlo import montecarlo


def main():
    # Simple demo series or parse a CSV if provided
    if len(sys.argv) > 1:
        # Expect a CSV file with a single column of numeric values
        csv_path = sys.argv[1]
        series = pd.read_csv(csv_path, header=None, squeeze=True)
        if not isinstance(series, pd.Series):
            series = series.iloc[:, 0]
    else:
        series = pd.Series([1, -2, 3, -1, 2, -3, 4, -2, 1])

    results = montecarlo(series, sims=1000, bust=-3, goal=5)
    print(results.stats)


if __name__ == "__main__":
    main()



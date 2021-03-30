import dask.dataframe as dd

see = dd.read_csv(
    "../ACCESS-CM2_daily_rainfall_NSW.csv",
    assume_missing=True,
    usecols=use_cols,
)

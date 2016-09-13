# In agg files, split beneficiary data from the agg data

# In agg files, remove street address information

# In agg files: reconcile headers between 2012/2013 and 2014
  - 2014 is in lowercase and abbreviations
  - 2014 contains standardized amount


# In agg files, figure out why the in2csv conversions have one more line than the Excel Save As conversions

(seems to be solved when using csvformat...)


```sh
wc -l wrangle/corral/fetched/2013-agg.csv
  956294 wrangle/corral/fetched/2013-agg.csv

wc -l wrangle/corral/fetched/Medicare-Physician-and-Other-Supplier-NPI-Aggregate-CY2013.csv
  956293 wrangle/corral/fetched/Medicare-Physician-and-Other-Supplier-NPI-Aggregate-CY2013.csv
```

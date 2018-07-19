import pandas as pd

rawData = pd.read_csv('KatieData_Validation.csv', na_values=['999', '-999', 999, -999])
rawData.head()

newDF = rawData.filter(like='_Scored')

newDF.head()

values = newDF.apply(pd.Series.value_counts, normalize=True, axis=0)

values.to_csv('NormalisedCorrect.csv', index=False)

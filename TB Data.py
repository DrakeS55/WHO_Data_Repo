# Export Turberculosis Data from WHO into Python using Pandas library

# import pandas to read CSV file
import pandas as pd

# read CSV file using read_csv
data = pd.read_csv("/Users/drakeshaub/Documents/GitHub Desktop/WHO Data Repo/WHO_Data_Repo/TB_burden_countries_2023-07-09.csv")

# slice original TB data frame to get only region code and cfr value
country_cfr_dataframe = data.loc[:, ['iso3', 'cfr']]
type(country_cfr_dataframe['cfr'][0])
# "NaN" is a numpy.float64 data type, or np.nan ("NULL") value
# delete those columns with "NaN" value in cfr column
# looping is slow in pandas dataframes, so we are going to use a vectorized solution
# drop each data that has "NaN" as part of the cfr column using dropna() function
country_cfr_dataframe.dropna(subset = ['cfr'], inplace = True)
print(country_cfr_dataframe)

# plot country vs cfr using matplotlib
import matplotlib as mpl
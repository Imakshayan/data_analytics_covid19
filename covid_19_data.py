# creator = Akshay Nalawade
# Project = Covid19 Data 
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('raw_data.csv')
print(df)
profile = ProfileReport(df)
profile.to_file(output_file= "raw_data.csv")
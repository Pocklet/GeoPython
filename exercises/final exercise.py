import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas

fp = r"C:\Users\calebs\Documents\Geo-Python\data/2315676.txt"

data = pd.read_csv(
    fp,
    delim_whitespace=True,
    na_values=["-9999"],
    usecols=["DATE", "TAVG", "TMAX", "TMIN"],
)

print(data.head())


for i in range(len(data)):
    data["="]


        

import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas

fp = r"C:\Users\calebs\Documents\Geo-Python\data/2315676.txt"

data = pd.read_csv(
    fp,
    delim_whitespace=True,
    na_values=["-9999"],
    usecols=["DATE", "TAVG", "TMAX", "TMIN"],
    skiprows=[1],
)

print(data.head())


# creates new tavg column and cleans data
data["TMAX"] = data["TMAX"].fillna(0)
data["TMIN"] = data["TMIN"].fillna(0)
data["TAVG_NEW"] = ""
data["TMAX"] = data["TMAX"].astype(float)
data["TMIN"] = data["TMIN"].astype(float)


# calculates new tavg
data["TAVG_NEW"] = (data["TMAX"]+data["TMIN"])/2
# replaces na values with newly calculated vales
data["TAVG"].fillna(data["TAVG_NEW"], inplace = True)
print(data.head())


# defines celius to fahr function
def celsius_to_fahr(temp):
    return 9 / 5 * temp + 32


# converts tavg to celsius
data["T_C_AVG"] = ""
data["T_C_AVG"] = celsius_to_fahr(data["TAVG"])
print(data.head())
        

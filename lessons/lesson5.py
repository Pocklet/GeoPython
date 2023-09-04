import pandas as pd

data = pd.read_csv("Kumpula-June-2016-w-metadata.txt", skiprows=8)

# data = pd.read_csv('Kumpula-June-2016-w-metadata.txt', sep=`,`)
# The sep parameter can be used to specify whether the input data 
# uses some other character, such as ; as a delimiter. 

# print(data)

# print(data.head())
# print(data.tail())
# print(type(data))


temp_data = pd.read_csv(
    "Kumpula-June-2016-w-metadata.txt", skiprows=8, usecols=["YEARMODA", "TEMP"]
)
# print(temp_data.head())


# checking data info
# print(len(data))
# print(data.shape)
# print(data.columns.values)
# print(data.index)
# print(data.dtypes)
# print(len(data.columns))


# selection = data[["YEARMODA", "TEMP"]]
# print(selection)

import matplotlib.pyplot as plt

print(data["TEMP"].mean())
print(data.mean())
print(data[["TEMP", "MAX", "MIN"]].describe())
plt.plot(data[["TEMP", "MAX", "MIN"]])
# plt.show()

number_series = pd.Series([4, 5, 6, 7.0], index=["a", "b", "c", "d"])
print(number_series)

# Station names
stations = [
    "Hanko Russarö",
    "Heinola Asemantaus",
    "Helsinki Kaisaniemi",
    "Helsinki Malmi airfield",
]

# Latitude coordinates of Weather stations
lats = [59.77, 61.2, 60.18, 60.25]

# Longitude coordinates of Weather stations
lons = [22.95, 26.05, 24.94, 25.05]

new_data = pd.DataFrame(data={"station_name": stations, "lat": lats, "lon": lons})
print(new_data)
data["DIFF"] = 0.0
data["DIFF"] = data["MAX"] - data["MIN"]
data["TEMP_CELSIUS"] =(data["TEMP"] - 32) / (9 / 5)
data["TEMP_KELVIN"] = data["TEMP_CELSIUS"] + 273.15
print(data.head())

# Select first five rows of dataframe using row index values
# selection = data[0:5]
# print(selection)

# Select temp column values on rows 0-5
# selection = data.loc[0:5, "TEMP"]
# print(selection)

# Select columns temp and temp_celsius on rows 0-5
selection = data.loc[23:29, ["TEMP", "TEMP_CELSIUS"]]
print(selection)

# Select one row using index
# row = data.loc[4]
# print(row)
# print(row["TEMP"])
# print(data.at[0, "TEMP"])
# print(data.iloc[0:5, 0:2])
# print(data.iloc[0, 1])
# print(data.iloc[-1])


# Select rows with temp celsius higher than 15 degrees from late June 2016
warm_temps = data.loc[(data["TEMP_CELSIUS"] > 15) & (data["YEARMODA"] >= 20160615)]
# Reset index
warm_temps = warm_temps.reset_index(drop=True)
print(warm_temps)

# mean temp for late june
print(data["TEMP_CELSIUS"].loc[data["YEARMODA"] >= 20160624].mean())


# Drop no data values based on the MIN column
warm_temps_clean = warm_temps.dropna(subset=["MIN"])
print(warm_temps_clean)

# Fill na values
# warm_temps.fillna(-9999)


#conversion drops decimal points instead of rounding
print("Original values:")
print(data["TEMP"].head())

print("Truncated integer values:")
print(data["TEMP"].astype(int).head())

# rounding function
print("Rounded integer values:")
print(data["TEMP"].round(0).astype(int).head())


# Get unique celsius values
unique = data["TEMP"].unique()
print(unique) 
# unique values as list
list(unique)

# Number of unique values
unique_temps = len(unique)
print(f"There were {unique_temps} days with unique mean temperatures in June 2016.")

# Sort dataframe, ascending
# print(data.sort_values(by="TEMP"))

# Sort dataframe, descending
# data.sort_values(by="TEMP", ascending=False)


# define output filename
output_fp = "Kumpula_temps_June_2016.csv"

# Save dataframe to csv
data.to_csv(output_fp, sep=",")

# define output filename
output_fp2 = "Kumpula_temps_above15_June_2016.csv"

# Save dataframe to csv
warm_temps.to_csv(output_fp2, sep=",", index=False, float_format="%.1f")
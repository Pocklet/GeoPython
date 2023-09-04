import pandas as pd

fp = r"C:\Users\calebs\Documents\Geo-Python\Lesson6\data/029440.txt"
data = pd.read_csv(
    fp, delim_whitespace=True,
      usecols=["USAF", "YR--MODAHRMN", "DIR", 
               "SPD", "GUS", "TEMP", "MAX", "MIN"], 
               na_values=[
        "*", "**", "***", "****", "*****", "******"]
)
# data = pd.read_csv("data/029440.txt")

print(data.head())
print(data.columns)

new_names = {"YR--MODAHRMN": "TIME", 
             "SPD": "SPEED", "GUS": "GUST",
             "TEMP": "TEMP_F", "USAF": "STATION_NUMBER"}

data = data.rename(columns=new_names)
print(data.columns)


def fahr_to_celsius(temp_fahrenheit):
    """Function to convert Fahrenheit temperature into Celsius.

    Parameters
    ----------

    temp_fahrenheit: int | float
        Input temperature in Fahrenheit (should be a number)

    Returns
    -------

    Temperature in Celsius (float)
    """

    # Convert the Fahrenheit into Celsius
    converted_temp = (temp_fahrenheit - 32) / 1.8

    return converted_temp

# print(fahr_to_celsius(32))

# iterate over the rows
# for idx, row in data.iterrows():
    
#     # print the index value
#     print(f"Index: {idx}")

#     # print the row
#     print(f"Temp F: {row['TEMP_F']}\n")
#     break



# Create an empty float column for the output values
data["TEMP_C"] = 0.0

# # Iterate over the rows
# for idx, row in data.iterrows():

#     # Convert the Fahrenheit to Celsius
#     celsius = fahr_to_celsius(row["TEMP_F"])

#     # Update the value of 'Celsius' column with the converted value
#     data.at[idx, "TEMP_C"] = celsius



data[["TEMP_C", "MIN_C", "MAX_C"]] = data[[
    "TEMP_F", "MIN", "MAX"]].apply(fahr_to_celsius
)
print(data.head())


# Convert to string
data["TIME_STR"] = data["TIME"].astype(str)

# Slice the string
data["YEAR_MONTH"] = data["TIME_STR"].str.slice(start=0, stop=6)
data["MONTH"] = data["TIME_STR"].str.slice(start=4, stop=6)

# Let's see what we have
print(data.head())


# Convert to datetime and keep only year and month
data["YEAR_MONTH_DT"] = pd.to_datetime(data[
    "TIME_STR"], format="%Y%m", exact=False)

print(data["YEAR_MONTH_DT"].head())


grouped = data.groupby("YEAR_MONTH")
print(data["YEAR_MONTH"].nunique())


# Specify a month (as character string)
month = "201908"

# Select the group
group1 = grouped.get_group(month)
print(group1)


# Specify the columns that will be part of the calculation
mean_cols = ["DIR", "SPEED", "GUST", "TEMP_F", "TEMP_C"]

# Calculate the mean values all at one go
mean_values = group1[mean_cols].mean()

print(mean_values)


# Iterate over groups
for key, group in grouped:
    # Print key and group
    print(f"Key:\n {key}")
    print(f"\nFirst rows of data in this group:\n {group.head()}")

    # Stop iteration with break command
    break



# Create an empty DataFrame for the aggregated values
monthly_data = pd.DataFrame()

# The columns that we want to aggregate
mean_cols = ["DIR", "SPEED", "GUST", "TEMP_F", "TEMP_C"]

# Iterate over the groups
for key, group in grouped:

    # Calculate mean
    mean_values = group[mean_cols].mean()

    # Add the ´key´ (i.e. the date+time information) into the aggregated values
    mean_values["YEAR_MONTH"] = key
    
    # Convert the mean_values series to a DataFrame and make it have a row orientation
    row = mean_values.to_frame().transpose()

    # Concatenate the aggregated values into the monthly_data DataFrame
    monthly_data = pd.concat([monthly_data, row], ignore_index=True)

print(monthly_data)



aprils = data[data["MONTH"] == "04"]

aprils = aprils[["STATION_NUMBER", "TEMP_F", "TEMP_C", "YEAR_MONTH"]]

grouped = aprils.groupby(by="YEAR_MONTH")

monthly_mean = grouped.mean()
print(monthly_mean.head())
print(monthly_mean.sort_values(by="TEMP_C", ascending=False).head(10))


import glob
# "*"" is a wild card, any file that start with data/0
# and ends with txt will be picked up
file_list = glob.glob(r"data/0*txt")

print(f"Number of files in the list: {len(file_list)}")
print(file_list)

######################################################################


# Repeat the analysis steps for each input file:
for fp in file_list:

    # Read selected columns of  data using varying amount of spaces as separator and specifying * characters as NoData values
    data = pd.read_csv(
        fp,
        delim_whitespace=True,
        usecols=["USAF", "YR--MODAHRMN", "DIR", "SPD", "GUS", "TEMP", "MAX", "MIN"],
        na_values=["*", "**", "***", "****", "*****", "******"],
    )

    # Rename the columns
    new_names = {
        "USAF": "STATION_NUMBER",
        "YR--MODAHRMN": "TIME",
        "SPD": "SPEED",
        "GUS": "GUST",
        "TEMP": "TEMP_F",
    }
    data = data.rename(columns=new_names)

    # Print info about the current input file:
    print(f"STATION NUMBER: {data.at[0, 'STATION_NUMBER']}")
    print(f"NUMBER OF OBSERVATIONS: {len(data)}")

    # Create column
    col_name = "TEMP_C"
    data[col_name] = None

    # Convert tempetarues from Fahrenheits to Celsius
    data["TEMP_C"] = data["TEMP_F"].apply(fahr_to_celsius)

    # Convert TIME to string
    data["TIME_STR"] = data["TIME"].astype(str)

    # Parse year and month
    data["MONTH"] = data["TIME_STR"].str.slice(start=5, stop=6).astype(int)
    data["YEAR"] = data["TIME_STR"].str.slice(start=0, stop=4).astype(int)

    # Extract observations for the months of April
    aprils = data[data["MONTH"] == 4]

    # Take a subset of columns
    aprils = aprils[["STATION_NUMBER", "TEMP_F", "TEMP_C", "YEAR", "MONTH"]]

    # Group by year and month
    grouped = aprils.groupby(by=["YEAR", "MONTH"])

    # Get mean values for each group
    monthly_mean = grouped.mean()

    # Print info
    print(monthly_mean.sort_values(by="TEMP_C", ascending=False).head(5))
    print("\n")

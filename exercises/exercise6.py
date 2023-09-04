import pandas as pd
import calendar as calendar

fp = r"adata/1091402.txt"
data = pd.read_csv(fp, skiprows=[1], delim_whitespace=True,
                   na_values=["-9999","--------"])

print(data.head())
print(data.tail())


tavg_null = data["TAVG"].isna().sum()
print("Number of no-data values in 'TAVG':", tavg_null)

tmin_null = data["TMIN"].isna().sum()
print("Number of no-data values in 'TMIN':", tmin_null)

sum_days = len(data)
print("Number of days:", sum_days)

first_obs = data.at[1, "DATE"]
print(first_obs)

last_obs = data.iloc[-1]
print(last_obs["DATE"])


avg_temp = data["TAVG"].mean()
print(avg_temp)

print("Average temperature (F) for the whole dataset:", 
      round(avg_temp, 2))


data["TIME_DATE"] = data["DATE"].astype(str)

data["YEAR"] = data["TIME_DATE"].str.slice(start=0, stop=6).astype(int)
year_1969 = data[data["YEAR"] == 196901]
year_1969 = year_1969[["TMAX"]]
print("Average temperature (F) for the Summer of 69:", year_1969.mean())


data["TEMP_CELSIUS"] = (data["TAVG"] - 32) / (9 / 5)
data["MONTH"] = data["TIME_DATE"].str.slice(start=4, stop=6).astype(int)

grouped = data.groupby(by=["MONTH"])
grouped = grouped[["TEMP_CELSIUS", "MONTH"]]
monthly_mean = grouped.mean()

# months = monthly_mean["MONTH"]
# print(months)
# idx = [months[1], months[2], months[3], months[4], 
#        months[5], months[6], months[7], months[8], 
#        months[9], months[10], months[11], months[12],]

# months.index = idx
# results = months.dt.month_name


print(monthly_mean.head())


# data["YEAR_INT"] = data["YEAR"].astype(int)
# print(data["YEAR_INT"].head())
# reference_temps = (data.loc[data["YEAR_INT"]] <= 198100)
# test git hub

print("gittyhub")




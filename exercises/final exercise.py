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



# defines fahr to celsius function
def fahr_to_celsius(temp):
    return (temp-32) * (5/9)


# converts tavg to celsius
data["T_C_AVG"] = ""
data["T_C_AVG"] = fahr_to_celsius(data["TAVG"])


# slices date into year for grouping
data["TIME_STR"] = data["DATE"].astype(str)
data["YEAR"] = data["TIME_STR"].str.slice(
    start = 0, stop = 4,).astype(int
)


# subsets and groups by year
data_subset = data[["YEAR", "T_C_AVG"]]
grouped = data_subset.groupby(by=["YEAR"])
# calculates mean for each year
yearly_mean = grouped.mean()

# prints yearly mean to show highest values
print(yearly_mean.sort_values(by="T_C_AVG",
ascending = False))


# creates plot
ax = yearly_mean.plot(
    style = "r:",
    title = "Finland Yearly Mean Temperature",
    xlabel = "Year",
    ylabel = "Temperature [°C]",
    figsize = (12, 6),
)

# adds text to plot
ax.text(2004, 3.40, "Warmest Year ->")
ax.text(1916, -4.1, "<- Coldest Year")

# saves plot
plt.savefig("finland-yearly-temp-mean.pdf", 
dpi = 600)




        

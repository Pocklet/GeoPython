# lesson 7

import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas

# define abosolute path
fp = r"C:\Users\calebs\Documents\Geo-Python\Lesson6\data/029740.txt"

data = pd.read_csv(
    fp, 
    delim_whitespace = True,
    na_values=["*", "**", "***", "****", "*****", "******"],
    usecols=["YR--MODAHRMN", "TEMP", "MAX", "MIN"],
    parse_dates=["YR--MODAHRMN"],
    index_col="YR--MODAHRMN",
    )

print(data.head())

# ax = data.plot()

oct1_temps = data["TEMP"].loc[data.index >= "201910011200"]
# ax = oct1_temps.plot()

# Change line and symbol format, and add axis labels/title
# ax = oct1_temps.plot(
#     style="ro--",
#     title="Helsinki-Vantaa temperatures",
#     xlabel="Date",
#     ylabel="Temperature [°F]",
#     figsize=(12, 6),
# )

# # Define the start, end, and cold times
# start_time = pd.to_datetime("201910011200")
# end_time = pd.to_datetime("201910011500")
# cold_time = pd.to_datetime("201910011205")

# # Create the plot, including the axis limits
# ax = oct1_temps.plot(
#     style="ro--",
#     title="Helsinki-Vantaa temperatures",
#     xlabel="Date",
#     ylabel="Temperature [°F]",
#     figsize=(12, 6),
#     xlim=[start_time, end_time],
#     ylim=[40.0, 46.0],
# )

# # Add text to display the coldest temperature
# ax.text(cold_time, 42.0, "<- Coldest temperature in early afternoon")


# # Define start, end, and warm times
# start_time = pd.to_datetime("201910011800")
# end_time = pd.to_datetime("201910020000")
# warm_time = pd.to_datetime("201910012120")

# # Create the plot, including the axis limits

# ax = oct1_temps.plot(
#     style="k:",
#     title="Evening temperatures on October 1, Helsinki-Vantaa",
#     xlabel="Date",
#     ylabel="Temperature [°F]",
#     figsize=(12, 6),
#     xlim=[start_time, end_time],
#     ylim=[35.0, 44.0],
# )

# # Display text on plot
# ax.text(warm_time, 43.0, "Warmest time of the evening ->")



# Define time range
oct1_afternoon = oct1_temps.loc[oct1_temps.index <= "201910011500"]

# # Create bar plot
# ax = oct1_afternoon.plot(
#     kind="bar",
#     title="Helsinki-Vantaa temperatures",
#     xlabel="Date",
#     ylabel="Temperature [°F]",
#     figsize=(12, 6),
#     ylim=[40, 46],
# )

# # Add plot text
# ax.text(0, 42.1, "Coldest \ntemp \nv")

# # Save plot to file
# plt.savefig("bar-plot.png")
# # Save plot to file (high resolution, PDF)
# plt.savefig("bar-plot-hi-res.pdf", dpi=600)



july2014_df = data.loc[(data.index >= "201407010000") & (data.index < "201407310000")]

july2014_df.hvplot(
    title="Helsinki-Vantaa temperatures",
    xlabel="Date",
    ylabel="Temperature [°F]",
    ylim=[45.0, 90.0],
)
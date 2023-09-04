import pandas as pd

data = pd.read_csv("Kumpula-June-2016-w-metadata.txt", skiprows = 8)

print(data.head())
print(len(data))
print(data.columns.values)
print(data.dtypes)

print(data["TEMP"].mean())
print(data["MAX"].std())

data_clean = data.dropna(subset=["MAX"]+["MIN"])
print(data_clean)

data_clean["TEMP_CELSIUS"] = (data_clean["TEMP"] - 32) / (9 / 5)
data_clean["TEMP_CELSIUS"] = data_clean["TEMP_CELSIUS"].round(0).astype(int)
print(data_clean.head())

output_fp = "Kumpala_temps_June2016_clean"
data.to_csv(output_fp, sep=",", index=False, float_format="%.1f")
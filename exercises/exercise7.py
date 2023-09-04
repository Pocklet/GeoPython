import pandas as pd
import numpy as np


data = pd.DataFrame(columns = ["X", "Y", "Colour"])
data["X"] = np.random.rand(1000)
data["Y"] = np.random.rand(1000)
data["Colour"] = np.random.rand(1000)

print(data.head())

data["X"] = data["X"].astype(float)
print(type(data["X"]))
print(len(data))

plt = data.plot(
    x="X",
    y="Y",
    kind = "scatter",
    s=50,
    c=(data["Colour"]),
    colormap = "magma",
    edgecolors = "black",
    title = "Random Number Generator",
    xlabel = "X Values",
    ylabel = "Y Values"
)


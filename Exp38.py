import pandas as pd
import numpy as np

data = {
    "city":["A","A","A","B","B","B","C","C","C"],
    "temp":[30,32,31,25,26,24,35,36,34]
}
df = pd.DataFrame(data)

mean_temp = df.groupby("city")["temp"].mean()
std_temp = df.groupby("city")["temp"].std()
temp_range = df.groupby("city")["temp"].apply(lambda x: x.max()-x.min())

city_max_range = temp_range.idxmax()
city_min_std = std_temp.idxmin()

print("Mean temp:\n", mean_temp)
print("\nStd dev:\n", std_temp)
print("\nRange:\n", temp_range)
print("\nHighest range city:", city_max_range)
print("Most consistent (lowest std) city:", city_min_std)

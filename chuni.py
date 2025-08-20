import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#just change the file name below and remove title data since it doesn't read UTF-8
chuni = pd.read_csv("chunithm_record_2025-08-20T17_41_08.734Z.csv")

#this is for score analysis
ranks = ["S", "S+", "SS", "SS+", "SSS", "SSS+", "AJ"]
score_thresholds = [975000, 990000, 1000000, 1005000, 1007500, 1009000, 1010000]  

#you can modify this into score or rating
#if rating, use 0 to 17.7
#if score, use 0 to 1010000 (975000 to 1010000 as default)
filtered_chuni = chuni[(chuni["rating"] >= 16) & (chuni["rating"] <= 17.7) ]

numeric_cols = ["score", "rating"]
filtered_chuni[numeric_cols] = filtered_chuni[numeric_cols].apply(pd.to_numeric, errors='coerce')

#use this if you're going for average
#filtered_chuni = filtered_chuni.groupby('const', as_index=False)[numeric_cols].mean()

filtered_chuni = filtered_chuni[filtered_chuni["const"] >= 14]

plt.figure(figsize=(10,6))
plt.gcf().canvas.manager.set_window_title("CHUNITHM Rating Analysis")

plt.scatter(filtered_chuni["const"], filtered_chuni["rating"], color='skyblue', label="Max Score per Chart")

# Regression line
z = np.polyfit(filtered_chuni["const"], filtered_chuni["rating"], 1)
p = np.poly1d(z)
plt.plot(filtered_chuni["const"], p(filtered_chuni["const"]), "r--", label="Regression Line")

# Display regression formula
formula = f"y = {z[0]:.3f}x + {z[1]:.3f}"
plt.text(14.1, 17.6, formula, color="red", fontsize=12)

#if rating, use 0 to 17.7
#if score, use 975000 to 1010000
plt.ylim(16, 17.7)

#use this if you're doing score analysis
#plt.yticks(score_thresholds, ranks)

#use this if you're doing rating analysis
yticks = [round(y, 1) for y in list(np.arange(16.0, 17.7, 0.1))]
plt.yticks(yticks)


#this is for the chart constants, arrange it from 0 to 15.8 and STRICTLY ONLY ON 0.1 TICK
xticks = [round(x, 1) for x in list(np.arange(14.0, 15.8, 0.1))]
plt.xticks(xticks)

plt.xlabel("Chart Constant (VERSE Intl ver.)")
plt.ylabel("Rank")
plt.title("Regression Analysis on Rating per CHUNITHM Chart Constant (14 and Above)")

plt.legend()
plt.show()

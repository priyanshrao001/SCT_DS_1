import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")
print(df.head())
print(df.columns)
df["Sex Ratio"] = df["Sex Ratio"].astype(str).str.replace(",", "").astype(int)

least5 = df.sort_values("Sex Ratio", ascending=True).head(5)
print(least5[["State", "Sex Ratio"]])

plt.figure(figsize=(10,6))
plt.figure(figsize=(8,5))
plt.bar(least5["State"], least5["Sex Ratio"], color="orange")
plt.xticks(rotation=30, ha="right")
plt.title("Top 5 States with Lowest Sex Ratio in India")
plt.xlabel("State")
plt.ylabel("Sex Ratio (Females per 1000 Males)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()


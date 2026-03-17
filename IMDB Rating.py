import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('IMDB Dataset.csv')

data.head(5)

data.isnull().sum()

plt.hist(data["Runtime"])
plt.ylabel("Count of Movies")
plt.xlabel("Runtime (minutes)")
plt.show()

plt.hist(data["IMDB_Rating"])
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")
plt.show()

data["Runtime"].unique()

bins_time = np.arange(80, 230, 10)

plt.hist(data["Runtime"], bins=bins_time, edgecolor="black", color="skyblue")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Count of Movies")
plt.show()

data["IMDB_Rating"].unique()

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data["IMDB_Rating"], bins=bins_rating, edgecolor="black", color="maroon")
plt.xlabel("IMDB Rating")   
plt.ylabel("Count of Movies")
plt.xticks(bins_rating)
plt.show()
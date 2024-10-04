import pandas as pd
import numpy as np
from pprint import pprint
import seaborn as sns
import matplotlib.pyplot as plt
import csv

#with open('winequality-red.csv', newline='') as file:
##    reader = csv.reader(file)
#    res = list(map(tuple, reader))

#print(res)
#print("3. Add quality tag:")
#for entry in res:
#    is_good = False
#    if entry["quality"] >= 6.0:
#        is_good = True
#    entry["is_good"] = is_good

df = pd.read_csv('winequality-red.csv')
df.insert(12, "is_good", 0)
#print(df)
#print(df["quality"][0])

#Define is wine is good
for i in range(len(df.index)):
    if df["quality"][i] >= 6.0:
        df.loc[i, "is_good"] = 1

q1 = np.percentile(df["quality"], 25)
q3 = np.percentile(df["quality"], 75)
interquartile_range = 1.5 * (q3-q1)
print("4. q1=", q1, " q3=", q3, " Interquntile range: ", interquartile_range)

#Define rows to remove if quality out of interquntile range
indexes = []
for i in range(len(df.index)):
    if df["quality"][i] < q1 or df["quality"][i] > q3:
        indexes.append(i)
#Drop rows out of interquntile range
filtered_quality_df = df.drop(indexes)

print("Droped indexes:", len(indexes))

#print(filtered_quality_df.to_string())
#print(indexes)
sns.displot(filtered_quality_df['quality'],bins=25)
plt.show()

#Medians
q2_fixed_acidity = np.percentile(df["fixed acidity"], 50)
q2_volatile_acidity = np.percentile(df["volatile acidity"], 50)
q2_citric_acid = np.percentile(df["citric acid"], 50)
q2_residual_sugar = np.percentile(df["residual sugar"], 50)
q2_chlorides = np.percentile(df["chlorides"], 50)
q2_free_sulfur_dioxide = np.percentile(df["free sulfur dioxide"], 50)
q2_total_sulfur_dioxide = np.percentile(df["total sulfur dioxide"], 50)
q2_density = np.percentile(df["density"], 50)
q2_ph = np.percentile(df["pH"], 50)
q2_sulphates = np.percentile(df["sulphates"], 50)
q2_alcohol = np.percentile(df["alcohol"], 50)
q2_quality = np.percentile(df["quality"], 50)

print("Medians:")
print("q2_fixed_acidity=", q2_fixed_acidity)
print("q2_volatile_acidity=", q2_volatile_acidity)
print("q2_citric_acid=", q2_citric_acid)
print("q2_residual_sugar=", q2_residual_sugar)
print("q2_chlorides=", q2_chlorides)
print("q2_free_sulfur_dioxide=", q2_free_sulfur_dioxide)
print("q2_total_sulfur_dioxide=", q2_total_sulfur_dioxide)
print("q2_density=", q2_density)
print("q2_ph=", q2_ph)
print("q2_sulphates=", q2_sulphates)
print("q2_alcohol=", q2_alcohol)
print("q2_quality=", q2_quality)

plt.boxplot(x=df['quality'])
plt.show()

sns.displot(filtered_quality_df['quality'],bins=25)
plt.show()

sns.displot(df['fixed acidity'],bins=25)
plt.show()
sns.displot(df['volatile acidity'],bins=25)
plt.show()
sns.displot(df['citric acid'],bins=25)
plt.show()
sns.displot(df['residual sugar'],bins=25)
plt.show()
sns.displot(df['chlorides'],bins=25)
plt.show()
sns.displot(df['free sulfur dioxide'],bins=25)
plt.show()
sns.displot(df['total sulfur dioxide'],bins=25)
plt.show()
sns.displot(df['density'],bins=25)
plt.show()
sns.displot(df['pH'],bins=25)
plt.show()
sns.displot(df['sulphates'],bins=25)
plt.show()
sns.displot(df['alcohol'],bins=25)
plt.show()
sns.displot(df['quality'],bins=25)
plt.show()

sns.heatmap(df.corr())
plt.show()
#Part 3
import pandas as pd
import seaborn as sns
import numpy as np
df=pd.read_csv("wdi_wide.csv")

#Question 3
df.info()

#Question 4
print(df.nunique())

#Question 5
print(df.describe())
#provides count, mean, standard deviation, minimum
#maximum and percentage of GNI over all countries in dataset

#Question 6
df["GNI per capita"] = (df["GNI"] / df["Population"]).round(2)

#Question 7 Part A
region_count=df["Region"].value_counts()
print(region_count)

# Question 7 Part B
high_income_economy_count =df["High Income Economy"].value_counts()
print(high_income_economy_count)

#Question 8 
result=pd.crosstab(df["Region"], df["High Income Economy"])
print(result)

#Question 9
filtered_df = df[df["Life expectancy, female"] > 80]
print(filtered_df)
for i in filtered_df["Country Name"] :
        print(i)
        
        
#Part 4 

#Question 1
sns.relplot(data=df, x="Life expectancy, male", y="GNI per capita")
sns.relplot(data=df, x="Life expectancy, female", y="GNI per capita")
#yes the longer you live the more GNI per Capita you have 

#Question 2
sns.relplot(data=df, x="Life expectancy, male", y="GNI per capita", hue="Region")
sns.relplot(data=df, x="Life expectancy, female", y="GNI per capita", hue="Region")

#Question 3 
sns.relplot(data=df, kind="line", x="Life expectancy, female", y="GNI per capita", hue="Region", errorbar="sd")

#Question 4 
sns.lmplot(data=df, x="Life expectancy, female", y="GNI per capita", hue="Region")

#Question 5 

#Do greenhouse gas emissions in each region influence women’s life expectancy?
sns.relplot(data=df, x="Life expectancy, female", y="Greenhouse gas emissions", col="Region")
#

#For a given region, is there a link between women’s tertiary education and their life expectancy?
sns.relplot(data=df, x="Life expectancy, female", y="Tertiary education, female", col="Region")
#

#Does access to physicians impact women’s life expectancy in a given region?
sns.relplot(data=df, x="Life expectancy, female", y="Physicians", col="Region")
#

#How does life expectancy for women relate to Internet use in each region?
sns.relplot(data=df, x="Life expectancy, female", y="Internet use", col="Region")
#

#What is the relationship between women in national parliament and their life expectancy for each region?
sns.relplot(data=df, x="Life expectancy, female", y="Women in national parliament", col="Region")
#

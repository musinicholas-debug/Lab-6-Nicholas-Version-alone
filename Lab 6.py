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
#In each given region there is no real difference. For most countries the Greenhouse gas emission are relativately simalery to one another but female life expectancy still has a great difference espically in regions like africa we're certain contries have very low life expectancys and others very high despite having simalar Greenhouse gas emissions.

#For a given region, is there a link between women’s tertiary education and their life expectancy?
sns.relplot(data=df, x="Life expectancy, female", y="Tertiary education, female", col="Region")
#For this question the plots clearly demonstrate that the more females attend tertiarty education the longer they live. In every plot for each region this trend is noticable.

#Does access to physicians impact women’s life expectancy in a given region?
sns.relplot(data=df, x="Life expectancy, female", y="Physicians", col="Region")
#Once again the plots for each region with africa as the only outlier demonstrate that the more access a population has to physicans the longer in this specefic plots the women live. For africa in the ranges of life expectancy from 55 to 75 there is very little access to physicans so no correlation can be made.

#How does life expectancy for women relate to Internet use in each region?
sns.relplot(data=df, x="Life expectancy, female", y="Internet use", col="Region")
#Again in countries with high internet use female life expectancy is high this can logically attributed with high internet use meaning a highly developped country meaning a higher life expectancy because of good social and medical infrastructre

#What is the relationship between women in national parliament and their life expectancy for each region?
sns.relplot(data=df, x="Life expectancy, female", y="Women in national parliament", col="Region")
#Similary to question 1 of Part 4 Q5 no real correlation can be made the points for each region are very random indicating no real relationship.

#Question 6 

#Part A
df["Emissions per capita"] = (df["Greenhouse gas emissions"] / df["Population"])
sns.relplot(data=df, x="Internet use", y="Emissions per capita", hue="Region")
#Yes there is the plot shows that the more you approch the left of the x-axis so 100% internet use the more emissions per capita you have. 

#Part B
filtered_df = df[df["Emissions per capita"] > 0.03]
print(filtered_df)
for i in filtered_df["Country Name"] :
        print(i)
#There are only 2 countries that fit the criterias for a high emission countries

#Part C
sns.relplot(data=filtered_df, x="Internet use", y="Country Name",)
#There a strong correlation because more then 95% of both Quatar and Brunei Darussalam populations use the internet

#Part D
filtered_df2 = df[df["High Income Economy"] > 0.03]
print(filtered_df2)
for i in filtered_df2["Country Name"] :
        print(i)
        
sns.relplot(data=filtered_df2, x="High Income Economy", y="Emissions per capita",)
# No not all high income economies have high emissions after seeing the plot you can see that many countries fall below the 0.03 high emission cutoff and still are high income economies.

        




















#Part 3
import pandas as pd
import seaborn as sns
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
#Yes the longer you live the more GNI per Capita you have 

#Question 2
sns.relplot(data=df, x="Life expectancy, male", y="GNI per capita", hue="Region")
sns.relplot(data=df, x="Life expectancy, female", y="GNI per capita", hue="Region")
#As seen by the plot, the most developed regions have longer life expectancies, and therefore, they have higher GNI per capita.


#Question 3 
sns.relplot(data=df, kind="line", x="Life expectancy, female", y="GNI per capita", hue="Region", errorbar="sd")
#What is noticeable for this plot is that even if I included the standard deviation for the plot, it is unnoticeable.

#Question 4 
sns.lmplot(data=df, x="Life expectancy, female", y="GNI per capita", hue="Region")
#We notice that regions such as Africa have very small linear regressions compared to Europe, which has a very steep slope, which is also situated on the leftmost side of the x-axis, compared to the African one situated on the rightmost side of the x-axis. Showing a clear difference between life expectancy and the accumulation of money.

#Question 5 

#Do greenhouse gas emissions in each region influence women’s life expectancy?
sns.relplot(data=df, x="Life expectancy, female", y="Greenhouse gas emissions", col="Region")
#In each given region, there is no real difference. For most countries, the Greenhouse gas emissions are relatively similar to one another, but life expectancy still has a great difference, especially in regions like Africa we're certain countries have very low life expectancies and others very high, despite having similar Greenhouse gas emissions

#For a given region, is there a link between women’s tertiary education and their life expectancy?
sns.relplot(data=df, x="Life expectancy, female", y="Tertiary education, female", col="Region")
#For this question, the plots clearly demonstrate that the more females attend tertiary education, the longer they live. In every plot for each region, this trend is noticeable.

#Does access to physicians impact women’s life expectancy in a given region?
sns.relplot(data=df, x="Life expectancy, female", y="Physicians", col="Region")
#Once again, the plots for each region with Africa as the only outlier demonstrate that the more access a population has to physicians, the longer in these specific plots the women live. For Africa, in the range of life expectancy from 55 to 75, there is very little access to physicians, so no correlation can be made.

#How does life expectancy for women relate to Internet use in each region?
sns.relplot(data=df, x="Life expectancy, female", y="Internet use", col="Region")
#Again, in countries with high internet use, female life expectancy is high. This can be logically attributed to high internet use, meaning a highly developed country, resulting in a higher life expectancy due to good social and medical infrastructure.

#What is the relationship between women in national parliament and their life expectancy for each region?
sns.relplot(data=df, x="Life expectancy, female", y="Women in national parliament", col="Region")
#Similarly to question 1 of Part 4 Q5, no real correlation can be made; the points for each region are very random, indicating no real relationship.

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
#There are only 2 countries that fit the criterias for high-emission countries.

#Part C
sns.relplot(data=filtered_df, x="Internet use", y="Country Name",)
#There is a strong correlation because more than 95% of both Qatar and Brunei Darussalam populations use the internet.

#Part D
filtered_df2 = df[df["High Income Economy"] > 0.03]
print(filtered_df2)
for i in filtered_df2["Country Name"] :
        print(i)
        
sns.relplot(data=filtered_df2, x="High Income Economy", y="Emissions per capita",)
#No, not all high-income economies have high emissions. After seeing the plot, you can see that many countries fall below the 0.03 high emission cutoff and are still high-income economies.


        




















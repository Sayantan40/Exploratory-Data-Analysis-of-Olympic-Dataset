import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

athlete_df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')

print(athlete_df.head())

print(athlete_df.head())

# Join the dataframe

athlete_df_1=athlete_df.merge(region_df,how='left',on='NOC')
print(athlete_df_1.head())

# to see the number rows and columns now after joining.

print(athlete_df_1.shape)

# Keeping the columns names consistent

athlete_df_1.rename(columns={'region':'Region','notes':'Notes'},inplace=True)

print(athlete_df_1.head())

# to get the full information/ summery of the dataframe
print(athlete_df_1.info())

# to get statistical details of the dataset

print(athlete_df_1.describe())

# To check for Null values in the dataset
# result will show which columns in the dataset has null values in boolean T/F
nan_value=athlete_df_1.isna()
nan_columns=nan_value.any()
print(nan_columns)

# To see the total number of null values present in each column.
print(athlete_df_1.isnull().sum())

# to filter out india details first 5 rows
Team_India=athlete_df_1.query('Team=="India"').head(5)
print(Team_India)


# to filter out japan details
Team_japan=athlete_df_1.query('Team=="Japan"').head(5)
print(Team_japan)

# To see the top countries participating in olympics  since 1896

Top_10_countries=athlete_df_1.Team.value_counts().sort_values(ascending=False).head(10)
print(Top_10_countries)

# Plot the top 10 countries

plt.figure(figsize=(12 , 6))
plt.title('Overall participation by countries')
bar_plot=sns.barplot(x=Top_10_countries.index, y=Top_10_countries,palette='Set2');
plt.show()

# To show the age distribution of the participant/athletes.

plt.figure(figsize=(12, 6))
plt.title("Age distribution of the athletes ")
plt.xlabel('Age')
plt.ylabel('Number of participants')
Hist_plot = plt.hist(athlete_df_1.Age , bins=np.arange(10,80,2) , color='orange', edgecolor='white');
plt.show()

# To show Winter Olympic sports
winter_sports=athlete_df_1[athlete_df_1.Season=='Winter'].Sport.unique
print((winter_sports))

# to show Summer Olympics sports
summer_sports=athlete_df_1[athlete_df_1.Season=='Summer'].Sport.unique
print((summer_sports))

# Number of Male and female participants

gender_count=athlete_df_1.Sex.value_counts()
print(gender_count)

# pie-plot to show the visual representation of the male and female participants
plt.figure(figsize=(12,6))
plt.title('Gender Distribution')
pie_plot=plt.pie(gender_count,labels=gender_count.index,autopct='%1.1f%%',startangle=120,shadow=True);
plt.show()

# total number of Medats

Total_Medals=athlete_df_1.Medal.value_counts
print(Total_Medals)


# total number of female athletes participated in each olympics

female_participants=athlete_df_1[(athlete_df_1.Sex=="F") & (athlete_df_1.Season=="Summer")][['Sex','Year']]
female_participants=female_participants.groupby('Year').count().reset_index()
print(female_participants.head())
print(female_participants.tail())

# to create count_plot of the female participants over the year of olympics

womenolympics =athlete_df_1[(athlete_df_1.Sex=="F") & (athlete_df_1.Season=="Summer")]
sns.set(style="darkgrid")
plt.figure(figsize=(15,10))
sns.countplot(x="Year",data=womenolympics,palette="Spectral")
plt.title("Female Participation")
plt.show()

# Line_graph f the female participants over the year of olympics.

part = womenolympics.groupby("Year")["Sex"].value_counts()
plt.figure(figsize=(15,10))
part.loc[:,'F'].plot()
plt.title("Female participation over the years of Olympics")
plt.show()

# Number of Gold Medal athletes
Gold_Medal_atheletes=athlete_df_1[(athlete_df_1.Medal=="Gold") & (athlete_df_1.Sex=="F")]
print(Gold_Medal_atheletes)

# take only the values ehich differnt from Nan

Gold_Medal_atheletes=Gold_Medal_atheletes[np.isfinite(Gold_Medal_atheletes["Age"])]

# To see athletes above the age of 60 has got an gold medal
athlete_60_gold=athlete_df_1[(athlete_df_1.Age>60) & (athlete_df_1.Medal=="Gold")]
print(athlete_60_gold)

# The sports on which they got the medals
sport_event=athlete_60_gold['Sport'][athlete_60_gold['Age']>60]
print(sport_event)

# plot the above sport_event
plt.figure(figsize=(12,10))
plt.tight_layout()
sns.countplot(sport_event)
plt.title('Gold medal atheletes above 60')
plt.show()

# to see the most recent summer Olympics that is in 2016 and number of medals achieved by each countries

max_year=athlete_df_1.Year.max()
print(max_year)
team_names = athlete_df_1[(athlete_df_1.Year==2016) & (athlete_df_1.Medal=="Gold")].Team
print(team_names.value_counts().head(10))

# Plot a bar_plot using above result
sns.barplot(x=team_names.value_counts().head(20),y=team_names.value_counts().head(20).index)
plt.xlabel('Country medals of the year 2016')
plt.ylim(None)
plt.show()

# To visualize the Height and weight of male and female athletes who acquired a medal(any medal)

# first to filter the values (here medals) only and not the null values.

not_null_medals=athlete_df_1[(athlete_df_1['Height'].notnull()) & (athlete_df_1['Weight'].notnull())]
print(not_null_medals.head())

# the Plot scatter_plot

plt.figure(figsize=(15,10))
axis=sns.scatterplot(x="Height",y="Weight",data=not_null_medals,hue="Sex")
plt.title("Height vs Weight of Olympic Medallsts ")
plt.show()













































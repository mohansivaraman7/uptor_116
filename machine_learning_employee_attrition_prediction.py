import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings('ignore')

df=pd.read_csv("HR-Employee-attrition.csv")

print(df.head())
print(df.head(10))

print(df.info())

print(df.describe())

#Corrlation Map

fig, ax= plt.subplots(figsize=(20,20))
data_corr= df.drop(['Attrition','Department','BusinessTravel',
          'EducationField','Gender','JobRole','MaritalStatus','Over18','OverTime'], axis=1)
sns.heatmap(data_corr.corr(),annot=True, linewidths=0.5, fmt='0.1f', ax=ax)

#Countplot

sns.countplot(x='OverTime', data=df)
fig = plt.gcf()
fig.set_size_inches(5,5)
plt.title('Over Time')
plt.show()

sns.countplot(data=df, x="Education")
fig= plt.gcf()
fig.set_size_inches(5,5)
plt.title('Education Level')
plt.show()

sns.countplot(x='MaritalStatus', hue='OverTime', data=df)
fig= plt.gcf()
fig.set_size_inches(5,5)
plt.title('Marital Status')
plt.show()

#getting the employee ids of the people who are the morattu singles
morattu_singles= df.loc[df['MaritalStatus'] == 'Single']
print("The employee ids of people who are single are as below:\n")
morattu_singles['EmployeeNumber']

sns.countplot(x= 'JobRole', data=df)
fig= plt.gcf()
fig.set_size_inches(21,5)
plt.title('Job Role')

sns.countplot(x='Gender', hue='OverTime' , data=df)
fig= plt.gcf()
fig.set_size_inches(5,5)
plt.title('Over Time Comparison wrt Gender')

sns.countplot(data=df, x="EducationField")
fig= plt.gcf()
fig.set_size_inches(10,5)
plt.title('Education Field')
plt.show()

sns.countplot(data=df, x="Department")
fig= plt.gcf()
fig.set_size_inches(6,5)
plt.title('Department')
plt.show()

#Categorical plot (sns.catplot)
sns.catplot(data=df, x='OverTime', y='Age', kind='swarm', hue='OverTime')
fig= plt.gcf()
fig.set_size_inches(5,5)
plt.title('Overtime vs Age Distribution')

sns.countplot(data=df, x="BusinessTravel")
fig= plt.gcf()
fig.set_size_inches(6,5)
plt.title('Business Travel')
plt.show()

plt.subplots(figsize=(20,10))
sns.countplot(data=df, x='TotalWorkingYears')
plt.title('Working Years')

sns.countplot(data= df, x='NumCompaniesWorked')
plt.title('Number of Companies Worked')
fig= plt.gcf()
fig.set_size_inches(5,5)
plt.show()

fig, ax= plt.subplots(figsize=(18,5))
sns.countplot(data=df, x='DistanceFromHome')
plt.title('Distance From Home')

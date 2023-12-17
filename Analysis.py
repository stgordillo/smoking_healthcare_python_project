# Importing packages needed for analysis
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Checking csv to make sure it read correctly
df = pd.read_csv('NHANES.csv')
df.head()
---
# Exploring data
df.info()
df.describe()
---
# Looking at the explored data, we can see there is 5,735 entries in 28 columns. I'd like to get rid of columns that
# is missing too much information and rename the columns to be easier to read. The original website provides a key for
# the column names.
---
# Creating and renaming dataframe with only usable columns
da = df.loc[: , ['SEQN', 'SMQ020', 'RIAGENDR', 'RIDAGEYR', 'DMDMARTL', 'DMDEDUC2', 'BMXWT', 'BMXHT', 'BMXBMI', 'BPXSY1']]
da.columns = ['id', 'smoking', 'gender', 'age', 'marital_status', 'education', 'weight', 'height', 'bmi' , 'systolic_blood_pressure']
da.head()
---
# Exploring new dataframe
da.info()
da.describe()
---
# Checking for duplicates
da[da.duplicated()]
# There are no duplicates
---
# Relabeling education to be clearer
da['education'] = da['education'].replace({1: "< 9", 2: "9-11", 3: "HS/GED", 4: "Some College/Associate's", 5: "College", 
                                       7: "Refused", 9: "Don't know"})

da['education'].value_counts()
---
# Relabeling gender to be clearer
da['gender'] = da.gender.replace({1: "Male", 2: "Female"})

da['gender'].value_counts()
---
# Relabeling marital_status to be clearer
da["marital_status"] = da['marital_status'].replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married",
                                      6: "Co-habitating", 7: "Refused"})


da['marital_status'].value_counts()
---
# Relabeling smoking to be clearer
da['smoking'] = da['smoking'].replace({1: "Yes", 2: "No" , 7: "Refused", 9:"Don't know "})

da['smoking'].value_counts()
---
# Checking dataset for new catagorical labels
da.head()
---
# Checking for null values in dataset
da.isnull().sum()
# For this analysis, the missing values are fairly small, with the highest being systolic at about 5%.
# I'll fix the information instead of dropping those columns.
---
# Replacing the null values
# Quantitative data will be replaced with the mean
# Catagorical data will be replaced with "Missing"
da['marital_status'] = da['marital_status'].fillna("Missing")
da['education'] = da['education'].fillna("Missing")

quantatives = da.select_dtypes(include = 'float64')

m_ary = np.mean(da[da.gender == 'Male'])[1:]
f_ary = np.mean(da[da.gender == 'Female'])[1:]


num = 0
for i in quantatives.columns :
    da.loc[(da.gender == 'Male' ) & (da[i].isna()), i] = m_ary[num]
    da.loc[(da.gender == 'Female' ) & (da[i].isna()), i ] = f_ary[num]
    num+=1

da.isna().sum()
---
# Checking that the dataset reads the new split between categorical and numerical data
da.describe()
---
# Creating histograms showing count for age, weight, height and BMI
fig, axs = plt.subplots(2,2, figsize=(15, 10))
      
sns.histplot(data= da, x="age", kde=True, color="purple", ax=axs[0,0])
sns.histplot(data= da, x="weight", kde=True, color="blue", ax=axs[0,1])
sns.histplot(data= da, x="height", kde=True, color="gold", ax=axs[1,0])
sns.histplot(data= da, x="bmi", kde=True, color="red", ax=axs[1,1])

plt.show()
---
# Creating boxplots showing systolic blood pressure differences between males and females in age groups
da["Age Group"] = pd.cut(da.age, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize=(12, 5))
sns.boxplot(x="Age Group", y='systolic_blood_pressure', hue="gender", data=da);
---
# Creating bar plot to compare smoking by gender, both count and percentage
sns.countplot(x='smoking', hue='gender', data=da)

(pd.crosstab(da['smoking'],da['gender'], 
             normalize='index')
   .plot.bar(stacked=True)
)
---
# Dynaically creating categorical columns
categorical_columns = da.select_dtypes(include='object').columns

# Creating subplots
fig, axes = plt.subplots(nrows=1, ncols=len(categorical_columns)-1, figsize=(24, 10))

# Creating a pie chart for each subplot
for i, column in enumerate(categorical_columns[1:]):
    counts = da.groupby([column, 'smoking']).size().unstack().fillna(0)['Yes']
    axes[i].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    axes[i].set_title(f'Smoking Distribution in {column}')

# Displaying the charts
plt.tight_layout()
plt.show()
---

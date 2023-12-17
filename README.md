# Smoking and Healthcare - Python Project
## Introduction
Final project as a part of my Data Analytics and Visualization college course.  We could use any dataset we wanted to use Python to explore, clean and visualize data.  I've chosen a dataset concerning a smoking questionnaire from 2015 - 2016.

We'll use the information found here to look at the general health of the participants, their smoking habits and we can find any correlation between smoking and other stressors in their life as reported on this survey.

## Data Sources
The dataset used in this project was retrieved from the National Health and Nutrion Examination Survey (NHANES) found on the Centers for Disease Control and Prevention (CDC) website found here: [CDC NHANES Survey](https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Questionnaire&CycleBeginYear=2015).

## Changelog & Cleaning
* The dataset column names aren't easy to follow, and there were a lot of data we didn't need for this particular analysis. I created a new dataframe using only 10 of the 28 columns and renamed them using the key found on the CDC website. As an example, I changed "DMDEDUC2" into "education"
* No duplicates found
* All the categorical data was defined in numerical values (1, 2, etc for multiple choices), so I needed to change them using the key found on the CDC website. As an example, I changed "3" in the education column into "HS/GED"
* I checked the null values, and while there were a few, I didn't think it would impact the data by not removing it. Instead, I changed numerical data into the mean value and the categorical data into "Missing"


## Analysis Summary
This section is a quick summary of my findings. You can find the full code and details in the [Analysis](https://github.com/stgordillo/smoking_healthcare_python_project/blob/e374cb1867358d67f65efbf0d647cfe3316fb58b/Analysis.py).

You can also find the visualizations created in Python in [Visualizations](https://github.com/stgordillo/smoking_healthcare_python_project/blob/8d2c66b70e7e49c3ed54c9e7f323cb09e62c08c8/Visualizations.md).

**Analysis**
* Created 4 histograms looking at the count of participants age, weight, height and BMI score
  * Found participants were in a generally healthy range. Age was mostly evenly spread, with a higher number of elderly
* Created a boxplot looking at age groups, gender and systolic blood pressure of participants
  * Number of outliers, with participants mostly in the at-risk range. Females generally healthier than males
* Created 2 bar charts, looking at the count and percentage of participants smoking habits, divided by gender
  * More males smoke by a significant margin. 
* Lastly, created 3 pie charts. One looking at similar data to the bar chart, another looking at correlation of smokers and relationship status, and the last looking at the correlation of education and smoking.
  * Married participants take up almost 50% of smokers. Those in the range of high school diploma or GED to some college or associate's degree smoke more than participants of other education levels.

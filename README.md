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
This section is a quick summary of my findings. You can find the full analysis and details in the [Analysis](https://github.com/stgordillo/Student-Performance-SQL/blob/4b6d5518e1e779aee94e8a89c852d5d88f1140c7/Analysis.sql).

**Queries**
STOPPED HERE
* First, I checked to make sure the csv was loaded properly and to look at the information given.
* The second query I combined all the scores together and ordered them to see top 5 scores.
* The third query was used as a starting place for the next, more complex query and to confirm that gender and race/ethnicity was working properly and present for both values. 
* The last query is essentially performing an analysis of student performance based on their total scores, gender, and race/ethnicity.  I used a WITH clause, JOINS and aggregation to find the scores above and below average.

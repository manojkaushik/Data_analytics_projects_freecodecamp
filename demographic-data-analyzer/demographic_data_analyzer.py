import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round(((df[df['education'] == "Bachelors"].shape[0]) /
                          (df.shape[0])) * 100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  q1 = df['education'] == "Bachelors"
  q2 = df['education'] == "Masters"
  q3 = df['education'] == "Doctorate"
  q4 = df['salary'] == ">50K"

  higher_education = df.loc[q1 | q2 | q3].shape[0]
  lower_education = df.loc[~(q1 | q2 | q3)].shape[0]

  # percentage with salary >50K
  higher_education_rich = round((df.loc[(q1 | q2 | q3) & q4].shape[0] /
                           higher_education) * 100, 1)
  lower_education_rich = round((df.loc[~(q1 | q2 | q3) & q4].shape[0] /
                          lower_education) * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].values.min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  q5 = df['hours-per-week'] == min_work_hours
  num_min_workers = df.loc[q5 & q4].shape[0]

  rich_percentage = round((num_min_workers/df.loc[q5].shape[0])*100, 1)

  # What country has the highest percentage of people that earn >50K?
  df1 = df.loc[q4]['native-country'].value_counts()
  df2 = df['native-country'].value_counts()
  df3 = pd.merge(df1, df2, left_index=True, right_index=True)
  df3['percentage'] = (df3['count_x'].values/df3['count_y'].values)*100
  
  highest_earning_country = df3.index[df3['percentage'] == df3['percentage'].max()].values[0]
  highest_earning_country_percentage = round(df3['percentage'].max() ,1)

  # Identify the most popular occupation for those who earn >50K in India.
  q6 = df['native-country'] == 'India'
  df4 = df[q4 & q6]['occupation'].value_counts()
  top_IN_occupation = df4.index[df4 == df4.max()].values[0]

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }

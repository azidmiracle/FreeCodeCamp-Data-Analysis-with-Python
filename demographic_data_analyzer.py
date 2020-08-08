import pandas as pd
import numpy as np # linear algebra

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = pd.Series(data=df['race'].to_numpy()).value_counts(dropna=True)

    # What is the average age of men?
    all_male=df[df['sex'] == 'Male']
    average_age_men = round(pd.Series(data=all_male['age'].to_numpy()).mean(),1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education-num']==13 ])/len(df))*100,1)
   
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education=df[(df['education']=='Bachelors')|(df['education']=='Masters') |(df['education']=='Doctorate')]

    #data not in higher_education
    lower_education=df[~((df['education']=='Bachelors')|(df['education']=='Masters') |(df['education']=='Doctorate'))]


    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[(higher_education['salary']=='>50K')])/len(higher_education))*100,1)

    lower_education_rich = round((len(lower_education[(lower_education['salary']=='>50K')])/len(lower_education))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = pd.Series(data=df['hours-per-week']).min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = (len(df[(df['salary']=='>50K') & (df['hours-per-week']==min_work_hours)])/(len(df[df['hours-per-week']==min_work_hours ])))*100

    # What country has the highest percentage of people that earn >50K?
    #filter countries with 50k
    grouped_country_persalary=df.groupby(['native-country','salary'])
    grouped_country_persalary=grouped_country_persalary['native-country'].aggregate([np.size]).rename(columns={'size':'>50k_size'})
    grouped_country_persalary=grouped_country_persalary.reset_index()
    group_rich=grouped_country_persalary[grouped_country_persalary['salary']=='>50K']
    group_rich=group_rich.set_index('native-country')

    #grouped all the compile
    grouped_all_coutries=df.groupby('native-country')
    grouped_all_coutries=grouped_all_coutries['native-country'].aggregate([np.size]).rename(columns={'size':'total_size'})
    grouped_all_coutries=grouped_all_coutries.reset_index()
    grouped_all_coutries=grouped_all_coutries.set_index('native-country')
    
    #merged the two results to create one table... native-country is the index... 
    df_combined=pd.concat([group_rich,grouped_all_coutries],axis=1,join='inner')
    #print(df_combined)
    #get the maximum value IndexError
    result=df_combined['>50k_size']/df_combined['total_size']
    #print(result)
    highest_earning_country=(result.idxmax())

   # highest_earning_country = pd.Series(data=df[df['salary']=='<=50K']['native-country'].to_numpy()#//).value_counts()#.idxmax(skipna=True)
 
    highest_earning_country_percentage = result.max()
    highest_earning_country_percentage = round(highest_earning_country_percentage*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = pd.Series(data=df[(df['salary']=='>50K') & (df['native-country']=='India')]['occupation'].to_numpy()).value_counts().idxmax(skipna=True)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

#create a function tocheck if the the cholesterol or gluc is good
def isGood(col):
  if(col==1):
    return 0
  else:
    return 1

#create function to check if overweight
def isOverweight(weight,height):
  '''Add an 'overweight' column to the data. To determine if a person is overweight, 
  first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. 
  If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.'''
  bmi=weight/((height/100)**2)

  if (bmi>25):
    return 1
  else:
    return 0

# Add 'overweight' column
df['overweight'] = df.apply (lambda x : isOverweight(x['weight'],x['height']),axis=1)#call the isOverwight function

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']= df.apply (lambda x : isGood(x['cholesterol']),axis=1)#call the isGood function
df['gluc']= df.apply (lambda x : isGood(x['gluc']),axis=1)#call the isGood function



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

    #grouped based on cardio, variable and value. Return count for 1 and 0 in value column
    #the result is in series format
    df_cat_series=df_cat.groupby(['cardio','variable','value'])['value'].count()

    #convert the series to datafram
    df_cat=df_cat_series.to_frame()
    
    #rename the value to total since it has the same index name for value
    df_cat=df_cat.rename(columns={"value": "total"})

    #convert all the index to columns
    df_cat=df_cat.reset_index()

    # Draw the catplot with 'sns.catplot()'
    g=sns.catplot(x="variable",y="total",col="cardio",hue="value",data=df_cat,kind="bar", palette="muted")
    fig = g.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = round(df_heat.corr(),1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    mask[np.triu_indices_from(mask)]= True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask,fmt='.1f',annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # linear algebra
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    x_yrs_extended=np.arange(1850,2100,25)
    plt.figure(figsize=(30,10))
    plt.scatter(x=x,y=y,marker='o')
    plt.xticks(range(1850,2100,25))

    # Create first line of best fit
    slope,intercept,r_value,p_value,std_err=linregress(x,y)
    line = [slope*xi + intercept for xi in x_yrs_extended]
    plt.plot(x_yrs_extended,line,'r',label='fitted line')

    # Create second line of best fit
    df_2020=df[df['Year']>=2000]
    x_2000=df_2020['Year']
    y_2000=df_2020['CSIRO Adjusted Sea Level']
    slope_2,intercept_2,r_value_2,p_value_2,std_err_2=linregress(x_2000,y_2000)
    line_2 = [slope_2*xi + intercept_2 for xi in x_yrs_extended]
    plt.plot(x_yrs_extended,line_2,'r',label='fitted line 2')


# Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()  
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
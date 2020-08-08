import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df=df.set_index('date')

#lower_q=df.quantile(0.025)

#upper_q=df.quantile(0.975)

# Clean data
df=df[(df['value'] >= df.quantile(0.025).value) & (df['value'] <= df.quantile(0.975).value)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(25,10))
    df.plot(kind='line', ax=ax)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Draw bar plot
    #convert to datetime
    df.index=pd.to_datetime(df.index)
    #group the data by year
    #add new columns for year and month
    df['year']=df.index.year
    df['month']=df.index.month

    df_bar=df.groupby(['year','month']).mean()
    df_bar=df_bar.unstack()
    
    #draw bar chart
    fig, ax = plt.subplots(figsize=(15,10))
    df_bar.plot(kind='bar', ax=ax)
    ax.legend(["January", "February",'March','April','May','June','July','August','September','October','November','December'],title="Months");
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,[ax1,ax2]=plt.subplots(1,2,figsize=(20,10))

    sns.boxplot(x='year',y='value',data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    sns.boxplot(x='month',y='value',data=df_box, ax=ax2,order= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

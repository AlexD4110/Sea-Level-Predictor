import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') #Read the data from the csv file
    
    # Create scatter plot
    plt.figure(figsize=(12, 8))  # Define the figure size
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='turquoise', marker='o', label='Data')  # Scatter plot
    
    # Create first line of best fit (using all data)
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_range_all = pd.Series(range(df['Year'].min(), 2051))  # Year range from the minimum year to 2050
    plt.plot(year_range_all, slope_all * year_range_all + intercept_all, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]  # Filter data from 2000 onwards
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    year_range_recent = pd.Series(range(2000, 2051))  # Year range from 2000 to 2050
    plt.plot(year_range_recent, slope_recent * year_range_recent + intercept_recent, color='green', label='Best Fit Line (2000 Onwards)')
    
    # Add labels and title
    plt.title('Rise in Sea Level')  # Title
    plt.xlabel('Year')  # X-axis label
    plt.ylabel('Sea Level (inches)')  # Y-axis label
    plt.legend()  # Display the legend
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
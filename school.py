
"""
    import weather dataset.describe data and its structure. discuss how to customize visualiation
    in python using matplotlib or seaborn. create a plot for temperature over time from weather_data.csv,
    modifying colors,titles,and labels. provide the code and explain your design. interpret result.Download file
"""

"""
    Import dataset on sales. Describe the data structure and dataset. Perform descriptive analysis.
    create a histogram for the sales_ammount column in the dataset sale_data.csv using matplotlib
    Include the code and discuss the insights gained from the histogram regarding sales distribution. interpret result  in detail using appropriate graphs. download file
"""

import pandas as pd

weather_data = pd.read_csv('weather_data.csv')

# Describe the dataset
print(weather_data.describe())  
print(weather_data.info())
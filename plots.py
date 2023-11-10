# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:25:02 2023

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('data.csv')

# Function to create line plot
def create_line_plot(data, x_col, y_col, hue_col, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    for hue_value in data[hue_col].unique():
        subset = data[data[hue_col] == hue_value] 
        plt.xticks(rotation=90)
        plt.plot(subset[x_col], subset[y_col], label=hue_value)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# Function to create bar plot
def create_bar_plot(data, x_col, y_col, hue_col, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    
    data.groupby([x_col, hue_col])[y_col].mean().unstack().plot(kind='bar', width = 0.6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=hue_col)
    plt.show()

# Function to create box plot
def create_box_plot(data, x_col, y_col, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    data.boxplot(column=y_col, by=x_col)
    
    plt.title(title)
    plt.suptitle('')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Line plot
create_line_plot(df, 'Country', 'Mean BMI', 'Gender', 'Mean BMI across Countries by Gender', 'Country', 'Mean BMI')

# Bar plot
create_bar_plot(df, 'Country', 'Mean BMI', 'Gender', 'Mean BMI across Countries by Gender', 'Country', 'Mean BMI')

# Box plot
create_box_plot(df, 'Gender', 'Mean BMI', 'Distribution of Mean BMI by Gender', 'Gender', 'Mean BMI')
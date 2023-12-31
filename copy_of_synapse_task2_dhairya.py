# -*- coding: utf-8 -*-
"""Copy of Synapse_Task2_Dhairya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S_6xm7pcpc-A-zLZsW3rVc4FPvgDscg-

# Synapse - Task 2

![image.png](data:image/png;base64,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)

Run the following cell to import your google drive.
"""

from google.colab import drive
drive.mount("/content/gdrive")

"""Run the following cell to import the required libraries."""

import pandas as pd
import matplotlib.pyplot as plt

"""## Task 2.1

For aspiring data scientists and machine learning enthusiasts, it is vital that they understand the coding environment. We normally use a jupyter notebook for most of our programming. To understand its importance, lets perform a small exercise.

We are given 2 datasets, they have data of certain students from 2 different branches and their respective divisions.

Download the datasets from the links given below -

Task2p1_0 - https://drive.google.com/file/d/1sCGCErnf2iC_qKUHcGLrt2O2HwuiwZYD/view?usp=sharing

Task2p1_1 - https://drive.google.com/file/d/1Kb_TcAEfsUGi-KPZpsh8pXBaxfs4AsHh/view?usp=sharing

Create a folder named 'Synapse' in your google drive and upload the datasets 'Task2p1_0' and 'Task2p1_1' there.

###Python Script
"""

data = pd.read_csv("/content/gdrive/MyDrive/Synapse/Task2p1_0.csv")
data
data = pd.read_csv("/content/gdrive/MyDrive/Synapse/Task2p1_1.csv")
data

from google.colab import drive
drive.mount('/content/drive')

"""###Jupyter Notebook"""

data = pd.read_csv("/content/gdrive/MyDrive/Synapse/Task2p1_0.csv")

data

data = pd.read_csv("/content/gdrive/MyDrive/Synapse/Task2p1_1.csv")

data

"""We are given a tabular dataset that consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.

Download the dataset from the link given below -

https://drive.google.com/file/d/1VGTLXJX_W4Faamfjp5VPM6Amqxw4GMDB/view?usp=drive_link

Create a folder named 'Synapse' in your drive and upload the .csv file there.

Run the following cell, once the steps mentioned above are completed.
"""

df = pd.read_csv("/content/gdrive/MyDrive/Synapse/netflix_titles.csv")
df

"""The dataset contains 8807 rows

## Task 2.1 - Preprocessing

Display the first 10 elements of the dataframe.
"""

df.head(10)

"""It is very important to clean the dataset before it is used. For this, remove all the rows from the dataset that have NaN values.

Once the rows are dropped, you will see that there is discontinuity in the dataframe. Thus, don't forget to reset the indices.

Failing to do so, will result in errors in the following cells.
"""

df.dropna(inplace=True)
df.reset_index(drop=True , inplace = True)
df.shape

"""You should have 5332 rows after cleaning

## Task 2.2 - Operations

Write a code to give me the number of rows that have the release_year as 2021 and type as Movie.
"""

# Your output will be 146, if correct
# Filter the DataFrame to select movies released in 2021
movies_2021 = df[(df['type'] == 'Movie') & (df['release_year'] == 2021)]

# Print the filtered DataFrame
movies_2021.shape[0]

"""Write a code to create a list of all the movies that have the word 'Avengers' in it."""

# Your output will contain 2 movies, if correct
avenger_movies=df[df['title'].str.contains('avengers', case=False)]['title'].tolist()
avenger_movies

"""Display the number of Movies/TV shows per country."""

# Create a copy of the DataFrame with the original index
df_with_original_index = df.copy()

# Replace spaces after commas in the "country" column
df_with_original_index['country'] = df_with_original_index['country'].str.replace(', ', ',')

# Split the countries in the "country" column and explode using the original index
country_counts = df_with_original_index['country'].str.split(',').explode().str.strip()

# Calculate the number of occurrences per country
number_per_country = country_counts.value_counts()
number_per_country

"""Display a new dataframe, that contains only those movies that are present in the Top 5 countries.

(Don't forget to reset the indices again)
"""

# The length of the new dataframe will be 3102, if correct
# Making a list of the top 5 countries
top_countries = number_per_country.head().index.tolist()

# Creating a new DataFrame containing only movies in the top countries
new_df = df[df['country'].str.split(',').explode().str.strip().isin(top_countries).any(level=0)]

# Reset the indices of the new DataFrame
new_df.reset_index(drop=True, inplace=True)

# Create a new DataFrame containing only movies from the new_df DataFrame
new_df_movies = new_df[new_df['type'] == 'Movie']

# Print the new DataFrame containing only movies
new_df_movies

"""## Task 2.3 - Chart

Use the new dataframe to create a Pie Chart on the basis of number of Movies/TV Shows per country.
"""

import matplotlib.pyplot as plt

# calculating the count of movies/TV Shows per country again with the new df
country_count_new = new_df['country'].str.split(',').explode().str.strip().value_counts()


# filtering the country_count_new dataframe to include only top countries
country_counts_top = country_count_new[top_countries]

# making the pie chart
plt.figure(figsize=(8,7))
plt.pie(country_counts_top, labels=country_counts_top.index, autopct='%1.1f%%', startangle=180)
plt.title('Distribution of Movies/TV Shows in Top 5 Countries')
plt.axis('equal')  # equal aspect ratio here ensures that the pie chart is circular
plt.show()


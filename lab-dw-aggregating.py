#!/usr/bin/env python
# coding: utf-8

# # Lab | Data Aggregation and Filtering

# In this challenge, we will continue to work with customer data from an insurance company. We will use the dataset called marketing_customer_analysis.csv, which can be found at the following link:
# 
# https://raw.githubusercontent.com/data-bootcamp-v4/data/main/marketing_customer_analysis.csv
# 
# This dataset contains information such as customer demographics, policy details, vehicle information, and the customer's response to the last marketing campaign. Our goal is to explore and analyze this data by first performing data cleaning, formatting, and structuring.

# 1. Create a new DataFrame that only includes customers who have a total_claim_amount greater than $1,000 and have a response of "Yes" to the last marketing campaign.

# 2. Using the original Dataframe, analyze the average total_claim_amount by each policy type and gender for customers who have responded "Yes" to the last marketing campaign. Write your conclusions.

# 3. Analyze the total number of customers who have policies in each state, and then filter the results to only include states where there are more than 500 customers.

# 4. Find the maximum, minimum, and median customer lifetime value by education level and gender. Write your conclusions.

# In[3]:


#1

import pandas as pd

url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/marketing_customer_analysis.csv"
df = pd.read_csv(url)

print(df)


# In[6]:


#2

import pandas as pd

# Step 1:
yes_responses_df = df[df['response'] == 'Yes']

# Step 2:
average_total_claim_amount = yes_responses_df['total_claim_amount'].mean()

# Step 3:
print("Average total claim amount for customers who responded 'Yes':", average_total_claim_amount)


# ## Bonus

# 5. The marketing team wants to analyze the number of policies sold by state and month. Present the data in a table where the months are arranged as columns and the states are arranged as rows.

# 6.  Display a new DataFrame that contains the number of policies sold by month, by state, for the top 3 states with the highest number of policies sold.
# 
# *Hint:*
# - *To accomplish this, you will first need to group the data by state and month, then count the number of policies sold for each group. Afterwards, you will need to sort the data by the count of policies sold in descending order.*
# - *Next, you will select the top 3 states with the highest number of policies sold.*
# - *Finally, you will create a new DataFrame that contains the number of policies sold by month for each of the top 3 states.*

# 7. The marketing team wants to analyze the effect of different marketing channels on the customer response rate.
# 
# Hint: You can use melt to unpivot the data and create a table that shows the customer response rate (those who responded "Yes") by marketing channel.

# External Resources for Data Filtering: https://towardsdatascience.com/filtering-data-frames-in-pandas-b570b1f834b9

# In[ ]:


# your code goes here


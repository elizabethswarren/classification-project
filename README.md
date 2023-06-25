# Telco Customer Churn

# Project Description
Customer churn is the portion of customers that stopped using a company's product or service during a period of time. In the case of our telco company, churn is defined as a customer that ended their phone and/or internet service with us for a rival provider. My intention with this project is to build a model that can accurately predict whether a customer churn will occur or not for a given customer.

# Project Goal
  * Find what drives customer churn
  * Use these findings to create a model to predict churn
  * Suggest actions based on discoveries

# Initial Thoughts
My initial hypothesis is that high charges will be one of the main drivers of churn.

# The Plan
  * Acquire data
    
  * Prepare data
    * Drop columns that had no useful information
    * Clean the total charges column and converted values to floats.
    * Fill null values in total charges with median value of column.
       * Median was used due to outliers skewing the mean.
    * Encoded categorical data.
    * Split the data into train, validate, split in a 50, 30, 20 split, stratified on churn.
      
  * Explore the data
    * Answer the questions:
      * Is contract type related to churn?
      * Is internet service type related to churn?
      * Are monthly charges related to churn?
      * Are total charges related to churn?
      * Is tenure related to churn?
        
  * Develop a model to predict churn
    * Use accuracy as my evaluation metric.
    * Baseline will be the percentage of non churning customers.
   
  * Make conclusions.

# Data Dictionary
|**Feature**|**Description**|
|:-----------|:---------------|
|Gender  | Male or Female|
|Senior Citizen| Whether a customer is a senior citizen or not.|
|Partner| Whether a customer has a partner.|
|Dependents| Whether a customer has dependents.|
|Tenure| Length of time customer has been with Telco, measured in months.|
|Monthly Charges| Amount paid each month by customer.|
|Total Charges| Total amount paid by customer over tenure.|
|Churn (Target)| Yes or No, if a customer has churned or not.|
|Contract Type| The different lengths of contracts our customers have signed; month to month, one year, and two year.|
|Internet Service Types| Types of internet service that our customers use; DSL, Fiber Optics, and None.|

# Steps to Reproduce
  * Clone this repo
  * Acquire data
  * Put the data in the same file as cloned repo
  * Run the final_report notebook

# Conclusions
  * Percentage of churn is approximately 26%
  * Contract type is a driver of churn
  * Monthly charges are a driver of churn
  * Tenure is an indicator of churn

# Next Steps
  * Look into cleaning and encoding data by mapping 'Yes' and 'No' values as bool for ease of use.
  * Explore multivariate feature relationships:
    * Do longer tenured pay more or less in monthly charges and what type of contracts do they hold?
    * Are month to month customers paying higher monthly charges on average?
  * Create a column with the number of additional services per customer for use as a feature.

# Recommendations
  * Incentivise customers to move from month to month contracts to longer ones.
  * Reward loyal customers to possibly increase tenure.
  

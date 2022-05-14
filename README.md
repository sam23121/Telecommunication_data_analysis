# Telecom-Data-Analysis
## User Overview analysis
For the telecom dataset
the following sub-tasks were conducted:

    - I identified the top 10 handsets used by the customers.
    - Then, identified the top 3 handset manufacturers
    - Next,I identify the top 5 handsets per top 3 handset manufacturer
● Next I Aggregate per user the following information in the column

    - number of xDR sessions
    - Session duration
    - the total download (DL) and upload (UL) data
    - the total data volume (in Bytes) during this session for each application
    
## User Engagement

● for this part of the analysis I used the following engagement metrics:

     - sessions frequency
     - the duration of the session
     - the sessions total traffic (download and upload (bytes))

● Based on the above I wrote a python script :
        - I Aggregate the above metrics per customer id (MSISDN) and report the top 10 customers per engagement metric
        - Normalize each engagement metric and run a k-means (k=3) to classify customers in three groups of engagement.
        - Compute the minimum, maximum, average & total non- normalized metrics for each cluster. 
        - Aggregate user total traffic per application and derive the top 10 most engaged users per application
        - Plot the top 3 most used applications using appropriate charts.
        - Using k-means clustering algorithm, group users in k engagement clusters based on

## User Experience

###### Aggregate, per customer, the following information (treat missing & outliers by replacing by the mean or the mode of the corresponding variable):
 - Average TCP retransmission
- Average RTT
- Handset type
- Average throughput

Compute & list 10 of the top, bottom and most frequent for the tcp retransmission, Round trip delay and Throughput values in the dataset

## User Satisfaction

- user satisfaction was calculated based on experience and engagement
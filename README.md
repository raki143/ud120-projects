# Investigating Enron's scandal using Machine Learning

## Introduction
> [In addition to being the largest bankruptcy reorganization in American history at that time, Enron was cited as the biggest audit failure](http://en.wikipedia.org/wiki/Enron_scandal)

From a $90 price per share, to a $1 value represents the huge value loss and scam that happened in Enron. This case has been
a point of interest for machine learning analysis because of the huge real-world impact that ML could help out and try to figure out what went wrong and how to avoid it in the future. It would be of great value to find a model that could potentially predict these types of events before much damage is done, so as to permit preventive action. Corporate governance, the stock market, and even the Government would be quite interested in a machine learning model that could signal potential fraud detections before hand.

## Enron Data
The interesting and hard part of the dataset is that the distribution of the non-POI's to POI's is very skewed, given that from the 146 there are only 11 people or data points labeled as POI's or guilty of fraud. We are interested in labeling every person in the dataset
into either a POI or a non-POI (POI stands for *Person Of Interest*). More than that, if we can assign a probability to each person to see what is the chance she is POI, it would be a much more reasonable model given that there is always some uncertainty.


## Data Processing
All features in the dataset are either financial data or features extracted from emails. Financial data includes features like salary and bonus while the email features include number of messages written/received and to whom/form.

There are 2 clear outliers in the data, **TOTAL** and **THE TRAVEL AGENCY IN THE PARK**. The first one seems to be the sum total of all the other data points, while the second outlier is quite bizarre. Both these outliers are removed from the dataset for all the analysis. Also all features are scaled using the **MinMaxScaler** (although it is not included in the final model).

### New features
From the initial dataset, 5 new features where added, you can find more details in the table below:

|Feature | Description     |
|--------|-----------------|
|Ratio of POI messages | POI related messages divided over the total messages from the person |
|Log of financials (multiple) | Financial variables with logarithmic transformation |
|Square of financials (multiple) | Financial variables with squared transformation |

The reasoning behind the **ratio of POI messages** is that we expect that POI's contact each other relatively more often than with non-POI's and the relationship might be non-linear. We also can expect that the financial gains for POI's is actually non-linear, that is why applying a logarithmic and a square transformation to the original features, and it should improve many algorithms.

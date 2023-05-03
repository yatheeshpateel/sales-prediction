# Sales-Prediction 
This is a case study of predicting future sales using machine learning algorithms. The goal is to build a model that can predict the sales based on historical sales data.

# Prerequisites
To run this project, you will need the following:
Python 3.x             
Jupyter Notebook            
scikit-learn library          
pandas library       
numpy library           

# Sales Prediction (Case Study)        
given some information about students like:         

TV: Advertising cost spent in dollars for advertising on TV;              
Radio: Advertising cost spent in dollars for advertising on Radio;          
Newspaper: Advertising cost spent in dollars for advertising on Newspaper;               
Sales: Number of units sold;                      

# explaination of the code 

# step 1
The code provided imports necessary libraries such as numpy, pandas, seaborn, matplotlib, plotly.express, and plotly.graph_objects. It then reads a CSV file named "Advertising.csv" into a Pandas DataFrame named dataset. The dataset contains 200 rows and 5 columns, including Unnamed: 0, TV, Radio, Newspaper, and Sales.

# step 2
Next, the code uses various functions such as head(), info(), describe(), and isnull().sum() to check the content and structure of the dataset.


# step 3
The code then creates scatter plots of the variables Sales and each of TV, Radio, and Newspaper using matplotlib.


# step 4
After that, the code prepares the data for modeling by dividing the data into input features X and output variable y and splitting the data into training and testing sets using train_test_split() from sklearn.model_selection.


# step 5
Finally, the code creates an instance of LinearRegression() from sklearn.linear_model, fits the training data to the model using .fit(), predicts the output variable for the test data using .predict(), and stores the results in y_pred. 

#RESULT
![Screenshot 2023-05-03 213833](https://user-images.githubusercontent.com/120399980/235975939-ba7b3114-560a-423c-b957-9ea00f9b1d9e.png)

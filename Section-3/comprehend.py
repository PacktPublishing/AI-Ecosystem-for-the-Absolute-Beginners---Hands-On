import pandas as pd

# Import the boto3 library for interacting with AWS services
import boto3


#Read the data from the CSV file 'data.csv' into a pandas DataFrame and assign it to the variable 'data'
data = pd.read_csv('data.csv')
data



#This function iterated through the whole dataframe 'data', collecting them into a list 'l' and a single string 'text'. Returning both 'text' and 'l'
def df_function(data):
    text = ""
    l = []
    for i in range(len(data)):
        l.append(data['Review'][i])
        text = text + data['Review'][i]
    return text,l



#calling df_function and storing the elements it return in 'paragraph' and 'list1'
paragraph, list1 = df_function(data)

#creating a client object for the AWS Comprehend service. Make sure to enter your unique access_key and secret_key
comprehend = boto3.client('comprehend', region_name = 'us-east-1', aws_access_key_id = '--access_key--', aws_secret_access_key = '--secret_key--')
final_response = []

#iterate throught each text in 'list1'
for i in list1:
    #Perform sentiment analysis on the text using AWS Comprehend
    response = comprehend.detect_sentiment(Text = i, LanguageCode = "en")

    #Append the result to the 'final_response' list
    final_response.append(response["Sentiment"])
    

#creating a dataframe containing serial no, reviews and sentiment results
final_data = pd.DataFrame({"Sr. No": range(1, len(data['Review']) + 1),
                           'Reviews': data['Review'],
                            "Result": final_response})


#displaying the final result
final_data







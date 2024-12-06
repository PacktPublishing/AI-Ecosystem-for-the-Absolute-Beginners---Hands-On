import json 
import boto3 #library which provides an interface to interact with various AWS services

#creating a client object for the Rekognition service
api = boto3.client('rekognition') 

def lambda_handler(event, context):
    #provide the name of your S3 bucket in the sbucket variable 
    sbucket = "__bucket-name__"     

    #name of the image in the image variable
    image = "__image-name__.jpeg"  

    #using the detect_faces method of the Rekognition client object
    result = api.detect_faces(Image = {'S3Object':{'Bucket': sbucket, 'Name': image}}, Attributes=['ALL']) 

    #iterating over the list of face details returned by Rekognition and print them in a json format
    for face in result['FaceDetails']: 
        print(json.dumps (face, indent = 2)) 

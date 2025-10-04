import streamlit as st
import os
import boto3
import torch
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client("s3")
bucket_name = os.getenv("BUCKET_NAME") 

local_path = "models/tiny_bert_sentiment"
s3_prefix = "ml-models/tiny_bert_sentiment"

def download_folder(bucket_name, local_path, s3_prefix):
    os.makedirs(local_path, exist_ok=True)
    
    paginator = s3.get_paginator('list_objects_v2')
    
    for result in paginator.paginate(Bucket = bucket_name, Prefix = s3_prefix):
        if 'Contents' in result:
            for key in result['Contents']:
                s3_key = key["Key"]
                local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))
                s3.download_file(bucket_name, s3_key, local_file)


st.header("Machine Learning")

model_button = st.button("Download Model")
if model_button:
    with st.spinner("Downloading... Please wait!"):
        download_folder(bucket_name, local_path, s3_prefix)
    
    st.info("Download Complete")
        

text = st.text_area("Enter Your Review")

predict_button = st.button("Predict")

if predict_button:
    with st.spinner("Getting results"):
        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        classifier = pipeline('text-classification', model = './models/tiny_bert_sentiment', device=device)
    
        output = classifier(text)
     
    st.write(output)
    


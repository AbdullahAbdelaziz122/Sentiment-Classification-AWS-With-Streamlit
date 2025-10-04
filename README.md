# Sentiment Classification with AWS S3 & Streamlit Deployment

This project demonstrates a Sentiment classification pipeline using a machine learning model Tiny Bert trained on IMDB Movies reviews stored on AWS S3 and deployed via Streamlit Hub.

## Features

- **Model Storage:** Trained sentiment classification model hosted on AWS S3.
- **Web Interface:** Interactive Streamlit app for real-time sentiment prediction.
- **Easy Deployment:** Simple setup for local or cloud deployment.

## Project Structure

```
.
├── app.py                # Streamlit application
├── requirements.txt      # Python dependencies
└── README.md
```

## Getting Started


### Installation

```bash
git clone https://github.com/abdullahabdelaziz122/sentiment_classification_AWS_Deployment_With_Streamlit.git
cd sentiment_classification_AWS_Deployment_With_Streamlit
pip install -r requirements.txt
```


### Usage

1. **Run Streamlit App:**
    ```bash
    streamlit run app.py
    ```

2. **Download Model from S3:**  
    The app automatically fetches the model from your specified S3 bucket.


3. **Interact:**  
    Enter text in the web interface to get sentiment predictions.


## Customization

- Set your AWS credentials as environment variables or configure via `~/.aws/credentials`.

- Update S3 bucket/model path in `app.py`.

- Modify UI components in Streamlit as needed.
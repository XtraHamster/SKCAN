# SKCAN - SKin CANcer recognition app

This app was made for my bachelor thesis on CTU in Prague. Full title of my bachelor thesis is "Skin cancer classification using machine learning algorithms". Main object was to make classification model for recognizing 7 types of skin lesions. As a superstructure for the model, I created this simple application for easy and quick testing

## App
Application is available on URL: https://skcan.herokuapp.com
The application is uploaded free of charge on a server with a limited launch time. It is necessary to turn on the server for testing purposes. If you are interested, contact me at martinkrecek98@seznam.cz

## App Output
Final result - diagnosis of the probability of seven diseases of skin lesions

![image](https://user-images.githubusercontent.com/60604602/122686800-74c1c680-d213-11eb-8682-6235ac99b821.png)

## Dataset:
For training my model I used this dataset called "HAM10000" which contains over 10000 pictures of skin leisons.
https://arxiv.org/abs/1902.03368

## Directories descriptions
#### Model
- contains trained model used in classify.py

## Files for our Streamlit App

#### classify.py
- get_model(): Loads the saved model into cache using streamlit's "@st.cache" feature.
- predict(): Takes an image as input from the function parameter, preprocesses it and feeds it to the model for results.

#### app.py
- Contains the front-end code for the streamlit app.
- Imports the predict() function fetches the result and displays it.

#### Procfile
A Procfile is a file which describes how to run your application.

#### requirements.txt
This has all the dependencies required to deploy our application on Heroku

## Run this app on your system.
### Requirements
- Python 3.6+
- NumPy 1.19.5
- Pillow 8.1.2
- TensorFlow-cpu 2.3.0
- Streamlit 0.78.0
- Pandas 1.1.3
- Plotly 4.14.3

### To run it on your system
- Install all the dependencies
- Clone this repository
- You need the Streamlit App folder to run this application.
- In your Command line/Terminal go to the directory where you have upload.py file then type 
#### streamlit run app.py



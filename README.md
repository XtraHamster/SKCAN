# SKCAN
## SKin CANcer recognition app made for my bachelor thesis

## App:
- Link: 



## App Output

## Project overview



## Dataset:
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
- NumPy
- Pillow
- TensorFlow 2.x
- Streamlit 

### To run it on your system
- Install all the dependencies
- Clone this repository
- You need the Streamlit App folder to run this application.
- In your Command line/Terminal go to the directory where you have upload.py file then type 
#### streamlit run app.py



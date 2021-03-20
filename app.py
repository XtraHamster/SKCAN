import streamlit as st 
from tensorflow.keras.preprocessing.image import load_img
import pandas as pd
import classify 

labels = ['akiec', 'bcc', 'bkl', 'df', 'mel','nv', 'vasc']

st.title("SKCAN")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:

        image = load_img(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.write("Result...")
                label = classify.predict(uploaded_file)
                label = [round(i * 100) for i in label]
                label = [str(i) + ' %' for i in label]
                st.write(pd.DataFrame({
                        'type': labels,
                        'prediction': label
                }))
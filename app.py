import streamlit as st 
from tensorflow.keras.preprocessing.image import load_img
import pandas as pd
import classify
import os 
from PIL import Image
import webbrowser
import time
import plotly.express as px

class plot_type:
    def __init__(self,data):
        self.data = data
        self.fig=None
        self.update_layout=None

    def bar(self,x,y,color,color_continuous_scale):
        self.fig=px.bar(self.data,x=x,y=y, color=color, color_continuous_scale=color_continuous_scale, width=1000)
        
    def set_title(self,title):
        


        self.fig.update_layout(
                title=f"{title}",
                    yaxis=dict(tickmode="linear"),
                    xaxis=dict(tickmode="linear", tick0=0, dtick=10, range=[0,100]),
                    paper_bgcolor='rgba(255,255,255,1)',
                    plot_bgcolor='rgba(255,255,255,1)',
                    font=dict(color='black',size=18))


    def plot(self):
        st.write(self.fig)



labels = ['akiec', 'bcc', 'bkl', 'df', 'mel','nv', 'vasc']

names = ['Actinic keratoses and Bowen\'s disease  ', 
          'Basal cell carcinoma  ', 
          'Benign keratosis  ',  # (solar lentigines / seborrheic keratoses and lichen-planus like keratose)
          'Dermatofibroma  ', 
          'Melanoma  ',
          'Melanocytic nevi  ', 
          'Vascular skin leisons  ' # (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)
          ]

urls = ['https://dermoscopedia.org/Actinic_keratosis_/_Bowen%27s_disease_/_keratoacanthoma_/_squamous_cell_carcinoma',
        'https://dermnetnz.org/topics/basal-cell-carcinoma/',
        'https://dermnetnz.org/topics/seborrhoeic-keratosis/',
        'https://dermnetnz.org/topics/dermatofibroma/',
        'https://dermnetnz.org/topics/melanoma/',
        'https://dermnetnz.org/topics/melanocytic-naevus/',
        'https://dermoscopedia.org/Vascular_lesions'
        ]

info = [
        ['**Actinic keratoses** typically arise on chronically sun-damaged skin and represent the most common lesions in the spectrum of keratinocyte skin cancer. Clinically they present as multiple pink macules or papules with a variably scaly surface.', '**Bowen’s disease** represents an intraepithelial carcinoma or in situ Squamous cell carcinoma (SCC). The most frequent clinical presentation is an erythematous scaly patch or slightly elevated plaque.'],
        ['**Basal cell carcinoma** is a common, locally invasive, keratinocyte cancer (also known as nonmelanoma cancer). It is the most common form of skin cancer. Basal cell carcinoma is also known as rodent ulcer and basalioma. Patients with Basal cell carcinoma often develop multiple primary tumours over time.'],
        ['**Seborrheic keratosis** are benign epithelial lesions that can appear on any part of the body except for the mucous membranes, palms, and soles. The lesions are quite prevalent in people older than 30 years and some people have hundreds of them. The etiology of seborrheic keratoses remains unclear.'],
        ['**Dermatofibromas** are prevalent cutaneous lesions that most frequently affect young to middle-aged adults, with a slight predominance in females. Clinically, dermatofibromas appear as firm, single or multiple papules/nodules with a relatively smooth surface and predilection for the lower extremities. Characteristically, upon lateral compression of the skin surrounding dermatofibromas, the tumors tend to pucker inward producing a dimple-like depression in the overlying skin.'],
        ['**Melanoma**, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, inside your body, such as in your nose or throat.'],
        ['**Melanocytic naevus**, or mole, is a common benign skin lesion due to a local proliferation of pigment cells (melanocytes). It is sometimes called a naevocytic naevus or just \'naevus\'. A brown or black melanocytic naevus contains the pigment melanin, so may also be called a pigmented naevus. A melanocytic naevus can be present at birth (a congenital melanocytic naevus) or appear later (an acquired naevus). There are various kinds of congenital and acquired melanocytic naevi.'],
        ['**Vascular skin lesions** comprise of all skin disease that originate from or affect blood or lymphatic vessels, including malignant or benign tumors, malformations and inflammatory disease. While some vascular lesions are easily diagnosed clinically and dermoscopically, other vascular lesions can be challenging as many of them share similar dermoscopic features. This chapter reviews all vascular lesions for which dermoscopic features were previously described.']
]

app_formal_name = "SKCAN"

# Start the app in wide-mode
st.set_page_config(
    layout="centered", page_title=app_formal_name,
)

st.title("SKCAN")


st.markdown('___')
uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg'])
if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=False)

        st.write("")
        st.markdown('___')
        if st.button('Predict'):
                with st.spinner(text='In progress...'):
                        time.sleep(2)
                label = classify.predict(image)
                label = [round(i * 100) for i in label]

                data = [label, labels]
                data_pd = pd.DataFrame({
                        'Name': names,
                        'Value': label
                })

                data_test = pd.DataFrame({
                        'Name': ['test'],
                        'Value': [100]
                })

                #data_pd = data_pd.append(data_test)
                #st.write(data_test)
                #st.write(data_pd)


                #fig = px.bar(data_pd, x='labels', y='value',
                        #hover_data=['lifeExp', 'gdpPercap'], 
                        #color='lifeExp',
                        #labels={'pop':'population of Canada'}, 
                 #       height=400)
                #st.write(fig.show())

                # results
                bar1 = plot_type(data_pd)
                bar1.bar("Value","Name","Value","deep")
                bar1.set_title("Result:")
                bar1.plot()
                
                # info
                st.markdown('___')
                st.subheader('Additional info')
                st.markdown('___')

                about = st.beta_expander(names[0])
                with about:
                        st.markdown(info[0][0])
                        st.write('Link to additional information: [LINK](https://dermoscopedia.org/Vascular_lesions)')
                        st.markdown(info[0][1])
                        st.write('Link to additional information: [LINK](https://dermoscopedia.org/Bowen%27s_disease)')
                             
                about = st.beta_expander(names[1])
                with about:
                        st.markdown(info[1][0])
                        st.write('Link to additional information: [LINK](https://dermnetnz.org/topics/basal-cell-carcinoma/)')

                about = st.beta_expander(names[2])
                with about:
                        st.markdown(info[2][0])
                        st.write('Link to additional information: [LINK](https://dermnetnz.org/topics/seborrhoeic-keratosis/)')

                about = st.beta_expander(names[3])
                with about:
                        st.markdown(info[3][0])
                        st.write('Link to additional information: [LINK](https://dermnetnz.org/topics/dermatofibroma/)')

                about = st.beta_expander(names[4])
                with about:
                        st.markdown(info[4][0])
                        st.write('Link to additional information: [LINK](https://dermnetnz.org/topics/melanoma/)')

                about = st.beta_expander(names[5])
                with about:
                        st.markdown(info[5][0])
                        st.write('Link to additional information: [LINK](https://dermnetnz.org/topics/melanocytic-naevus/)')

                about = st.beta_expander(names[6])
                with about:
                        st.markdown(info[6][0])
                        st.write('Link to additional information: [LINK](https://dermoscopedia.org/Vascular_lesions)')

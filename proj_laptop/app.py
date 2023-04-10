import streamlit as st
import pandas as pd
import time
import numpy as np
import pickle
import altair as alt
import sklearn
import os
from PIL import Image
from matplotlib import image
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR)
model_path = os.path.join(dir_of_interest,'dataframe.pkl')
df_path = os.path.join(dir_of_interest,'Tesla.csv')
IMAGE_PATH = os.path.join(dir_of_interest, "elon.jpg")


def main():
    st.title(':green[Hello Everyone !] :sunglasses:')
    st.header('**:red[Laptop Price Prediction ]**')
    html_temp = """
    <div style="background-color:#586e75;padding:10px">
    <h2 style="color:white;text-align:center;">Laptop Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    model = pickle.load(open(model_path,'rb'))
    df = pd.read_csv(df_path)
    image = Image.open(IMAGE_PATH)
    st.image(image, caption='Process for ML Model')
    with st.form('form1'):
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        with col1:
            a = st.radio('**RAM:**',
            (df['RAM'].unique()),help='Select the RAM size')
        with col2:
            b = st.selectbox('**Operating System:**',
            (df['Operating_System'].unique()),help='Select the Operating System')
        with col4:
            c = st.radio('**Storage:**',
            (df['Disc Size'].unique()),help='Select the Storage Type')
        with col3:
            d = st.selectbox('**RAM Type:**',
            (df['RAM_Type'].value_counts().index),help='Select the RAM Type')
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Wait for it....'):
                time.sleep(1)
            ram = 0
            os_ = 0
            storage = 0
            ram_type = 0
            if a == '4 GB':
                ram = 1
            elif a == '8 GB':
                ram = 2
            elif a == '16 GB':
                ram = 3
            else:
                ram = 4
            if b == 'Mac':
                os_ = 5
            elif b == 'Windows 11':
                os_ = 4
            elif b == 'Windows 10':
                os_ = 3
            elif b == 'Chrome':
                os_ = 2
            else:
                os_ = 1
            if c == '32GB':
                storage = 1
            elif c == '64GB':
                storage = 2
            elif c == '128GB':
                storage = 3
            elif c == '256GB':
                storage = 4
            elif c == '512GB':
                storage = 5
            elif c == '1TB':
                storage = 6
            else:
                storage = 7
            if d == 'DDR4':
                ram_type = 1
            elif d == 'DDR5':
                ram_type = 2
            elif d == 'LPDDR3':
                ram_type = 3
            elif d == 'LPDDR4':
                ram_type = 4
            elif d == 'LPDDR4X':
                ram_type = 5
            elif d == 'LPDDR5':
                ram_type = 6
            elif d == 'Unified':
                ram_type = 7
            st.success(f"$ {int(model.predict([[os_,ram_type,ram,storage]])[0])}")

if __name__=='__main__':
    main()

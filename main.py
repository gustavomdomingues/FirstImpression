import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import altair as alt

def main():

    st.sidebar.markdown('Developed by **Gustavo Domingues**.')
    st.sidebar.markdown('gustavomdom@gmail.com')

    st.title('First Impressions')
    st.header('Get the first impressions of your dataset using this app!')

    # choose csv file
    st.write('Upload your csv file here (200MB limit):')
    encoding = st.selectbox(label = 'Choose the encoding', options = (['utf-8', 'utf-16', 'utf-32', 'US-ASCII']), index=0)
    uploaded_file = st.file_uploader(label= '', type=['csv'], encoding=encoding)

    if uploaded_file is not None:
    	
    	separator = st.text_input(label='Cell separation character:' , value=',')
    	decimal_indicator = st.selectbox(label = 'Decimal indicator: ', options = (['.', ',']), index=0)
    	data = pd.read_csv(uploaded_file, sep=separator, decimal=decimal_indicator)
    	
    	st.dataframe(data)

    # [tab] Correlations

    # [tab] Features individually

    # imputation

    # categorical treatment

    # standarize / normalize

    # pca (classification)

    # save file
    

if __name__ == '__main__':
    main()
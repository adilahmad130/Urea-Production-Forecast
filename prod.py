import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import requests
import base64

# Provided data for companies
companies = ['NFL', 'RCF', 'MFL', 'BVFCL', 'IFFCO', 'KRIBHCO', 'GSFC', 'CIL', 'SFC', 'Zuari', 'SPIC', 'MCFL',
             'GNFC', 'NFCL', 'CFCL', 'Grasim', 'KFL', 'IPL', 'Narmada Bio', 'KanpurFert', 'MFCL', 'Yara', 'RFCL']

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("WhatsApp Image 2024-06-19 at 14.09.56.jpeg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/adilahmad130/Projects/blob/main/WhatsApp%20Image%202024-06-19%20at%2014.09.56.jpeg?raw=true");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"] > .main::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5); /* Adjust the opacity value as needed */
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Urea Production Forecast')

# Search bar for company name
company = st.selectbox('Select a Company:', companies)
#st.image('iffco.png', use_column_width= False)
# Load the forecast data for the selected company
if company:
    try:
        with open(f'{company}_forecast.pkl', 'rb') as f:
            train_data, forecast = pickle.load(f)
    except FileNotFoundError:
        st.error(f"No forecast data found for {company}")
    else:
        # Plot actual vs. forecasted values
        plt.figure(figsize=(10, 6))
        plt.plot(train_data.index, train_data, label='Actual')
        plt.plot(forecast.index, forecast, label='Forecasted', linestyle='--')
        plt.xlabel('Year')
        plt.ylabel('Urea Production')
        plt.title(f"Urea Production Forecast for {company}")
        plt.legend()
        st.pyplot(plt)

        # Display the forecasted data as a DataFrame
        st.subheader(f'Forecasted Data for {company}')
        forecast_df = pd.DataFrame({'Year': forecast.index, 'Production': forecast.values})
        st.write(forecast_df)

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
#Ahora que tiene una aplicación, lo siguiente que deberá hacer es obtener el conjunto de datos de Uber para recogidas y devoluciones en la ciudad de Nueva York.
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)

data_load_state = st.text('Loading data...done!!!')
st.subheader('Raw data example')
st.write(data.head(10))
#histograma para ver cuáles son las horas de mayor actividad de Uber en la ciudad de Nueva York. Para comenzar, agreguemos un subtítulo justo debajo de la sección de datos sin procesar:
st.subheader('Number of pickups by hours')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

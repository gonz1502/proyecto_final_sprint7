import pandas as pd
import plotly.express as px
import streamlit as st 

st.write('Histograma tipo de vehículos')

car_data = pd.read_csv('vehicles_us.csv')

mostrar = st.button("Mostrar histograma")

if "mostrar" not in st.session_state:
    st.session_state.mostrar = False

if mostrar:
    st.session_state.mostrar = True

if st.session_state.mostrar:
    fig = px.histogram(car_data, x="type", title="Distribución de tipos de vehículo")
    st.plotly_chart(fig, use_container_width=True)
    
st.write('Dispersión precios vehículos')

show = st.button('Gráfico de dispersión precios')

if "show" not in st.session_state:
    st.session_state.show = False
    
if show:
    st.session_state.show = True
    
if st.session_state.show:
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre precio y kilometraje",
        opacity=0.6
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
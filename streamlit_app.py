import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import multiprocessing
import warnings
import seaborn as sns
import datetime as dt
from datetime import datetime
from skimage import io


st.set_page_config(page_title="Exel Pitss",
                   page_icon=":bar_chart:",
                   layout="wide")
st.title("PAP ITESO")

#Importando Librerias Servicios PAP.csv
Data_Pitss = pd.read_csv("C:/Users/crist/Desktop/PAP/Exel Pitss Limpio.csv")
datos = pd.read_csv("C:/Users/crist/Desktop/PAP/Servicios.csv")
datos= datos.fillna(.001)

#st.dataframe(Data_Pitss)


st.sidebar.header("Filtros")
city = st.sidebar.multiselect("Selecciona El Estado",
                              options=Data_Pitss["ServiceRouteName"].unique(),
                              default=Data_Pitss["ServiceRouteName"].unique())

tecnico_ejecutor = st.sidebar.multiselect(
    "Selecciones El Tecnico Ejecuto", options=Data_Pitss["tecnicoEjecutor"].unique(),
    default=Data_Pitss["tecnicoEjecutor"].unique())


seleccion = Data_Pitss.query(
    "ServiceRouteName == @city or tecnicoEjecutor == @tecnico_ejecutor")

st.dataframe(seleccion)

#KPIS



#####SOCNAME

st.markdown("En este apartado hicimos gráficas de tipo de máquina, total de visitas, modelo más solicitado y promedio de horas de uso muestran la cantidad de veces que se solicita cada tipo de máquina, el número total de visitas del tecnico ejecutor, el modelo de máquina que se solicita con mayor frecuencia y el promedio de horas que se utilizan para finalizar un pedido, estos datos pueden ayudar al personal de la empresa a tomar decisiones para sastifacer las necesidades y preferencias de sus clientes.")


Tipo = seleccion.groupby(['SOCNAME'])['SOCNAME'].count()

figura_1 = px.bar(Tipo,x="SOCNAME",y=Tipo.index,
                  orientation=("h"), title= "<b> Tipo De Maquina",
                  color_discrete_sequence=["#0083B8"] * len(Tipo),
                  template="plotly")

#####Numero De Visitas

Visitas = seleccion.groupby(['tecnicoEjecutor'])['NumVisitas'].count()

figura_2 = px.bar(Visitas,x="NumVisitas",y=Visitas.index,
                  orientation=("h"), title= "<b> Total de Visitas",
                  color_discrete_sequence=["#0083B8"] * len(Visitas),
                  template="plotly")


#####Modelo
Modelo = seleccion.groupby(['productModel'])['productModel'].count()

figura_3 = px.bar(Modelo,x="productModel",y=Modelo.index,
                  orientation=("h"), title= "<b> Modelo más solicitado",
                  color_discrete_sequence=["#0083B8"] * len(Modelo),
                  template="plotly")

#####Tiempo

Tiempo = seleccion.groupby(['tecnicoEjecutor'])['horas'].mean()

figura_4 = px.bar(Tiempo,x="horas",y=Tiempo.index,
                  orientation=("h"), title= "<b> Promedio De Horas",
                  color_discrete_sequence=["#0083B8"] * len(Tipo),
                  template="plotly")

#####Ratio



a, b, c,d = st.columns(4)

a.plotly_chart(figura_1, use_container_width = True)
b.plotly_chart(figura_2, use_container_width = True)
c.plotly_chart(figura_3, use_container_width = True)
d.plotly_chart(figura_4, use_container_width = True)

#Frecuencia de Estatus
st.title("Modelo")

st.header("Frecuencia de Estatus")
freq=pd.value_counts(datos['Estatus'])
st.dataframe(freq)

st.header("Frecuencia Relativa")
frecuencia=pd.DataFrame(freq)
frecuencia.columns = ["Frec_abs"]
frecuencia["Frec_rel_%"] = 100*frecuencia["Frec_abs"]/len(datos)
st.dataframe(frecuencia)
###imagenes
st.header("Frecuencia Relativa de Dias transcurridos para que el proceso sea relativo")
img = io.imread("C:/Users/crist/Desktop/Sin título-4.png")
st.image(img, caption='Jamón')

img1 = io.imread("C:/Users/crist/Desktop/1.png")
st.image(img1, caption='Observado lo anterior, podemos descartar a partir del día 23 porque el nivel de significancia dentro de nuestros datos no es relevante')


st.header("Tabla de Procesos Resueltos dentro de los primeros 22 días")
st.markdown("Podemos ver acontinuación la frecuencia absoluta de los estados la cuál nos indica el número de veces que se produce un evento en una muestra y por otro lado tenemos la frecuencia relativa que es el cociente entre la frecuencia absoluta y el tamaño de la muestra.")
img = io.imread("C:/Users/crist/Desktop/2.png")
st.image(img, caption='Frecuencia De Estados')

st.header("Segmentación de Regiones")
st.markdown('Procederemos a realizar una regionalización del pais respecto a la Ruta de servicio y observar de manera porcionada el cambio que se obtiene al analizar el tiempo de recepción, tiempo de y tiempo de respuesta para evaluar el comportamiento del modelo en cuestión.')
st.markdown("Crearemos Nuestras regiones con base en las regiones economicas del país.")
img = io.imread("C:/Users/crist/Desktop/6.png")
st.image(img, caption='Segmentación de Datos')

#Matrices

st.header("Matriz de Covarianza Por Región")
st.markdown("La covarianza es una medida de la relación lineal entre dos variables aleatorias. Se puede interpretar como el grado en que las dos variables varían juntas.")
st.markdown("Una covarianza positiva indica que las dos variables aumentan o disminuyen juntas; cuanto mayor sea la covarianza, mayor será el cambio conjunto de las variables. Una covarianza negativa indica que cuando una variable aumenta, la otra variable tiende a disminuir y viceversa; cuanto más negativo sea el valor de la covarianza, mayor será el cambio opuesto de las variables. ")
st.markdown("Utilizamos la covarianza para predecir el comportamiento futuro de una variable en función del comportamiento de otra variable")


#Matrices
ocho, nueve, diez, once, doce, trece, catorce, quince  = st.tabs(["Covarianza Region Norte", "Covarianza Region Noroeste", "Covarianza Region Norte","Covarianza Region Centro Occidente","Covarianza Region Centro Este","Covarianza Region Oriente","Covarianza Region Sur","Covarianza Yucatán"])

with ocho:
   st.header("Covarianza Region Norte")
   st.image(io.imread("C:/Users/crist/Desktop/8.png"), width=500)

with nueve:
   st.header("Covarianza Region Noroeste")
   st.image(io.imread("C:/Users/crist/Desktop/9.png"), width=500)

with diez:
   st.header("Covarianza Region Noreste")
   st.image(io.imread("C:/Users/crist/Desktop/10.png"), width=500)
   
with once:
   st.header("Covarianza Region Centro Occidente")
   st.image(io.imread("C:/Users/crist/Desktop/11.png"), width=500)

with doce:
   st.header("Covarianza Region Centro Este")
   st.image(io.imread("C:/Users/crist/Desktop/12.png"), width=500)

with trece:
   st.header("Covarianza Region Oriente")
   st.image(io.imread("C:/Users/crist/Desktop/13.png"), width=500)

with catorce:
   st.header("Covarianza Region Sur")
   st.image(io.imread("C:/Users/crist/Desktop/14.png"), width=500)

with quince:
   st.header("Covarianza Yucatán")
   st.image(io.imread("C:/Users/crist/Desktop/15.png"), width=500)     


#Otra cosa
st.header("Gráfica de Tiempo de Respuesta vs. Tiempo de Recepcion vs. Tiempo de Cierre por Region")
st.markdown("Graficamos estas 3 variables por región, para saber si había alguna diferencia significativa en el tiempo de respuesta y el tiempo de cierre entre las regiones")

diez_seis, diez_siete, diez_ocho, diez_nueve, veinte, veinte_uno, veinte_dos, veinte_tres  = st.tabs(["Region Norte", "Region Noroeste", "Region Norte","Region Centro Occidente","Region Centro Este","Region Oriente","Region Sur","Yucatán"])

with diez_seis:
   st.header("Region Norte")
   st.image(io.imread("C:/Users/crist/Desktop/16.png"), width=500)

with diez_siete:
   st.header("Region Noroeste")
   st.image(io.imread("C:/Users/crist/Desktop/17.png"), width=500)

with diez_ocho:
   st.header("Region Noreste")
   st.image(io.imread("C:/Users/crist/Desktop/18.png"), width=500)
   
with diez_nueve:
   st.header("Region Centro Occidente")
   st.image(io.imread("C:/Users/crist/Desktop/19.png"), width=500)

with veinte:
   st.header("Region Centro Este")
   st.image(io.imread("C:/Users/crist/Desktop/20.png"), width=500)

with veinte_uno:
   st.header("Region Oriente")
   st.image(io.imread("C:/Users/crist/Desktop/21.png"), width=500)

with veinte_dos:
   st.header("Region Sur")
   st.image(io.imread("C:/Users/crist/Desktop/22.png"), width=500)

with veinte_tres:
   st.header("Yucatán")
   st.image(io.imread("C:/Users/crist/Desktop/23.png"), width=500)  

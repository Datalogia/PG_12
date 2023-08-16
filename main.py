# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os

from fastapi import FastAPI, HTTPException
from pandasql import sqldf
from datetime import datetime

from numpy import sin, cos, arccos, pi, round

os.environ["OPENBLAS_L2SIZE"]="512k"

app = FastAPI(title = 'Consultas')

df_sub=pd.read_csv('https://github.com/Datalogia/ProyectoG_12/raw/main/raw/Gmaps_H/google_concat.parquet')
#--------------------------------------------------------------------------------------
@app.get("/")   
def index():
    multi_line_string = """
* Para el correcto funcionamiento de la API se debe considerar lo siguiente:
* Modificar el valor del parámetro introduciendo valores válidos que se encuentren 
* en el Dataset.Respetar siempre la ubicación que cada parámetro como se provee en el código.
"""
    return  multi_line_string

#------------------------------------------------------------------------------------------

# Devuelve la distancia desde el punto origen elegido, hasta los puntos
# o coordenadas de los locales en el dataset estudiado

@app.get("/getDistance/{latitude1}/{longitude1}/{unit}")
def getDistance(latitude1:float, longitude1:float,unit:str):
 
  df_sub['distancia']=''
  for i in df_sub.index:
      latitude2=df_sub.latitude[i]
      longitude2=df_sub.longitude[i]
      
      degrees = radians * 180 / pi
      radians = degrees * pi / 180
      theta = longitude1 - longitude2
     
      distance = 60 * 1.1515 * rad2deg( arccos((sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))  ) )

  if unit == 'miles':
      distance=round(distance, 2)
  if unit == 'kilometers':
      distance=round(distance * 1.609344, 2)
      
      df_sub.distancia[i]=distance

  df_sub.sort_values('distancia', inplace=True)     
  return {'recomendadas por prioridad descendente':distance}
#reemplazar distance con df_sub
#----------------------------------------------------

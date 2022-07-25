# -*- coding: utf-8 -*-

import folium

def crea_mapa(latitud, longitud, zoom=9):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    ENTRADA:
        -latitud: latitud del centro del mapa en pantalla -> float
        -longitud: longitud del centro del mapa  en pantalla-> float
        -zoom: nivel del zoom con el que se muestra el mapa -> int
    SALIDA:
        - mapa: objeto mapa creado -> folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa

def crea_marcador (latitud, longitud, etiqueta):
    '''
    Función que crea un marcador rojo con un icono de tipo señal de información.
    El marcador se mostrará en el punto del mapa dado por la latitud y longitud
    y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    ENTRADA:
        -latitud: latitud del marcador -> float
        -longitud: longitud del marcador-> float
        -etiqueta: texto de la etiqueta que se asociará al marcador -> str
    SALIDA:
        - marcador: objeto marcador creado -> folium.Marker
    Toma como entrada la latitud y longitud de dos puntos y devuelve la distancia euclídea
    '''
    marcador = folium.Marker([latitud,longitud], 
                   popup=etiqueta, 
                   icon=folium.Icon(color='red', icon='info-sign')) 
    return marcador

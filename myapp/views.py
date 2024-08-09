import pandas as pd
from django.shortcuts import render
from django.conf import settings
import os

def mostrar_datos(request):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv('./myapp/static/data.csv')

    # Convertir el DataFrame a un formato HTML
    data_html = df.to_html(classes='table table-striped', index=False)

    # Pasar el HTML a la plantilla
    return render(request, 'mostrar_datos.html', {'data_html': data_html})

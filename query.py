import os
import django
from django.db import connection

# Establecer la ruta base del proyecto Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(__file__)
print(BASE_DIR)


# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
django.setup()

# Cambiar al directorio del proyecto Django
os.chdir(BASE_DIR)

from  app.models import *

def consulta_comuna():
    with connection.cursor() as cursor:
        # Ejecutar la consulta SQL
        query = """
        select comuna_id, app_comuna.nombre, app_inmueble.nombre, descripcion 
from app_inmueble
inner join app_comuna on app_comuna.id=comuna_id
group by comuna_id, app_comuna.nombre, app_inmueble.nombre, descripcion
order by comuna_id;

        """
        cursor.execute(query)
        # Obtener todos los resultados
        rows = cursor.fetchall()
    return rows

def save_data_to_txt(rows, file_path):
    with open(file_path, 'w', encoding="utf-8") as file:
        for row in rows:
            file.write(str(row) + '\n')

def export_comuna():
    # Paso 1: Obtener los datos de la base de datos
    rows = consulta_comuna()
    

    # Paso 2: Guardar los datos en un archivo de texto
    file_path = 'consulta_comuna.txt'
    save_data_to_txt(rows, file_path)

    print(f"Data saved to {file_path}")

def consulta_region():
    with connection.cursor() as cursor:
        # Ejecutar la consulta SQL
        query = """
        select region_id, app_region.nombre, app_inmueble.nombre, descripcion 
from app_inmueble
inner join app_region on app_region.id=region_id
group by region_id, app_region.nombre, app_inmueble.nombre, descripcion
order by region_id;

        """
        cursor.execute(query)
        # Obtener todos los resultados
        rows = cursor.fetchall()
    return rows

def save_data_to_txt(rows, file_path):
    with open(file_path, 'w', encoding="utf-8") as file:
        for row in rows:
            file.write(str(row) + '\n')

def export_region():
    # Paso 1: Obtener los datos de la base de datos
    rows = consulta_region()
    

    # Paso 2: Guardar los datos en un archivo de texto
    file_path = 'consulta_region.txt'
    save_data_to_txt(rows, file_path)

    print(f"Data saved to {file_path}")

if __name__ == '__main__':
    export_comuna()
    export_region()
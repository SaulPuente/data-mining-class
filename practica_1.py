import requests
import cloudscraper
import os

cwd = os.getcwd()
folder = "\\data\\"

print("\n\n\tPráctica 1")


urls = [
    "http://datos.cfe.gob.mx/Datos/Electrificacionrural.csv",
    "http://datos.cfe.gob.mx/Datos/Usuariosyconsumodeelectricidadpormunicipio.csv",
    "https://sie.energia.gob.mx/xls/dfrkdsknng_IBMC01_18092023_21_11.xls"
]

archivos = [
    "Electrificacionrural.csv",
    "Usuariosyconsumodeelectricidadpormunicipio.csv",
    "Origen_y_destino_de_la_energia_2000.xls"
]

headers = {'Accept-Encoding': 'gzip',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            "X-Requested-With": "XMLHttpRequest"}

scraper = cloudscraper.create_scraper()

for url, nombre_archivo in zip(urls, archivos):
    print(f"\n\tDescargando {nombre_archivo} de {url} ...")
    
    response = scraper.get(url)

    nombre_archivo = cwd + folder + nombre_archivo
    
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f'\n\tArchivo {nombre_archivo} descargado con éxito.')
    else:
        print(f'\n\tError al descargar el archivo. Código de respuesta: {response.status_code}')
    print(nombre_archivo)
    
# El dataset del IDH se obtiene de esta página, pero no encontré la url del csv
# http://www.snim.rami.gob.mx/
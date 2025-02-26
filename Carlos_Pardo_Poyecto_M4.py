#Importar librerías para hacer la petición, crear archivo json y crear la carpeta
#En la terminal se debe colocar: pip install requests
import requests
import json
import os
import matplotlib.pyplot as plt  # Para mostrar la imagen del Pokémon
from PIL import Image  #Se usa para abrir y manejar imágenes
from urllib.request import urlopen  #Se usa para abrir la URL de la imagen

#Se pide al usuario que ingrese el nombre de un Pokémon
pokemon = input("Escribe el nombre de un Pokémon: ")
#Se complementa la URL de la API de PokeAPI para obtener los datos del Pokémon ingresado
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
#Se realiza solicitud GET a la API
respuesta = requests.get(url)
#Se verifica si la solicitud fue exitosa (código de estado 200)
if respuesta.status_code != 200:
    print("Pokémon no encontrado")
    exit()
else:
    datos_pokemon = respuesta.json()
    #Se Obtiene la información deseada del pokemon
    nombre = datos_pokemon["name"].capitalize()
    peso = datos_pokemon["weight"]
    altura = datos_pokemon["height"]
    #Se usa for para recorrer la lista de tipos y traerlos a una lista en blanco
    tipos = []
    for tipo in datos_pokemon["types"]:
        tipos.append(tipo["type"]["name"].capitalize())
    #Se usa for para recorrer la lista de habilidades y traerlos a una lista en blanco
    habilidades = []
    for habilidad in datos_pokemon["abilities"]:
        habilidades.append(habilidad["ability"]["name"].capitalize())
    #Se usa for para recorrer la lista de movimientos limitandolos a 5 y traerlos a una lista en blanco
    movimientos = []
    for movimiento in datos_pokemon["moves"][:5]:
        movimientos.append(movimiento["move"]["name"].capitalize())
    #Se obtiene la imagen
    url_imagen = datos_pokemon["sprites"]["front_default"]
    #Se muestran los datos
    print("\n--- Información del Pokémon ---")
    print(f"Nombre: {nombre}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} dm")
    print(f"Tipos: {', '.join(tipos)}")
    print(f"Habilidades: {', '.join(habilidades)}")
    print(f"Movimientos: {', '.join(movimientos)}")
    print(f"Imagen: {url_imagen}")
    #Se abre la imagen desde la URL
    imagen = Image.open(urlopen(url_imagen))
    # Mostramos la imagen del Pokémon con Matplotlib
    plt.title("Información del Pokémon")  # Colocamos el nombre de la grafica
    imgplot = plt.imshow(imagen)  # Mostramos la imagen con imshow()
    plt.axis('off')  # Quitamos los ejes
    #Se agrupan los datos a mostrar en la gráfica
    info_text_grafica = (
    f"Nombre: {nombre}\n"
    f"Peso: {peso} kg\n"
    f"Altura: {altura} dm\n"
    f"Tipos: {', '.join(tipos)}\n"
    f"Habilidades: {', '.join(habilidades)}\n"
    f"Movimientos: {', '.join(movimientos)}\n"
    f"Imagen: {url_imagen}"
    )
    # Posicionamos el texto en la parte inferior de la imagen
    plt.text(45, 90, info_text_grafica, fontsize=10, color='black',bbox=dict(facecolor='white', alpha=0), ha='center', va='center')
    #Se muestra todo en pantalla
    plt.show()
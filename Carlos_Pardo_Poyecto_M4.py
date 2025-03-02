#Importar librerías para hacer la petición, crear archivo json y crear la carpeta
#En la terminal se debe colocar: pip install requests
import requests #Se usa requests para hacer la solicitud a la API
import os #Se usa os para manejar archivos y directorios
import json #Se usa json para guardar los datos en un archivo JSON
import matplotlib.pyplot as plt  #Se usa matplotlib.pyplot para mostrar la imagen del Pokémon
from PIL import Image  #Se usa para abrir y manejar imágenes
from urllib.request import urlopen  #Se usa para abrir la URL de la imagen

#Se pide al usuario que ingrese el nombre de un Pokémon y se borran los espacios en blanco
pokemon = input("Escribe el nombre de un Pokémon: ").strip()
#Se complementa la URL de la API de PokeAPI para obtener los datos del Pokémon ingresado
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
#Se realiza solicitud GET a la API
respuesta = requests.get(url)
#Se maneja el tiempo de espera (timeout)
try:
    #Se intenta hacer una solicitud GET con un tiempo de espera de 5 segundos
    respuesta = requests.get(url, timeout=5)
except requests.timeout:
    #Si la solicitud tarda más de 5 segundos, se muestra un mensaje de error
    print("Error: El tiempo de espera ha finalizado")
#Se verifica si la solicitud fue exitosa (código de estado 200)
if respuesta.status_code != 200:
    print("Pokémon no encontrado")
    exit()
else:
    #Se convierte la respuesta en un diccionario de Python
    datos_pokemon = respuesta.json()
    #Se Obtiene la información deseada del pokemon (Nombre, Peso y Altura)
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
    #Se usa for para recorrer la lista de movimientos, ademas se usa un if para limitar los recorridos a 5 y luego trar eso a una lista en blanco
    movimientos = []
    contador_M = 0
    for movimiento in datos_pokemon["moves"]: 
        if contador_M < 5:
            movimientos.append(movimiento["move"]["name"].capitalize())
            contador_M += 1
        else:
            break
    #Se obtiene la imagen
    url_imagen = datos_pokemon["sprites"]["front_default"]
    #Se muestran los datos
    print("\n--- Información del Pokémon ---")
    print(f"Nombre: {nombre}")
    print(f"Peso: {peso/10} kg") #Se divide en 10 para que de el dato exacto en la medida que es cuando se muestra al usuario
    print(f"Altura: {altura/10} mts") #Se divide en 10 para que de el dato exacto en la medida que es cuando se muestra al usuario
    print(f"Tipos: {', '.join(tipos)}") #Se usa join para unir los datos separandolos por coma
    print(f"Habilidades: {', '.join(habilidades)}") #Se usa join para unir los datos separandolos por coma
    print(f"Movimientos: {', '.join(movimientos)}") #Se usa join para unir los datos separandolos por coma
    print(f"Imagen: {url_imagen}")
    #Se abre la imagen desde la URL
    imagen = Image.open(urlopen(url_imagen))
    #Se coloca el nombre de la grafica
    plt.title("Información del Pokémon")
    #Se muestra la imagen con imshow()
    imgplot = plt.imshow(imagen)
    #Se quitan los ejes
    plt.axis('off')
    #Se agrupan los datos a mostrar en la gráfica
    info_text_grafica = (
    f"Nombre: {nombre}\n"
    f"Peso: {peso/10} kg, Altura: {altura/10} mts, Tipos: {', '.join(tipos)}\n" #Se divide en 10 para que de el dato exacto en la medida que es cuando se muestra al usuario y se usa join para unir los datos separandolos por coma
    f"Habilidades: {', '.join(habilidades)}\n" #Se usa join para unir los datos separandolos por coma
    f"Movimientos: {', '.join(movimientos)}\n" #Se usa join para unir los datos separandolos por coma
    f"Imagen: {url_imagen}"
    )
    #Se posicionamos el texto en la parte inferior de la imagen
    plt.text(45, 95, info_text_grafica, fontsize=10, color='black',bbox=dict(facecolor='white', alpha=0), ha='center', va='center')
    #Se muestra todo en pantalla
    plt.show()
    # Crear la carpeta si no existe
    if not os.path.exists("Pokedex"):
        os.mkdir("Pokedex")
    #Se estructuran los datos para guardarlos
    datos_archivo_json = {
    "nombre": nombre,
    "peso": peso,
    "altura": altura,
    "tipos": tipos,
    "habilidades": habilidades,
    "movimientos": movimientos, 
    "Imagen: ": url_imagen
    }
    #Se obtiene la carpeta donde está el script
    carpeta_actual = os.path.dirname(__file__)
    #Se guardan los archivos en un archivo JSON y se usa la ubicación actual del archivo que se está ejecutando
    archivo_guardar = os.path.join(carpeta_actual, f"Pokedex\{nombre}.json")
    #Se abre archivo en modo escritura ("w") y se usa "with open" para asegurar que el archivo se cierre correctamente después de usarlo
    with open(archivo_guardar, "w") as archivo:
        #Se guarda el diccionario, se convirte el archivo en formato JSON y se usa el parametro "indent=4" para darle espacio al archivo para que sea más facil de leer
        json.dump(datos_archivo_json, archivo, indent=4)
    #Se imprime en pantalla que el archivo se gurdó
    print(f"\n¡Datos guardados en {archivo_guardar}!")
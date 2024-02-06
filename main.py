#importar las librerias
from fastapi import FastAPI 
import pandas as pd 

''' 
Instanciamos la clase
FastAPI es una clase de Python que provee toda la funcionalidad para tu API
'''
app = FastAPI()

'''
Cargamos los datos con los que se trabajaran
'''
def function_df(ruta):
    try:
        df = pd.read_json(ruta, lines=True)
    except ValueError as e:
        return print(f"Error al leer el archivo JSON: {e}")
    return df

df_steam_games = function_df('./Datasets/clean_steam_games.json')
df_user_reviews = function_df('./Datasets/clean_user_reviews.json')
df_user_items = function_df('./Datasets/clean_user_items.json')

# Convierte la columna 'release_date' a tipo datetime
df_steam_games['release_date'] = pd.to_datetime(df_steam_games['release_date'], errors='coerce')

# Elimina los registros con NaT en la columna 'release_date'
df_steam_games = df_steam_games.dropna(subset=['release_date'])

''' 
Escribimos el decorador de path para cada funcion
Este decorador le dice a FastAPI que la funcion que esta por debajo
corresponde al path / con una operacion GET
Usamos async para que la llamada al servidor sea asincrona
De esta forma pueda ejecutar otras tareas en vez de tener que estar esperando a que se devuelva una respuesta
'''
@app.get("/A")
async def developer( desarrollador : str ):
    '''
    Calcula cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora

    Parametros
    ----------
    desarrollador : str

    Retorno
    -------
    Año, Cantidad de items, porcentaje contenido free

    '''
    #Transformar la columna "developer" y "price" en str en letra minuscula
    df_steam_games['developer'] = df_steam_games['developer'].astype(str).str.lower()
    df_steam_games['price'] = df_steam_games['price'].astype(str).str.lower()
    desarrollador.lower()

    #Filtrar por desarrollador
    developer_df = df_steam_games[df_steam_games['developer'].str.contains(desarrollador, case=False)]

    if developer_df.empty:
        print(f"No hay registros para el desarrollador {desarrollador}.")
        return None

    estadisticas_desarrolladores = []

    for developer, juegos in developer_df.groupby('developer'):
        total_juegos = len(juegos)
        juegos_free = juegos[juegos['price'].str.contains('free', case=False)]
        total_juegos_free = len(juegos_free)

        porcentaje_free = (total_juegos_free / total_juegos) * 100 if total_juegos > 0 else 0

        estadisticas = {
            'desarrollador': developer,
            'total_juegos': total_juegos,
            'porcentaje_free': porcentaje_free
        }

        estadisticas_desarrolladores.append(estadisticas)

    return estadisticas_desarrolladores


@app.get("/B")
async def userdata( User_id : str ):
    '''
    Calcula cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items

    Parametros
    ----------
    User_id : str

    Retorno
    -------
    {"Usuario X" : nombre de usuario, "Dinero gastado": x USD, "% de recomendación": x%, "cantidad de items": x}

    '''
    # Unir los dataframes usando 'item_id' como clave
    df_merged = pd.merge(df_steam_games, df_user_reviews, on='item_id')

    # Filtrar juegos comprados por el usuario
    juegos_comprados = df_merged[df_merged['user_id'] == User_id].copy()

    # Convertir la columna 'price' a tipo cadena
    juegos_comprados['price'] = juegos_comprados['price'].astype(str)
    # Reemplazar "free" o "Free" en la columna 'price' por 0
    juegos_comprados.loc[juegos_comprados['price'].str.contains(r'(?i)\bfree\b'), 'price'] = 0
    # Convertir la columna 'price' a tipo float para poder sumar los valores
    juegos_comprados['price'] = juegos_comprados['price'].astype(float)
    
    # Convertir la columna 'price' a tipo numérico
    juegos_comprados['price'] = pd.to_numeric(juegos_comprados['price'], errors='coerce')

    # Calcular dinero gastado por el usuario
    dinero_gastado = round(juegos_comprados['price'].sum(), 2)

    # Calcular el porcentaje de recomendación
    total_reviews = juegos_comprados.shape[0]
    reviews_recomendadas = juegos_comprados[juegos_comprados['recommend'] == True].shape[0]
    porcentaje_recomendacion = (reviews_recomendadas / total_reviews) * 100 if total_reviews > 0 else 0

    # Calcular cantidad de items
    cantidad_items = juegos_comprados.shape[0]

    return {
        "Usuario": User_id,
        "Dinero gastado": f"{dinero_gastado} USD",
        "% de recomendación": f"{porcentaje_recomendacion}%",
        "Cantidad de items": cantidad_items
    }


@app.get("/C")
async def UserForGenre( genero : str ):
    '''
    Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

    Parametros
    ----------
    genero : str 

    Retorno
    -------
    {"Usuario con más horas jugadas para Género X" : nombre de usuario, "Horas jugadas":[{Año: x1, Horas: n}, {Año: x2, Horas: n2}, {Año: x3, Horas: n3}]}

    '''
    
    return


@app.get("/D")
async def best_developer_year( año : int ):
    '''
    Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

    Parametros
    ----------
    año : int 

    Retorno
    -------
    [{"Puesto x1" : X}, {"Puesto x2" : Y},{"Puesto x3" : Z}]

    '''
    
    return


@app.get("/E")
async def developer_reviews_analysis( desarrolladora : str ): 
    '''
    Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

    Parametros
    ----------
    desarrolladora : str 

    Retorno
    -------
    {'desarrollador x' : [Negative = x1, Positive = x2]}

    '''
    
    return

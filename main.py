#importar las librerias
from fastapi import FastAPI 

''' 
Instanciamos la clase
FastAPI es una clase de Python que provee toda la funcionalidad para tu API
'''
app = FastAPI()

''' 
Escribimos el decorador de path para cada funcion
Este decorador le dice a FastAPI que la funcion que esta por debajo
corresponde al path / con una operacion GET
Usamos async para que la llamada al servidor sea asincrona
De esta forma pueda ejecutar otras tareas en vez de tener que estar esperando a que se devuelva una respuesta
'''
@app.get("/")
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

    return


@app.get("/")
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
    
    return


@app.get("/")
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


@app.get("/")
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


@app.get("/")
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

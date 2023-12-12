import pandas as pd
import gzip
import ast

def descomprimirjson(ruta, variable_anidada):
    '''Función que recibe una ruta de acceso a un archivo json anidado y carga la información en un
    DataFrame de Pandas'''
    fila = []
    with gzip.open(ruta, 'rt', encoding='MacRoman') as archivo:
        for line in archivo.readlines():
            fila.append(ast.literal_eval(line))

    df = pd.DataFrame(fila)                                                 
    df = df.explode(variable_anidada).reset_index()                         
    df = df.drop(columns="index")                                           
    df = pd.concat([df, pd.json_normalize(df[variable_anidada])], axis=1)   
    df = df.drop(columns=variable_anidada)                                  

    return df
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.dropna(axis=0, inplace=True)

    df['sexo']=df['sexo'].str.lower()

    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()

    df['idea_negocio']=df['idea_negocio'].str.lower()
    df['idea_negocio']=df['idea_negocio'].replace('-', ' ')
    df['idea_negocio']=df['idea_negocio'].replace('_', ' ')

    df['barrio']=df['barrio'].str.lower()
    df['barrio']=df['barrio'].replace('-', ' ')
    df['barrio']=df['barrio'].replace('_', ' ')

    df['monto_del_credito']=df['monto_del_credito'].replace('.','')
    df['monto_del_credito']=df['monto_del_credito'].replace(',','')
    df['monto_del_credito']=df['monto_del_credito'].str.strip('$')

    df.drop_duplicates(inplace=True)

    print(df['sexo'].value_counts())
    #
    # Inserte su código aquí
    #

    return df
print(clean_data())

"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    
    df.dropna(axis=0, inplace=True)

    
    df['sexo'] = df['sexo'].str.lower()
    df['sexo'] = df['sexo'].str.replace('_', ' ')
    df['sexo'] = df['sexo'].str.replace('-', ' ')

    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('_', ' ')
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.replace('-', ' ')

    df['idea_negocio']=df['idea_negocio'].str.lower()
    df['idea_negocio']=df['idea_negocio'].replace('-', ' ')
    df['idea_negocio']=df['idea_negocio'].replace('_', ' ')

    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')

    df['barrio']=df['barrio'].str.lower()
    df['barrio']=df['barrio'].replace('-', ' ')
    df['barrio']=df['barrio'].replace('_', ' ')

    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(str).str.strip('.0')

    df['fecha_de_beneficio']=pd.to_datetime(df['fecha_de_beneficio'],format='%d/%m/%Y' , errors='coerce').fillna(
            pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce'))
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d-%m-%Y')

    df['monto_del_credito']=df['monto_del_credito'].str.strip('$')
    df['monto_del_credito']=df['monto_del_credito'].str.replace(",","")
    df['monto_del_credito']=df['monto_del_credito'].astype(float)
    df['monto_del_credito']=df['monto_del_credito'].astype(int)


    df['línea_credito']=df['línea_credito'].str.lower()
    df=df.dropna(inplace=True)

    #print(df['sexo'].value_counts())
    #print(df['línea_credito'].isnull().sum())
    #
    # Inserte su código aquí
    #

    return df
clean_data()

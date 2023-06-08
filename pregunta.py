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
    df['idea_negocio']=df['idea_negocio'].str.replace('-', ' ')
    df['idea_negocio']=df['idea_negocio'].str.replace('_', ' ')

    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ')

    df['barrio']=df['barrio'].str.lower()
    df['barrio']=df['barrio'].str.replace('-', ' ')
    df['barrio']=df['barrio'].str.replace('_', ' ')
    
    df['estrato'] = df['estrato'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True)
    

    
    
    df['monto_del_credito']=df['monto_del_credito'].str.strip('$')
    df['monto_del_credito']=df['monto_del_credito'].str.replace(",","")
    df['monto_del_credito']=df['monto_del_credito'].astype(float)
    df['monto_del_credito']=df['monto_del_credito'].astype(int)
    


   
  
    df.drop_duplicates(inplace=True)


    print(df['tipo_de_emprendimiento'].value_counts().to_list())
    #print(df['línea_credito'].isnull().sum())
    #
    # Inserte su código aquí
    #

    return df
clean_data()

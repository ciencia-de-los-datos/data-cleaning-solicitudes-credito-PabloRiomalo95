"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df= df[df.columns[1:]]
    df=df.dropna()
    df.columns.values
    df['sexo']= df['sexo'].str.lower() 
    df['tipo_de_emprendimiento']= df['tipo_de_emprendimiento'].str.lower()
    # idea_negocio
    df['idea_negocio']= df['idea_negocio'].str.lower()
    df['idea_negocio']=df['idea_negocio'].str.replace("-","_")
    df['idea_negocio']=df['idea_negocio'].str.replace("_"," ")
    df['idea_negocio']=df['idea_negocio'].str.strip()
    # Barrio
    df['barrio']= df['barrio'].str.lower()
    df['barrio']=df['barrio'].str.replace("-","_")
    df['barrio']=df['barrio'].str.replace("_"," ")
    df['barrio']=df['barrio'].str.replace(".","")
    df['barrio']=df['barrio'].str.strip()
    #Casos Especiales
    df['barrio']=df['barrio'].str.replace("bel¿n","belen")
    df['barrio']=df['barrio'].str.replace("antonio nari¿o","antonio nariño")
    #línea_credito
    df['línea_credito']= df['línea_credito'].str.lower()
    df['línea_credito']=df['línea_credito'].str.replace("-","_")
    df['línea_credito']=df['línea_credito'].str.replace("_"," ")
    df['línea_credito']=df['línea_credito'].str.replace(".","")
    df['línea_credito']=df['línea_credito'].str.strip()
    #Casos Especiales
    df['línea_credito']=df['línea_credito'].str.replace("soli diaria","solidaria")
    #fecha_de_beneficio
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,dayfirst=True)
    #monto_del_credito
    df['monto_del_credito']=df['monto_del_credito'].str.replace(",","")
    df['monto_del_credito']=df['monto_del_credito'].str.replace("$","")
    df['monto_del_credito']=df['monto_del_credito'].str.strip()
    df['monto_del_credito'] = df['monto_del_credito'].apply(pd.to_numeric, downcast="integer", errors='ignore')
    df.drop_duplicates(inplace=True)
    # df=pd.DataFrame(df).reset_index(drop=True)

    return df

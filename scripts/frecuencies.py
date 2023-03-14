#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:02:35 2022

@author: Cristhian
"""

import pandas as pd

def craete_frequency(filename:str,new_filename:str) -> None:
    """
    Recibe el nombre del archivo que se va a leer
    Recibe el nombre del nuevo archivo a guardar

    Realiza la agrupación de los datos, ordena y
    los guarda en formato csv

    Parameters
    ----------
    filename : String
        Nombre del archivo a leer.
    new_filename : String
        Nombre del nuevo archivo.

    Returns
    -------
    None.

    """
    df =pd.read_csv('data/{}.csv'.format(filename))
    df = df.groupby('sub_razas_asociadas')['raza'].count().reset_index(name="frecuencia")\
                .sort_values(by="frecuencia", ascending = False).reset_index(drop=True)

    df.columns = ['sub_razas', 'frecuencia']
    
    df.to_csv('data/{}.csv'.format(new_filename), index=False)
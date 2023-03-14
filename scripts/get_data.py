#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:43:32 2022

@author: Cristhian
"""
import requests
import json


def get_data(url:str,file_name:str) -> None:
    """
    Recibe la url del endpoint y nombre que se quiere dar al archivo
    y guarda un archivo .json en el directorio actual
    
    Parameters
    ----------
    url : string
        endpoint.
        
    nombre_archivo : string
        nombre que se desea dar al archivo.

    Returns
    -------
    None.

    """
    res = requests.get(url)
    data = res.json()
    with open('data/{}.json'.format(file_name), 'w') as f:
        json.dump(data, f)
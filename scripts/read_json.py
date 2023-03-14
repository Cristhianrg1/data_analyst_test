#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:15:10 2022

@author: Cristhian
"""

import json
import csv


def open_data(file):
    """
    Recibe el nombre del archivo, abre, filtra
    la sección inicial del json y returna un dict

    Parameters
    ----------
    file : string
        Nombre del archivo.

    Returns
    -------
    message_data : Dict
        Diccionario filtrado.

    """
    with open('data/{}.json'.format(file)) as file:
        data = json.load(file)
    
    message_data = data['message']
    return message_data


def save_csv_file(data, file_name):
    """
    Recibe los datos en formato json/dict,
    crea el archivo con el nombre que se deja en el parámetro
    y guarda un csv con los datos

    Parameters
    ----------
    data : Dict

    file_name : string
        Nombre con el que se quiere guardar el archivo.

    Returns
    -------
    None.

    """
    file = open('data/{}.csv'.format(file_name),'w')
    csv_writer = csv.writer(file)
    
    header = ['raza','sub_razas_asociadas']
    csv_writer.writerow(header)
    
    for i in data:
        row_list = []
        row_list.append(i)
        row_list.append(len(data[i]))
        csv_writer.writerow(row_list)
    
    file.close()
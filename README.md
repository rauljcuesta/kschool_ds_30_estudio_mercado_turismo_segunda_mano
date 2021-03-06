# IMPORTANTE (2022-06-24 18:45)
Se han añadido al repositorio una copia de los notebook 3 y 4 con las celdas ejecutadas y nuevos enlaces en el README con los datos ya preprocesados, subidos al Drive y con permisos. Son las únicas modificaciones hechas.


# Estudio venta turismos

El siguiente repositorio contiene el trabajo de fin de máster de Raúl José de la Cuesta García, alumno de la edición número 30 del máster de Data Science de la escuela KSCHOOL.

## Descripción
El trabajo expone las carácteristicas más importantes de la información que proporciona la DGT sobre las transacciones de vehículos, así como intenta predecir la cantidad de traspasos futuros

## Ejecución
Previo a la ejecución, es necesario realizar el cambio del parametro "base_route", indicando la ruta desde la cual se va a ejecutar, dentro del archivo "config/config.yml" (https://github.com/rauljcuesta/kschool_ds_30_estudio_mercado_turismo_segunda_mano/blob/main/config/config.yml)

Para la ejecución del trabajo, es necesario ejecutar los notebook en el siguiente orden
- Obtención de datos de la DGT: 01_obtain_data_dgt.ipynb
- Preprocesamiento de los datos: 02_preprocess_dgt_files.ipynb
- Estudio previo de los datos: 03_study_dgt_dataset.ipynb
- Modelización: 04_dgt_time_series.ipynb 

## Memoria
La memoria es el archivo "memoria_raul_j_cuesta_mercado_turismo_kschool_ds_30.pdf"

## Descarga de datos
Los archivos necesario se pueden descargar en las siguientes url's:

Nuevos, Drive:
https://drive.google.com/file/d/1DKGyoHhpML8QQdw7lWrDykSlrv-pQuS-/view?usp=sharing
https://drive.google.com/file/d/1bp3G0bq7vDki_khs1LWzE6wmABopjo5d/view?usp=sharing
https://drive.google.com/file/d/1x-BdMzWd_8Q41KMVP1k7mRvVgnDSDR6q/view?usp=sharing
https://drive.google.com/file/d/1MPDZ6jdn8L0ZLzDdUXKUrqyylAxiumSO/view?usp=sharing
https://drive.google.com/file/d/1kCttyU-TfzYQerrbSHxfjy0kr29AIiIa/view?usp=sharing
https://drive.google.com/file/d/1Vpbqm2WmwGRJEfZLOTqprhdcRDCW9gDp/view?usp=sharing
https://drive.google.com/file/d/19usRP8-NNFX9eCmkcnD5R6iObQJ-haLP/view?usp=sharing


No tienen permisos
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2015.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2016.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2017.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2018.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2019.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2020.csv.tar.gz?authuser=0
https://storage.cloud.google.com/rauljcuesta_kschool_proyecto_master/dgt/export_anual_trf_2021.csv.tar.gz?authuser=0

Deben de almacenarse el la ruta "data/dgt/"

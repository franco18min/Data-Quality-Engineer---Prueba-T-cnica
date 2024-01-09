![header](https://capsule-render.vercel.app/api?type=rect&height=120&section=header&text=%20Prueba%20Tecnica%20Data%20Quality%20Enginner&fontSize=30&&color=04045b&fontColor=ffffff&font)
<div align="center">
  <img src="https://th.bing.com/th/id/OIP.D5j4O42f84oip3otPzpPYwAAAA?rs=1&pid=ImgDetMain" width="200" height="150">
</div>




## Indice
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#Indice">Índice</a></li>
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Alcance">Alcance</a></li>
    <li><a href="#Tecnologías">Tecnologías Utilizadas</a></li>
    <li><a href="#Conclusiones relevantes">Conclusiones relevantes</a></li>
    <li><a href="#Desarrollador">Desarrollador</a></li>
  </ol>
</details>

## Introducción
Esta es la prueba tecnica para la empresa R5. 

Esta prueba propone hacer un reporte de calidad de datos con archivo JSON 

## Objetivo
El objetivo es realizar el reporte de calidad de datos con el fin de dar a conocer el nivel de detalle a la hora de reportar anomalias. 

La prueba busca alcanzar los siguientes objetivos especificos:
- Transformar los datos a un formato adecuado para realizar el reporte.
- Sacar conclusiones a partir del reporte hecho.

## Alcance
La prueba fue desarrollada siguiendo los pasos a continuación:

1. Pre-procesamiento de datos del archivo JSON en donde hemos desanidado complementamente los mismo para tener un dataframe plano facil de manipular. [spotify_json_to_csv.py](spotify_json_to_csv.py)
2. Análisis exploratorio de datos con el fin de encontrar anomalias en la calidad de datos. [SpotifyDataQualityAnalysis.ipynb](SpotifyDataQualityAnalysis.ipynb)
3. Desarrollo del reporte de calidad de datos que sera el mismo archivo ipynb que se encuentra en este repositorio.

## Tecnologías
![Pycharm](https://img.shields.io/badge/Pycharm-000000?style=for-the-badge&logo=Pycharm&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)
![Json](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=JSON&logoColor=white&color=green)
![Seaborn](https://img.shields.io/badge/Seaborn-000000?style=for-the-badge&logo=Seaborn&logoColor=white&color=purple)
![Matplotlib](https://img.shields.io/badge/Matplotlib-000000?style=for-the-badge&logo=Matplotlib&logoColor=white&color=light)

## Conclusiones relevantes
1. **Conclusiones**
- Tenemos datos nulos en las columnas "album_name", "track_name", "track_id", "danceability", "energy", "key", "loudness", "speechiness", "acousticness", "liveness", "tempo" y "time_signature" que deberiamos analizar y tomar una decision de que hacer con ellos.
- Tenemos datos repetidos en las columnas "id" y "track_id" que deberiamos analizar y tomar una decision de que hacer con ellos.
- Tenemos datos que no corresponden al tipo de datos que deberian ser en las columnas "key", "instrumentalness" y "time_signature" que deberiamos analizar y tomar una decision de que hacer con ellos.
- Tenemos datos que no corresponden al intervalo de valores que deberian ser en las columnas "track_popularity", "acousticness" e "instrumentalness" que deberiamos analizar y tomar una decision de que hacer con ellos.

## Desarrollador
<div align="center">

 
| [<img src="https://avatars.githubusercontent.com/u/44064764?v=4" width=115><br><sub>Franco Aguilera</sub>](https://github.com/franco18min) |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| 

Aquí esta mi Linkedin si te quieres poner en contacto conmigo: </br>

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/franco-aguilera-0686ba255/)

</div>

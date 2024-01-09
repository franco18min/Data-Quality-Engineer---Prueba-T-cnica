# Importamos las librerias necesarias

import pandas as pd
import json

# Leemos el archivo json

with open('taylor_swift_spotify.json') as f:
    data = json.load(f)

# Procesamos el JSON

rows = [] # Inicializamos una lista vacia
for album in data['albums']: # Recorremos los albums
    for track in album['tracks']: # Recorremos las canciones
        row = { # Dentro del bucle de las pistas, se crea un diccionario row que contiene información sobre el artista, el álbum y la pista actual
            'artist_id': data['artist_id'],
            'artist_name': data['artist_name'],
            'artist_popularity': data['artist_popularity'],
            'album_id': album['album_id'],
            'album_name': album['album_name'],
            'album_release_date': album['album_release_date'],
            'album_total_tracks': album['album_total_tracks'],
            'track_id': track['track_id'],
            'track_name': track['track_name'],
            'track_popularity': track['track_popularity'],
            'disc_number': track['disc_number'],
            'duration_ms': track['duration_ms'],
            'explicit': track['explicit'],
            'track_number': track['track_number'],
        }
        row.update(track['audio_features']) # Se añaden las características de audio_feature
        rows.append(row) # Se añade el diccionario row a la lista rows

# Convertimos la lista de diccionarios en un DataFrame

df = pd.DataFrame(rows)

# Guardamos el DataFrame en un archivo csv

df.to_csv('taylor_swift_spotify.csv', index=False)
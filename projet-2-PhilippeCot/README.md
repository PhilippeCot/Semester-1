# Project 2 :  Data Processing and Object-Oriented Programming

# Introduction

This playlist system project was developed as part of a school assignment at Inducedieul. The objective was to implement an object-oriented design for creating and playing playlists using Python. The project emphasized the use of abstract classes, inheritance, and aggregation to model instruments, songs, and playlists effectively. I am proud to share that I achieved a perfect score of 100% for this project, demonstrating the quality and effort put into its completion.

#### Part 1 :  Data Processing

We will analyze a dataset of songs using scientific libraries in a Jupyter Notebook, an ideal format for data exploration.

Working directory: part1/.

Detailed instructions: See Part 1.

#### Part 2 : Object-Oriented Programming

This section focuses on creating an application to "play" song playlists using musical instruments.

Working directory: part2/.


Detailed instructions: See Part 2.



## Project structure

```plaintext
<principal>/
│   README.md
└─── part1/
│   └─── plots/
│           ...
│        songs-analysis.ipynb
└─── part2/
    └─── data/
    │       songs.csv
    │       songs.json
    └─── modules/
    │       utils.py
    │       instruments.py
    │       song.py
    │       playlist.py
    └─── main.py
```

### Directory `part1/`
This directory is used for completing Part 1 of the project.

songs.csv: A CSV file containing song data.

songs-analysis.ipynb: A Jupyter Notebook for analyzing songs.

plots/: Contains sample visual outputs expected from the Notebook.

Working in Jupyter (via VS Code):


Open songs-analysis.ipynb.

Configure the appropriate kernel.


### Directory  `part2/`
For object-oriented programming tasks.

data/: 

Includes CSV and JSON song data.

modules/: 

Houses class implementation files.

main.py: 

Tests the implementation.

Run tests by executing main.py or through the editor.

Data Insights (Part 1)

The dataset includes metrics like Spotify streams, YouTube views, TikTok engagements, and more. Analysis includes creating visualizations and training a linear regression model.

## Content
| Nom de la colonne | Description |
| -- | -- |
| Track Name | Titre de la chanson. |
| Album Name | Nom de l'album auquel la chanson appartient. |
| Artist | Nom de l'artiste ou des artistes de la chanson. |
| Release Date | Date de sortie de la chanson. |
| ISRC | International Standard Recording Code de la chanson. |
| All Time Rank | Classement de la chanson basé sur sa popularité historique. |
| Track Score | Score attribué au titre selon divers facteurs. |
| Spotify Streams | Nombre total d'écoutes sur Spotify. |
| Spotify Playlist Count | Nombre de playlists Spotify contenant la chanson. |
| Spotify Playlist Reach | Portée de la chanson à travers les playlists Spotify. |
| Spotify Popularity | Score de popularité de la chanson sur Spotify. |
| YouTube Views | Nombre total de vues de la vidéo officielle de la chanson sur YouTube. |
| YouTube Likes | Nombre total de likes sur la vidéo officielle de la chanson sur YouTube. |
| TikTok Posts | Nombre de publications TikTok incluant la chanson. |
| TikTok Likes | Nombre total de likes sur les publications TikTok incluant la chanson. |
| TikTok Views | Nombre total de vues sur les publications TikTok incluant la chanson. |
| YouTube Playlist Reach | Portée de la chanson à travers les playlists YouTube. |
| Apple Music Playlist Count | Nombre de playlists Apple Music contenant la chanson. |
| AirPlay Spins | Nombre de fois que la chanson a été diffusée sur les stations de radio. |
| SiriusXM Spins | Nombre de fois que la chanson a été diffusée sur SiriusXM. |
| Deezer Playlist Count | Nombre de playlists Deezer contenant la chanson. |
| Deezer Playlist Reach | Portée de la chanson à travers les playlists Deezer. |
| Amazon Playlist Count | Nombre de playlists Amazon Music contenant la chanson. |
| Pandora Streams | Nombre total d'écoutes sur Pandora. |
| Pandora Track Stations | Nombre de stations Pandora incluant la chanson. |
| Soundcloud Streams | Nombre total d'écoutes sur Soundcloud. |
| Shazam Counts | Nombre total de fois que la chanson a été recherchée sur Shazam. |
| TIDAL Popularity | Score de popularité de la chanson sur TIDAL. |
| Explicit Track | Indique si la chanson contient un contenu explicite. |

## Travail à réaliser
Les instructions détaillées se trouvent directement dans le cahier Jupyter `song-analysis.ipynb`.
- 1.1. Chargement du jeu de données
- 1.2. Exploration des données
- 1.3. Nettoyage des données
- 1.4. Extraction de données
- 1.5. Conversion de données
- 1.6. Visualisation de données
- 1.7. Matrice de corrélation
- 1.8. Entraînement d'un modèle de régression

# Part 2 : Object-Oriented Programming

The goal is to create a playlist playback system capable of generating playlists from a database of songs (stored in data/songs.csv and data/songs.json) and playing them in "solo" mode using a single instrument.

Overview

Implement an abstract class Instrument with shared instrument characteristics and its child classes: Guitar, Piano, and Drum.

Develop the Song class, which aggregates an Instrument to play songs.

Build the Playlist class, aggregating a dictionary of Song objects, allowing playback of multiple songs from a playlist.


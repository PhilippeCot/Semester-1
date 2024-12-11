from modules.instruments import Guitar, Piano, Drum, Instrument
from modules.song import Song
from modules.playlist import Playlist
from modules.utils import print_section_separator

import json

csv_path = "data/songs.csv"
json_path = "data/songs.json"

# 2.1.3. Fonction à compléter après avoir compléter le code de modules/instruments.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testInstruments():
  return # <- Ligne à retirer
  print_section_separator("Tests partie 2.1")
  
  # TODO: Instancier un objet de la classe Instrument.

  # TODO: Instancier une Guitar du "fabricant-g", l'afficher, et appeler sa méthode play().

  # TODO: Instancier un Piano du "fabricant-p", l'afficher, et appeler sa méthode play().

  # TODO: Instancier un Drum du "fabricant-b", l'afficher, et appeler sa méthode play().


# 2.2.6. Fonction à compléter après avoir compléter le code de modules/song.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testSong():
  return # <- Ligne à retirer
  print_section_separator("Tests partie 2.2")

  # TODO: Instancier une Song appelée "Title", de l'artiste "Artist",
  #       sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
  #       Afficher l'instance créée.

  # TODO: Instancier une Song à partir d'un dictionnaire/objet vide (i.e. {}).
  #       Afficher l'instance créée.

  # TODO: Instancier une Song à partir de la 1ère chanson du fichier "data/songs.json"
  #       Afficher l'instance créée.


# 2.3.6. Fonction à compléter après avoir compléter le code de modules/playlist.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testPlaylist():
  return # <- Ligne à retirer
  print_section_separator("Tests partie 2.3")

  # TODO: Instancier une Playlist nommée "Playlist-csv" depuis le fichier CSV data/songs.csv.

  # TODO: Instancier une Playlist nommée "Playlist-json" depuis le fichier JSON data/songs.json.

  # TODO:Ajouter un dictionnaire/objet vide (i.e. {}) à la playlist "Playlist-json".
  
  # TODO: Ajouter les chansons de la playlist "Playlist-json" à la playlist "Playlist-csv".
  
  # TODO: Retirer la chanson intitulée "We Will Rock You" de la playlist "Playlist-csv".

  # TODO: Jouer toutes les chansons de la playlist "Playlist-json" en mode normal.

  #TODO: Jouer toutes les chansons de la playlist "Playlist-csv" en mode aléatoire.


if __name__ == "__main__":
  testInstruments()
  testSong()
  testPlaylist()

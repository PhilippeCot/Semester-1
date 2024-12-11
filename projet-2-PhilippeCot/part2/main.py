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
  print_section_separator("Tests partie 2.1")
  
  # TODO: Instancier un objet de la classe Instrument.
  try:
      instr = Instrument("fabricant-X")
      print(instr)
  except TypeError:
      print("Impossible d'instancier un Instrument.")

  # TODO: Instancier une Guitar du "fabricant-g", l'afficher, et appeler sa méthode play().
  guitare = Guitar("fabricant-g")
  print(guitare)
  guitare.play()
  # TODO: Instancier un Piano du "fabricant-p", l'afficher, et appeler sa méthode play().
  piano = Piano("fabricant-p")
  print(piano)
  piano.play()
  # TODO: Instancier un Drum du "fabricant-b", l'afficher, et appeler sa méthode play().
  batterie = Drum("fabricant-b")
  print(batterie)
  batterie.play()

# 2.2.6. Fonction à compléter après avoir compléter le code de modules/song.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testSong():
  print_section_separator("Tests partie 2.2")

  # TODO: Instancier une Song appelée "Title", de l'artiste "Artist",
  #       sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
  #       Afficher l'instance créée.
  song_drum = Song("Title", "Artist", 2024, Drum("brand"))
  print(song_drum)
  # TODO: Instancier une Song à partir d'un dictionnaire/objet vide (i.e. {}).
  #       Afficher l'instance créée.
  try:
     error_song = Song.from_obj({})
  except ValueError as e:
     print("ValueError, message: Impossible d'instancier une chanson depuis l\'objet '{}'.")
  # TODO: Instancier une Song à partir de la 1ère chanson du fichier "data/songs.json"
  #       Afficher l'instance créée.
  first_data = json.load(open("part2/data/songs.json"))[0]
  first_song = Song.from_obj(first_data)
  print(first_song)
# 2.3.6. Fonction à compléter après avoir compléter le code de modules/playlist.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testPlaylist():
    print_section_separator("Tests partie 2.3")

    # Instancier une Playlist nommée "Playlist-csv" depuis le fichier CSV.
    playlist_csv = Playlist.from_csv("Playlist-csv", "part2/data/songs.csv")

    # Instancier une Playlist nommée "Playlist-json" depuis le fichier JSON.
    playlist_json = Playlist.from_json("Playlist-json", "part2/data/songs.json")

    # Ajouter un dictionnaire/objet vide à la playlist "Playlist-json" pour déclencher une exception.
    try:
        playlist_json + {}
    except TypeError as e:
        print(f"TypeError, message: {e}")

    # Ajouter les chansons de "Playlist-json" à "Playlist-csv".
    for song in playlist_json:
        playlist_csv += song

    # Retirer la chanson intitulée "We Will Rock You" de "Playlist-csv".
    playlist_csv -= "We Will Rock You"

    # Jouer toutes les chansons de "Playlist-json" en mode normal.
    playlist_json.play_all(False)

    # Jouer toutes les chansons de "Playlist-csv" en mode aléatoire.
    playlist_csv.play_all(True)


if __name__ == "__main__":
  testInstruments()
  testSong()
  testPlaylist()

from modules.song import Song
from typing import Iterator
import csv, json, random


class Playlist():
  def __init__(self, name: str, songs: list[Song]):
    self.__name = name
    self.__songs = {song.title: song for song in songs}

  @classmethod
  def from_csv(cls, name: str, csv_path: str):
    songs = []
    name = name
    with open(csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
         song = Song.from_obj(line)  
         songs.append(song)
    return cls(name, songs)
  
  @classmethod
  def from_json(cls, name: str, json_path: str):
    songs = []
    with open(json_path, 'r') as json_file:
     file_data = json.load(json_file)
    for obj in file_data:
      song = Song.from_obj(obj)
      songs.append(song)
    return cls(name, songs)
  
  @property
  def name(self) -> str:
    return self.__name
  
  @property
  def songs(self) -> dict[str, Song]:
    return self.__songs
  
  @name.setter
  def name(self, name: str):
    self.__name = name

  @songs.setter
  def songs(self, songs: list[Song]):
    self.__songs = {song.title: song for song in songs}

  def __iter__(self) -> Iterator[Song]:
    list_song = list(self.__songs.values())
    return iter(list_song)
  
  def __add__(self, song: Song):
    if not isinstance(song, Song):
      raise TypeError(f"Impossible d'ajouter une chanson de type {type(song)}.")
    self.__songs[song.title] = song
    return self
  
  def __sub__(self, song_title: str):
    self.__songs.pop(song_title)
    return self
  
  def play_all(self, rdm_mode: bool = False):
    mode = "standard" if not rdm_mode else "aléatoire"
    print(f"Lecture de {self.__name} ({len(self.__songs)} chansons en mode {mode})")
    songs_to_play = list(self.__songs.values())
    if rdm_mode:
        random.shuffle(songs_to_play)
    for song in songs_to_play:
        song.play()
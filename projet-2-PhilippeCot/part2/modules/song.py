import modules.instruments # used in from_obj() classmethod
from modules.instruments import Instrument
from datetime import datetime


class Song():
  max_len_str_attr = 25
  def __init__(self, title: str, artist: str, release_year: int, instrument: Instrument):
    self.__title = title
    self.__artist = artist
    self.__release_year = release_year
    self.__instrument = instrument

  @classmethod
  def from_obj(cls, obj: dict):
    desired_fields = {"title", "artist", "release_year", "instrument", "instrument_brand"}
    if not desired_fields.issubset(obj.keys()):
      raise ValueError(f"Impossible d'instancier une chanson depuis l'objet '{obj}'.")
    
    title = obj["title"]
    artist = obj["artist"]
    release_year = obj["release_year"]
    instrument_name = obj["instrument"]
    instrument_brand = obj["instrument_brand"]
    instrument_cls = getattr(modules.instruments, obj["instrument"])
    instrument = instrument_cls(instrument_brand)
    return cls(title, artist, release_year, instrument)
  @property 
  def title(self) -> str:
    return self.__title
  @property
  def artist(self) -> str:
    return str(self.__artist)
  
  @property
  def release_year(self) -> int:
    return int(self.__release_year)
  
  @property
  def instrument(self) -> Instrument:
    return self.__instrument
  
  @title.setter
  def title(self, title: str):
    self.__title = title
  @artist.setter
  def artist(self, title: str):
    self.__artist = title
    
  @release_year.setter
  def release_year(self, release_year: int):
    self.__release_year = release_year
    

  @instrument.setter
  def instrument(self, instrument: Instrument):
    self.__instrument = instrument
  def __str__(self) -> str:
        return (
            f"Titre: {self.__title}\n"
            f" Artiste: {self.__artist}\n"
            f" Annee de sortie: {self.__release_year}\n"
            f" Instrument: {self.__instrument}")
  def play(self):
    formatted_title = f"{self.title:<{self.max_len_str_attr}}"  
    formatted_title = f"{self.title:<{self.max_len_str_attr}}"
    print(f"Joue {formatted_title} solo avec ", end="")
    self.instrument.play()
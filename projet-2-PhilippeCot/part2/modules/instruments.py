from abc import ABC, abstractmethod



INSTRUMENT_NAME_WIDTH = 16

class Instrument(ABC):
  
  def __init__(self, brand:str):
    self._brand = brand
  
  def __repr__(self) -> str:
    return f"{self.__class__.__name__}(brand='{self._brand}')"
  
  @abstractmethod
  def play(self):
    pass


class Guitar(Instrument):
 
  def __init__(self, brand: str):
    super().__init__(brand)


  def play(self):
    print(f"*** guitare ***".ljust(INSTRUMENT_NAME_WIDTH) + f" du fabricant {self._brand}")

class Piano(Instrument):
 
  def __init__(self, brand: str):
    super().__init__(brand)

  def play(self):  
    print(f"*** piano ***".ljust(INSTRUMENT_NAME_WIDTH) + f" du fabricant {self._brand}")

class Drum(Instrument):
  
  def __init__(self, brand: str):
    super().__init__(brand)

  def play(self):  
    print(f"*** batterie ***".ljust(INSTRUMENT_NAME_WIDTH) + f" du fabricant {self._brand}")
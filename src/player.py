# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, species, currentRoom):
    self._name = name
    self._species = species
    self._currentRoom = currentRoom

  def __str__(self):
    return f"something something... my name was something... ahhh right its {self._name} and I am {self._species} in the {self._currentRoom}"
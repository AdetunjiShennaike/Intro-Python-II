# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc, items):
    self._name = name
    self._desc = desc
    self._items = items

  def __str__(self):
    return f"Room: {self._name}\nContained Items: {self._items}\nDescription of the Room: {self._desc}"
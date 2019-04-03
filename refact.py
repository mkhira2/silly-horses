import time, random
from colorama import init, Fore  #We should note to install this locally


class Horse:
    '''
    Defines a Horse

    Attributes:
      name: Whats a horse without a name
      number: We need to know the number
      color: Maybe I'll use this maybe I wont
      jockey: TODO Kenji can use this however he sees fit
    '''

    #Setting Jockey and Color to default as None for now, class level constants are OK
    def __init__(self, name, number, color=None, jockey=None):
        self.name = name
        self.number = number
        self.color = color
        self.jockey = jockey

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number


class Track(Horse):
    def __init__(self, track):
        self.track = track
        self.start_gate = []

    def getTrackName(self):
        return self.track

    def pop_starting_gate(self, horse):
        self.start_gate.append(horse)


kenji = Horse('kenji', 11)
patrick = Horse('patrick', 14)
james = Horse('james', 22)

gate = [kenji, james, patrick]

delta = Track('delta_downs')

for horse in gate:
    delta.pop_starting_gate(horse)

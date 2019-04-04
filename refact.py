import time, random
from dataclasses import dataclass
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
        #TODO write func to make check if number is 1-8 (or take any input and have internal value...maybe this lives on the Track Class)
        self.number = number
        self.color = color
        self.jockey = jockey

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number


'''
Alternatively you can use a dataclass.
Personally I think this is the better approach as the Horse is pure data.
Unfortunately dataclasses are only available in python3.7
'''


@dataclass
class DataClassHorse:
    name: str
    number: int
    color: str = None
    jockey: str = None


class Track(Horse):
    '''
    TODO add a fields to deal with text in race, this way you can instantiate new classes with the text you'd like.
    ie self.welcome = welcome
    '''

    def __init__(self, track):
        self.track = track
        self.start_gate = []
        self.bet = None

    def welcome(self):
        # welcome message
        print('\n***---------------------------------------------------***')
        print('Welcome to the races here at {0}!'.format(self.track))
        time.sleep(3)
        print('Step right up and place your bets!\n')
        time.sleep(3)

    def race(self):
        # race
        print('Here comes the {0} horse, {1}!'.format(
            self.start_gate[0].number, self.start_gate[0].name))
        time.sleep(3)
        print('{0}, the {1} horse, is falling behind!'.format(
            self.start_gate[1].name, self.start_gate[1].number))
        time.sleep(3)
        print(
            'And now from the back, the {0} horse {1} is coming up strong!\n'.
            format(self.start_gate[2].number, self.start_gate[2].name))
        time.sleep(3)
        print('They\'re at the finish line, and out of nowhere it\'s the...\n')
        time.sleep(4)
        print(Fore.GREEN + '{0} horse, {1}, for the win!\n'.format(
            self.start_gate[2].number, self.start_gate[2].name))
        time.sleep(2)

    def getTrackName(self):
        return self.track

    def pop_gate(self, gate):
        #Takes a list of horses and populates them into a starting gate
        for horse in gate:
            self.start_gate.append(horse)

    def assoc_horse(self):
        for horse in self.start_gate:
            print(horse.number)


kenji = Horse('kenji', 1)
patrick = Horse('patrick', 2)
james = Horse('james', 3)

gate = [kenji, james, patrick]

d = Track('delta_downs')
d.pop_gate(gate)
d.welcome()
d.race()

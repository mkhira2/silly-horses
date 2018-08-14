import time, random
from colorama import init, Fore

init(autoreset=True)

# global variables; increments if user opts to play_again
raceNumber = 1
betsWon = 0
betsLost = 0
play = True

while play:

    # personal preference
    def wait(seconds):
        time.sleep(seconds)

    def getRandomHorseName():
        return random.choice(allHorseNames)

    allHorseNames = ['Bad Horse', 'Big John', 'Dollar', 'Gunpowder', 'Maximus', 'Shadowfax', 'Sylvester', 'Two Bits']

    # get horse names and numbers
    horseNames = {}
    horseIndexes = {}
    for i in range(4):
        horseNames[i] = getRandomHorseName()
        horseIndexes[i] = allHorseNames.index(horseNames[i]) + 1

    # welcome message
    print('\n***---------------------------------------------------***')
    print('Welcome to Race #{} here at Ham Sandwich Downs!'.format(raceNumber))
    wait(3)
    print('Step right up and place your bets!\n')
    wait(3)

    # validate user input is a number between 1-8
    while True:
        try:
            myBet = int(raw_input('Which horse would you like to bet on? Please select 1-8: '))
        except ValueError:
            print('That\'s not a number!\n')
        else:
            if 1 <= myBet <= 8:
                break
            else:
                print('That horse isn\'t running tonight.\n')

    # get bet from user
    print(Fore.GREEN + 'Alright, your bet is placed for the {} horse, {}. Good luck!\n'.format(myBet, allHorseNames[myBet - 1]))
    wait(2)

    # pre-race
    print('Horses 1-8, lined up!')
    wait(2)
    print('Are you ready?..')
    wait(2)
    print('And they\'re off!\n')
    wait(2)

    # race
    print('Here comes the {} horse, {}!'.format(horseIndexes[0], horseNames[0]))
    wait(3)
    print('{}, the {} horse, is falling behind!'.format(horseNames[1], horseIndexes[1]))
    wait(3)
    print('And now from the back, the {} horse {} is coming up strong!\n'.format(horseIndexes[2], horseNames[2]))
    wait(3)
    print('They\'re at the finish line, and out of nowhere it\'s the...\n')
    wait(4)
    print(Fore.GREEN + '{} horse, {}, for the win!\n'.format(horseIndexes[3], horseNames[3]))
    wait(2)

    # resolve bet
    if (myBet == horseIndexes[3]):
        betsWon = betsWon + 1
        print('You won!\n')
        wait(2)
    else:
        betsLost = betsLost + 1
        print('You lost.\n')
        wait(2)
    
    # ask user to play again
    play_again = raw_input("If you'd like to play again, please type 'yes': ")
    if play_again.lower() == 'yes' or play_again.lower() == 'y':
        raceNumber += 1
        continue
    else:
        print('Thanks for playing. You won {} bet(s) and lost {} bet(s).'.format(betsWon, betsLost))
        break
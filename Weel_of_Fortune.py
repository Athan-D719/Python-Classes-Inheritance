import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWEL_COST = 250
VOWELS = 'AEIOU'

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv += '_'
        else:
            rv += s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

category, phrase = getRandomCategoryAndPhrase()

guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

print("\n{}\n".format("-"*5))

print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]), obscurePhrase(phrase, guessed)))

print("\n{}\n".format("-"*5))

obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}".format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]), showBoard(phrase, obscured_phrase, guessed)))

print("\n{}\n".format("-"*5))

num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())


print("\n{}\n".format("-"*5))

print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")

time.sleep(2)

min_t = 1
max_t = 10
print(getNumberBetween('Testing getNumberBetween(). Enter a number between {} and {}'.format(min_t, max_t), min_t, max_t))

#################################################################################
################################################################################

# Write the WOFPlayer class definition (part A) here
class WOFPlayer(object):
    
    def __init__(self, name): # prizes = []
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self,prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
        self.prizeMoney = 0
        self.prizes = []

    def getMove(self,category, obscuredPhrase, guessed):
        return input("{} has ${} \n\n Category: {} \n Phrase:  {} \n Guessed: {} \n\n Guess a letter, phrase, or type 'exit' or 'pass': ".format(self.name, self.prizeMoney, category, obscured_phrase, guessed))

    def __str__(self):
        return "{} ({})".format(self.name, self.prizeMoney)
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self,name,d):
        WOFPlayer.__init__(self,name)
        self.difficulty = d
        self.prizeMoney = 0
        self.prizes = []

    def smartCoinFlip(self):
        if random.ranint(1,10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self,guessed):
        a = []
        if self.prizeMoney < VOWEL_COST:
            for i in LETTERS:
                if i in VOWELS:
                    continue
                else:
                    if i in guessed:
                        continue
                    else:
                        a.append(i)
            return ''.join(a)
        else:
            for i in LETTERS:
                if i in guessed:
                    continue
                else:
                    a.append(i)
            return ''.join(a)

    def getMove(self,category, obscuredPhrase, guessed):
        #if self.smartCoinFlip() == True:

        if len(self.getPossibleLetters(guessed)) < 1:
            return 'pass'
        else:
            return self.getPossibleLetters(guessed)
a = WOFPlayer('hehe')
c = WOFHumanPlayer('hello')
b = WOFComputerPlayer('jiojio',2)
#print(a)
print(a.prizeMoney)
a.addMoney(2)
print(a.prizeMoney)
print(c.prizeMoney)
print(b.prizeMoney)








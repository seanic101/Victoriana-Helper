import random

random.seed()

class DiceRoller:

    @classmethod
    def __rollD6(cls, numberOfDice : int): #__ denotes a private method
        rolls = [random.randint(1, 6) for i in range(numberOfDice)] # list comprehension
        print(rolls)
        return rolls

    @classmethod # basically a static method
    def rollSuccesses(cls, numberOfDice : int, diceType='white'):
        firstRole = cls.__rollD6(numberOfDice=numberOfDice)

        # count the number of ones
        numberOfOnes = sum([1 if roll == 1 else 0 for roll in firstRole])

        # count the number of sixes
        numberOfSixes = sum([1 if roll == 6 else 0 for roll in firstRole])

        numberOfSuccesses = numberOfOnes + numberOfSixes

        # if we are rolling white dice, reroll the sixes, otherwise don't
        if diceType == 'white':
            secondRole = cls.__rollD6(numberOfDice=numberOfSixes)

            # count the number of ones and sixes in the second role and add it to the number of successes
            numberOfSuccesses += sum([1 if roll == 6 or roll == 1 else 0 for roll in secondRole])

        return numberOfSuccesses

for i in range(10):
    print(DiceRoller.rollSuccesses(6))
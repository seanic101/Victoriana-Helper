import random

random.seed()

class DiceRoller:

    @classmethod
    def __roll_d6(cls, number_of_dice : int): #__ denotes a private method
        """
        Rolls numberOfDice 6 sided dice and returns a list of the results
        :param number_of_dice: the number of dice to roll
        :return: a list of the dice roll outcomes
        """
        rolls = [random.randint(1, 6) for i in range(number_of_dice)] # list comprehension
        print(rolls)
        return rolls

    @classmethod # basically a static method
    def roll_successes(cls, number_of_dice : int, dice_type='white'):
        """

        :param number_of_dice:
        :param dice_type:
        :return:
        """
        first_roll = cls.__roll_d6(number_of_dice=number_of_dice)

        # count the number of ones
        number_of_ones = sum([1 if roll == 1 else 0 for roll in first_roll])

        # count the number of sixes
        number_of_sixes = sum([1 if roll == 6 else 0 for roll in first_roll])

        number_of_successes = number_of_ones + number_of_sixes

        # if we are rolling white dice, reroll the sixes, otherwise don't
        if dice_type == 'white':
            second_roll = cls.__roll_d6(number_of_dice=number_of_sixes)

            # count the number of ones and sixes in the second role and add it to the number of successes
            number_of_successes += sum([1 if roll == 6 or roll == 1 else 0 for roll in second_roll])

        return number_of_successes

#print(DiceRoller.roll_successes(8))
#print(DiceRoller.roll_successes(3, dice_type='black'))
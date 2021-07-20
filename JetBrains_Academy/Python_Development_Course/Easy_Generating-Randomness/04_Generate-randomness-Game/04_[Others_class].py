import random


def create_triad_counts():
    """Builds a dictionary whose keys are triads, and values are a list of length 2."""
    triads = [str(i) + str(j) + str(k) for i in range(2) for j in range(2) for k in range(2)]
    triad_counts = {}

    for triad in triads:
        triad_counts[triad] = [0, 0]

    return triad_counts


def filter_string(string, *characters):
    """Takes a string and removes all but the specified characters."""
    return ''.join([character for character in string if character in characters])


def predict_next(triad, triad_counts):
    """Predicts and returns the next number in a string of 1s and 0s"""
    if triad_counts[triad][0] > triad_counts[triad][1]:
        return '0'
    if triad_counts[triad][0] < triad_counts[triad][1]:
        return '1'
    if triad_counts[triad][0] == triad_counts[triad][0]:
        return random.choice(['0', '1'])


class PredictionGame:
    counts = create_triad_counts()

    def __init__(self):
        self.learning_string = ''
        self.test_string = ''
        self.triad_counts = dict(PredictionGame.counts)
        self.prediction = ''
        self.capital = 1000

    def main(self):
        while True:
            if len(self.test_string) == 0:
                self._update_test_string()
                return self.main()
            if self.test_string == 'enough':
                print("Game over!")
                return

            self._make_prediction()

            print('prediction:')
            print(self.prediction + '\n')

            self._calculate_accuracy()
            print(f'Your capital is now ${self.capital}')
            self.prediction = ''

            self._update_test_string()

    def setup(self):
        print("Please give AI some data to learn...")
        print("The current data length is 0, 100 symbols left")
        self._update_learning_string(100)

        print("\nFinal data string: ")
        print(self.learning_string + '\n')
        print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')

        self._update_triad_counts()
        self._update_test_string()

        return

    def _update_learning_string(self, length):
        """Prompts a user for strings until a string of specified length with 0s and 1s is obtained."""
        user_string = input("Print a random string containing 0 or 1: ")
        full_string = filter_string(user_string, '0', '1')
        while True:
            if len(full_string) >= length:
                break
            else:
                print(f'\nCurrent data length is {len(full_string)}, {length - len(full_string)} symbols left')
                more = input("Print a random string containing 0 or 1: ")
                filtered_input = filter_string(more, '0', '1')
                full_string += filtered_input

        self.learning_string = full_string

        return

    def _update_triad_counts(self):
        """Calculates how many times each triad is followed by a 1 and 0, and updates the triad_counts attribute."""
        for i in range(len(self.learning_string) - 3):
            triad = self.learning_string[i] + self.learning_string[i + 1] + self.learning_string[i + 2]

            if self.learning_string[i + 3] == '0':
                self.triad_counts[triad][0] += 1
            elif self.learning_string[i + 3] == '1':
                self.triad_counts[triad][1] += 1

        return

    def _update_test_string(self):
        string = input("Print a random string containing 0 or 1:\n\n")
        if string == 'enough':
            self.test_string = string
            return

        self.test_string = filter_string(string, '0', '1')

        return

    def _make_prediction(self):
        """Makes a string prediction of the same length as the test string based on triad statistics."""
        for i in range(3):
            self.prediction += random.choice(['0', '1'])

        for i in range(len(self.test_string) - 3):
            triad = self.test_string[i] + self.test_string[i + 1] + self.test_string[i + 2]
            self.prediction += predict_next(triad, self.triad_counts)

        return

    def _calculate_accuracy(self):
        """Calculates the accuracy of the prediction and updates the capital count accordingly."""
        same = 0
        dif = 0
        for x, y in zip(self.test_string[3:], self.prediction[3:]):
            if x == y:
                same += 1
            else:
                dif += 1

        accuracy = round((same / (same + dif)) * 100, 2)
        print(f'Computer guessed right {same} out of {same + dif} symbols ({accuracy} %)')
        self.capital += dif
        self.capital -= same

        return


game = PredictionGame()
game.setup()
game.main()
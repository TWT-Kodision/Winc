# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'
from decimal import*

# Add your code after this line
class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = str(name)
        self.speed = float(speed)
        self.endurance = float(endurance)
        self.accuracy = float(accuracy)
       
        if 0 <= self.speed <= 1 and 0 <= self.endurance <= 1 and 0 <= self.accuracy <= 1:    
            print("all values are correct")
        else:
            raise ValueError()

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."
    
    #create a list of tuple in specific order
    def create_tuple(self):
        speedTuple = ("speed", self.speed)
        enduranceTuple = ("endurance", self.endurance)
        accuracyTuple = ("accuracy", self.accuracy)
        combined = (speedTuple, enduranceTuple, accuracyTuple)
        return combined
    
    #get highest number from list of tuple, returns tuple
    def find_highest_tuple(self, tuple):
        highest = tuple[0]
        if tuple[1][1] > tuple[0][1]:
            highest = tuple[1]
        if tuple[2][1] > highest[1]:
            highest = tuple[2]
        return highest

    def strength(self):
        best_strength = self.find_highest_tuple(self.create_tuple())
        return best_strength

class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        sum = getattr(player,"speed") + getattr(player,"endurance") + getattr(player,"accuracy")
        return sum

    #compares the sum of specs of 2 players and returns the highest or if even a string
    def compare_sum_player(self, playerA, playerB):
        sum_playerA = self.sum_player(playerA)
        sum_playerB = self.sum_player(playerB)
        if sum_playerA == sum_playerB:
            return 'These two players might as well be twins!'
        elif sum_playerA > sum_playerB:
            return getattr(playerA, "name")
        else:
            return getattr(playerB, "name")

    def compare_players(self, playerA, playerB, spec):
        spec_playerA = (getattr(playerA, spec))
        spec_playerB = (getattr(playerB, spec))
        if spec_playerA == spec_playerB:
            return self.compare_sum_player(playerA, playerB)
        elif spec_playerA>spec_playerB:    
            return getattr(playerA,"name")
        else:
            return getattr(playerB,"name")
 
test = Player("test", 0, 1, 0.6)
ray = Commentator('Ray Hudson')
alice = Player('Alice', 0.7, 0.3, 0.6)
bob = Player('Bob', 0.7, 0.4, 0.6)
print(ray.compare_players(alice, bob, 'speed'))

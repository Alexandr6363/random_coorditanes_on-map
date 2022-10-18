import random

Arr1 = ["S", "N"]
Arr2 = ["E", "W"]


class Coordinate:
    def __init__(self):
        self.meridian = round(random.uniform(0, 180), 5)
        self.side_SN = random.choice(Arr1)
        self.palallels = round(random.uniform(0, 90), 5)
        self.side_EW = random.choice(Arr2)

    def __str__(self):
        return f"{self.side_SN} {str(self.palallels)} " \
               f"{self.side_EW} {str(self.meridian)}"


list_of_cord = [Coordinate() for i in range(20)]
for cord in list_of_cord:
    print(cord)
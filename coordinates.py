import random

Arr1 = ["S", "N"]
Arr2 = ["E", "W"]


class Coordinate:
        def __init__(self):
            self.meridian_degrees = random.randint(0, 180)
            self.meridian_minutes = random.randint(0, 60)
            self.meridian_seconds = round(random.uniform(0, 60), 2)
            self.side_SN = random.choice(Arr1)
            self.parallels_degrees = random.randint(0, 90)
            self.parallels_minutes = random.randint(0, 60)
            self.parallels_seconds = round(random.uniform(0, 60), 2)
            self.side_EW = random.choice(Arr2)
            self.coordinate_link = f"https://www.google.com/maps/place/" \
                   f"{self.parallels_degrees}%C2%B0{self.parallels_minutes}'" \
                   f"{self.parallels_seconds}%22{self.side_SN}+" \
                   f"{self.meridian_degrees}%C2%B0{self.meridian_minutes}'" \
                   f"{self.meridian_seconds}%22{self.side_EW}/"

        def __str__(self):
            return self.coordinate_link

        def write_list_of_coordinates_in_file(self):
            with open("link_list.txt", "a") as file:
                file.write(self.coordinate_link)
                file.write("\n")


list_of_cord = [Coordinate() for i in range(20)]
for cord in list_of_cord:
    cord.write_list_of_coordinates_in_file()
    print(cord)



"""
https://www.google.com/maps/place/20%C2%B056'11.0%22S+55%C2%B024'03.6%22W/

56° 34' 14.04'

"""
# return f"{self.side_EW} {self.parallels_degrees} {self.parallels_minutes} {self.parallels_seconds}" \
#        f"{self.side_SN} {self.meridian_degrees} {self.meridian_minutes} {self.meridian_seconds}"








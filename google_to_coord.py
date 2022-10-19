

with open("google_coord.txt", "r") as file:
    coordinates = file.read().splitlines()

list_of_coord = []
for coordinat in coordinates:
    coord_in_string = coordinat[34:36] + "\xb0" + coordinat[42:49] + coordinat[52] +\
                      " " + coordinat[54:56] + "\xb0" + coordinat[62:69] + coordinat[73]
    list_of_coord.append(coord_in_string)


with open("coord_from_google.txt", "w") as file:
    for coord in list_of_coord:
        file.write(coord)
        file.write('\n')



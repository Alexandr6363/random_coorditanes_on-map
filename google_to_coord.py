

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
"""
https://www.google.com/maps/place/80%C2%B042'12.86%22S+050%C2%B004'01.71%22E/
https://www.google.com/maps/place/44%C2%B049'06.0%22S+89%C2%B002'31.4%22W
"""




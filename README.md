# random_coorditanes_on-map
This code get a list of random coordinates in 2 files: 
in one file there is the list of classic view of coordinates:
"N 74.61868 E 32.38444"
in second file there is a random list of link to googlemaps: 
"https://www.google.com/maps/place/69%C2%B039'33.17%22N+162%C2%B059'36.47%22W/"
- Файл coordinates.py создает список случайных координат и записывает их в файл txt, также параллельно сосдает список с координатами в формате google maps и записывает его в другой файл
- Файл google_to_coord.py извлекает из списка ссылок из google maps координаты и записывает файл со списком координат в формате "64°13'01.6S 12°059'30.W"
- The coordinates.py file creates a list of random coordinates and writes them to a txt file, also creates a list with coordinates in google maps format in parallel and writes it to another file
- The google_to_coord.py file extracts coordinates from a list of links from google maps and writes a file with a list of coordinates in the format "64°13'01.6S 12°059'30.W"

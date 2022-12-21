
from exif import Image
import os
import matplotlib.pyplot as plot

directory = 'pokemon'
 
# iterate over files in
# that directory
lats = []
longs = []

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    with open(f, 'rb') as image_file:
        image = Image(image_file)
        lat = image.gps_latitude
        latRef = image.gps_latitude_ref
        long = image.gps_longitude
        longRef = image.gps_longitude_ref
        lats.append(decimal_coords(lat, latRef))
        longs.append(decimal_coords(long, longRef))

plot.scatter(lats, longs)
plot.show()
import csv
import json
from collections import OrderedDict
import math
import pyproj


def calR(area):
    area = float(area)
    return math.sqrt(area/math.pi)

def changeformat(x, y):
    transformer = pyproj.Transformer.from_crs("EPSG:26917", "EPSG:4326")
    x1,y1= transformer.transform(x, y)

    return x1, y1

x,y = changeformat(167141.3,1112.351)
print(x,y)




li = []
with open('../assets/taz-centers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    for taz,coordx,coordy,area in reader:
        print(taz,coordx,coordy,area)
        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [changeformat(float(coordx), float(coordy))]
        }
        d['properties'] = {
            'taz': taz,
            'radius': calR(area)
        }
        li.append(d)

d = OrderedDict()
d['type'] = 'FeatureCollection'
d['features'] = li
with open('../assets/Geo_chargers.json', 'w') as f:
    f.write(json.dumps(d, sort_keys=False, indent=4))
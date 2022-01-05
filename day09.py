import sys
from collections import defaultdict
from itertools import permutations

input = """
Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
"""

star1 = 0
star2 = 0 

routes = defaultdict(dict)
cities = set()

for line in input.strip().split("\n"):
  distance = line.split(" = ")[1]
  route1 = line.split(" = ")[0].split(" to ")[0]
  route2 = line.split(" = ")[0].split(" to ")[1]

  cities.add(route1)
  cities.add(route2)
  
  routes[route1][route2] = int(distance)
  routes[route2][route1] = int(distance)

shortest_distance = 10000
longest_distance = 0

for city in permutations(cities):
  distance = 0
  for n, k in enumerate(list(city)):
    if n == len(cities)-1:
      break
    distance += routes[city[n]][city[n+1]]

  if distance < shortest_distance:
    shortest_distance = distance
  else:
    shortest_distance = shortest_distance

  if distance > longest_distance:
    longest_distance = distance
  else:
    longest_distance = longest_distance

star1 = shortest_distance
star2 = longest_distance

print("star 1: ", star1)
print("star 2: ", star2)
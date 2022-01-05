input = """
Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.
"""

rules = dict()

for line in input.strip().split("\n"):
  name, _, _, kms, _, _, seconds, _, _, _, _, _, _, rest, _ = line.split(" ")
  rules[name] = dict()
  rules[name]["kms"] = int(kms)
  rules[name]["seconds"] = int(seconds)
  rules[name]["rest"] = int(rest) + int(seconds)
  rules[name]["distance_traveled"] = int(rules[name]["kms"])
  rules[name]["lead_points"] = 0 

for tick in range(1,2503):
  for k, v in rules.items():
    if tick % rules[k]["rest"] < rules[k]["seconds"]:
      distance_change = rules[k]["distance_traveled"] + rules[k]["kms"]
      rules[k]["distance_traveled"] = distance_change

  ds = []
  for k, v in rules.items():
    ds.append(v["distance_traveled"])
  max_distance = max(ds)
  for k, v in rules.items():
    if v["distance_traveled"] == max_distance:
      lead_points = rules[k]["lead_points"] + 1
      rules[k]["lead_points"] = lead_points

distances = []
points = []
for v in rules.values():
  distances.append(v["distance_traveled"])
  points.append(v["lead_points"])

star1 = max(distances)
star2 = max(points) + 1

print("star 1:", star1)
print("star 2:", star2)
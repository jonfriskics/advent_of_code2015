import itertools

input = """
Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
"""

ingredients = dict()

for line in input.strip().split("\n"):
  ingredient_name, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split(" ")
  ingredient_name = ingredient_name.rstrip(":")
  ingredients[ingredient_name] = dict()
  ingredients[ingredient_name]["capacity"] = int(capacity.rstrip(','))
  ingredients[ingredient_name]["durability"] = int(durability.rstrip(','))
  ingredients[ingredient_name]["flavor"] = int(flavor.rstrip(','))
  ingredients[ingredient_name]["texture"] = int(texture.rstrip(','))
  ingredients[ingredient_name]["calories"] = int(calories)

star1 = 0
star2 = 0 

total_capacity = 0
total_durability = 0
total_flavor = 0
total_texture = 0

total_ingredients = 100

total_scores = []
total_scores_calorie_limited = []

for i1 in range(total_ingredients):
  for i2 in range(total_ingredients - i1):
    for i3 in range(total_ingredients - i1 - i2):
      i4 = total_ingredients - i1 - i2 - i3
      total_capacity = i1 * ingredients["Sugar"]["capacity"] + i2 * ingredients["Sprinkles"]["capacity"] + i3 * ingredients["Candy"]["capacity"] + i4 * ingredients["Chocolate"]["capacity"]
      total_durability = i1 * ingredients["Sugar"]["durability"] + i2 * ingredients["Sprinkles"]["durability"] + i3 * ingredients["Candy"]["durability"] + i4 * ingredients["Chocolate"]["durability"]
      total_flavor = i1 * ingredients["Sugar"]["flavor"] + i2 * ingredients["Sprinkles"]["flavor"] + i3 * ingredients["Candy"]["flavor"] + i4 * ingredients["Chocolate"]["flavor"]
      total_texture = i1 * ingredients["Sugar"]["texture"] + i2 * ingredients["Sprinkles"]["texture"] + i3 * ingredients["Candy"]["texture"] + i4 * ingredients["Chocolate"]["texture"]
      total_calories = i1 * ingredients["Sugar"]["calories"] + i2 * ingredients["Sprinkles"]["calories"] + i3 * ingredients["Candy"]["calories"] + i4 * ingredients["Chocolate"]["calories"]

      if total_capacity < 0:
        total_capacity = 0
      if total_durability < 0:
        total_durability = 0
      if total_flavor < 0:
        total_flavor = 0
      if total_texture < 0:
        total_texture = 0

      total_score = total_capacity * total_durability * total_flavor * total_texture
      total_scores.append(total_score)

      if total_calories == 500:
        total_scores_calorie_limited.append(total_score)

star1 = max(total_scores)
star2 = max(total_scores_calorie_limited)

print("star 1", star1)
print("star 1", star2)
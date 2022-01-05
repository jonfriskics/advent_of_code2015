input = """
Hit Points: 100
Damage: 8
Armor: 2
"""

my_hp = 100
my_damage = 0
my_armor = 0
boss_hp = 0
boss_damage = 0
boss_armor = 0

boss_hp = int(input.strip().split("\n")[0].split(": ")[1])
boss_damage = int(input.strip().split("\n")[1].split(": ")[1])
boss_armor = int(input.strip().split("\n")[2].split(": ")[1])

# print(f"\nmy_hp   {my_hp}\tmy_damage   {my_damage}\tmy_armor   {my_armor}\nboss_hp {boss_hp}\tboss_damage {boss_damage}\tboss_armor {boss_armor}")

weapons = [
  {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
  {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
  {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
  {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
  {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}
]

armor = [
  {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
  {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
  {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
  {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
  {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5},
  {"name": "none", "cost": 0, "damage": 0, "armor": 0}
]

rings = [
  {"name": "DamagePlus1", "cost": 25, "damage": 1, "armor": 0},
  {"name": "DamagePlus2", "cost": 50, "damage": 2, "armor": 0},
  {"name": "DamagePlus3", "cost": 100, "damage": 3, "armor": 0},
  {"name": "none-damage", "cost": 0, "damage": 0, "armor": 0},
  {"name": "DefensePlus1", "cost": 20, "damage": 0, "armor": 1},
  {"name": "DefensePlus2", "cost": 40, "damage": 0, "armor": 2},
  {"name": "DefensePlus3", "cost": 80, "damage": 0, "armor": 3},
  {"name": "none-armor", "cost": 0, "damage": 0, "armor": 0}
]

my_wins = []
my_losses = []

for w in range(len(weapons)):
  for a in range(len(armor)):
    for r1 in range(len(rings)):
      for r2 in range(len(rings)):
        bhp = boss_hp
        mhp = my_hp

        if r1 == r2:
          continue

        ring_damage = 0
        ring_armor = 0

        if rings[r1]["damage"] > 0:
          ring_damage += rings[r1]["damage"]
        elif rings[r1]["armor"] > 0:
          ring_armor += rings[r1]["armor"]
        if rings[r2]["damage"] > 0:
          ring_damage += rings[r2]["damage"]
        elif rings[r2]["armor"] > 0:
          ring_armor += rings[r2]["armor"]
        
        cost = weapons[w]["cost"] + armor[a]["cost"] + rings[r1]["cost"] + rings[r2]["cost"]
        my_damage = weapons[w]["damage"] + ring_damage
        my_armor = armor[a]["armor"] + ring_armor

        winner = False
        while not winner:
          bhp = bhp - (my_damage - boss_armor)
          if bhp <= 0:
            my_wins.append(cost)
            winner = True
            break
          mhp = mhp - (boss_damage - my_armor)
          if mhp <= 0:
            my_losses.append(cost)
            winner = True
            break

star1 = min(my_wins)
star2 = max(my_losses)

print("star 1", star1)
print("star 2", star2)
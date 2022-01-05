import itertools

input = """
Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George.
"""

seating = dict()
for line in input.strip().split("\n"):
  person_name, _, direction, amount, _, _, _, _, _, _, seatmate_name = line.split(" ")
  if person_name not in seating.keys():
    seating[person_name] = dict()

  if direction == "gain":
    amount = int(amount) * 1
  elif direction == "lose":
    amount = int(amount) * -1

  seatmate_name = seatmate_name.rstrip(".")
  seating[person_name][seatmate_name] = amount

arrangement = list(seating.keys())

perms = list(itertools.permutations(arrangement))

total_costs = []

for arr in perms:
  total_cost = 0
  for n in range(len(arr)):
    person = arr[n]
    seated_to_right = ""
    seated_to_left = ""
    if n == len(arr) - 1:
      seated_to_right = arr[0]
    else:
      seated_to_right = arr[n+1]
    
    if n == 0:
      seated_to_left = arr[len(arr)-1]
    else:
      seated_to_left = arr[n-1]

    total_cost += seating[person][seated_to_right] + seating[person][seated_to_left]
  total_costs.append(total_cost)

star1 = max(total_costs)

input = """
Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Alice would gain 0 happiness units by sitting next to Jon.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Bob would gain 0 happiness units by sitting next to Jon.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
Carol would gain 0 happiness units by sitting next to Jon.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
David would gain 0 happiness units by sitting next to Jon.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Eric would gain 0 happiness units by sitting next to Jon.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
Frank would gain 0 happiness units by sitting next to Jon.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
George would gain 0 happiness units by sitting next to Jon.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George.
Mallory would gain 0 happiness units by sitting next to Jon.
Jon would gain 0 happiness units by sitting next to Alice.
Jon would gain 0 happiness units by sitting next to Bob.
Jon would gain 0 happiness units by sitting next to Carol.
Jon would gain 0 happiness units by sitting next to David.
Jon would gain 0 happiness units by sitting next to Eric.
Jon would gain 0 happiness units by sitting next to Frank.
Jon would gain 0 happiness units by sitting next to George.
Jon would gain 0 happiness units by sitting next to Mallory.
"""

seating = dict()
for line in input.strip().split("\n"):
  person_name, _, direction, amount, _, _, _, _, _, _, seatmate_name = line.split(" ")
  if person_name not in seating.keys():
    seating[person_name] = dict()

  if direction == "gain":
    amount = int(amount) * 1
  elif direction == "lose":
    amount = int(amount) * -1

  seatmate_name = seatmate_name.rstrip(".")
  seating[person_name][seatmate_name] = amount

arrangement = list(seating.keys())

perms = list(itertools.permutations(arrangement))

total_costs = []

for arr in perms:
  total_cost = 0
  for n in range(len(arr)):
    person = arr[n]
    seated_to_right = ""
    seated_to_left = ""
    if n == len(arr) - 1:
      seated_to_right = arr[0]
    else:
      seated_to_right = arr[n+1]
    
    if n == 0:
      seated_to_left = arr[len(arr)-1]
    else:
      seated_to_left = arr[n-1]

    total_cost += seating[person][seated_to_right] + seating[person][seated_to_left]
  total_costs.append(total_cost)

star2 = max(total_costs)

print("star 1:", star1)
print("star 2:", star2)
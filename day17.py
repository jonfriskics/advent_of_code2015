import itertools

input = """
33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42
"""

star1 = 0
star2 = 0

containers = []
storage_target = 150
solutions = []
sizes = []

for line in input.strip().split("\n"):
  containers.append(int(line))

for n in range(len(containers)):
  for combination in itertools.combinations(containers, n):
    if sum(combination) == storage_target:
      star1 += 1
      solutions.append(combination)

for solution in solutions:
  sizes.append(len(solution))

sizes.sort()

min_length = sizes[0]

for size in sizes:
 if size == min_length:
   star2 += 1

print("star 1", star1)
print("star 2", star2)
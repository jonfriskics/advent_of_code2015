input = int("34000000")

star1 = 0
star2 = 0

elves = dict()
houses = dict()

presents_delivered = 0
n = 1
while presents_delivered < input:
  break
  houses[n] = 0
  elves[n] = 0

  d = 0
  for k, v in elves.items():
    # print(f"k: {k} v: {v} n: {n}")
    if n % k == 0:
      d += k * 10
      # print(f"elf {k} delivers to house {n} these presents {houses[n]}")
    if d > input:
      presents_delivered = d
      star1 = n  
      break
  n += 1
  if n % 1000 == 0:
    print(n, d)

elves = dict()
houses = dict()

presents_delivered = 0
n = 1
while presents_delivered < input:
  houses[n] = 0
  elves[n] = 0

  d = 0
  for k, v in elves.items():
    # print(f"k: {k} v: {v} n: {n}")
    if n % k == 0 and elves[n] <= 50:
      elves[n] += 1
      d += k * 11
      # print(f"elf {k} delivers to house {n} these presents {houses[n]}")
    if d > input:
      presents_delivered = d
      star2 = n  
      break
  n += 1
  if n % 1000 == 0:
    print(n, d)

print("star 1", star1)
print("star 2", star2)
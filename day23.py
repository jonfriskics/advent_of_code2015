input = """
jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""

# set a to 0 for part 1, a to 1 for part 2
a = 1
b = 0

instructions = []

for line in input.strip().split("\n"):
  if len(line.split(", ")) == 2:
    if line.split(", ")[0].split(" ")[0] == "jio":
      instructions.append({"instruction": "jio", "register": line.split(", ")[0].split(" ")[1], "operation": int(line.split(", ")[1].split(" ")[0].lstrip("+"))})
    elif line.split(", ")[0].split(" ")[0] == "jie":
      instructions.append({"instruction": "jie", "register": line.split(", ")[0].split(" ")[1], "operation": int(line.split(", ")[1].split(" ")[0].lstrip("+"))})
  else:
    if line.split(" ")[0] == "inc":
      instructions.append({"instruction": "inc", "register": line.split(" ")[1]})
    elif line.split(" ")[0] == "tpl":
      instructions.append({"instruction": "tpl", "register": line.split(" ")[1]})
    elif line.split(" ")[0] == "hlf":
      instructions.append({"instruction": "hlf", "register": line.split(" ")[1]})
    elif line.split(" ")[0] == "jmp":
      instructions.append({"instruction": "jmp", "register": None, "operation": int(line.split(" ")[1].lstrip("+"))})

position = -1
n = 0
print(instructions)
while position < len(instructions) - 1:
  n = n + 1
  position = position + 1
  instruction = instructions[position]
  print(f"before n {n} position {position} a {a} b {b} {instruction}")
  if instruction["instruction"] == "hlf":
    if instruction["register"] == "a":
      a = a / 2
    else:
      b = b / 2
  elif instruction["instruction"] == "tpl":
    if instruction["register"] == "a":
      a = a * 3
    else:
      b = b * 3
  elif instruction["instruction"] == "inc":
    if instruction["register"] == "a":
      a = a + 1 
    else:
      b = b + 1
  elif instruction["instruction"] == "jmp":
    position += instruction["operation"] - 1
  elif instruction["instruction"] == "jie":
    if instruction["register"] == "a":
      if a % 2 == 0:
        position += instruction["operation"] - 1
    else:
      if b % 2 == 0:
        position += instruction["operation"] - 1
  elif instruction["instruction"] == "jio":
    if instruction["register"] == "a":
      if a == 1:
        position += instruction["operation"] - 1
    else:
      if b == 1:
        position += instruction["operation"] - 1
  print(f"after n {n} a {a} b {b}")
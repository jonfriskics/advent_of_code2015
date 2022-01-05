import os
from re import escape

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/day_08_input.txt', 'r')
input = file.read().strip().split('\n')

star1 = 0
star2 = 0

string_length = 0
memory_length = 0

for line in input:
  star1 += len(line)
  star1 -= len(eval(line))
  
for line in input:
  star2 += line.count('\\') + 2
  star2 += line.count('"')

print("star 1", star1)
print("star 2", star2)
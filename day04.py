import hashlib

input = "bgvyzdsv"

star1 = 0
star2 = 0

for n in range(0,10000000):
  hash_input = input + str(n)
  md5_hash = hashlib.md5(hash_input.encode())
  if md5_hash.hexdigest()[0:5] == "00000":
    if star1 == 0:
      star1 = n
  if md5_hash.hexdigest()[0:6] == "000000":
    if star2 == 0:
      star2 = n

print("star 1", star1)
print("star 2", star2)
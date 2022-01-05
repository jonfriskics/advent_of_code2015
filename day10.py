input = "1113222113"

star1 = 0
star2 = 0

def fresh_dictionary():
  sequence_as_dict = {}
  for n in range(0,10):
    sequence_as_dict[n] = 0
  return sequence_as_dict

def run_steps(steps, input):
  current_sequence = input
  sequence_as_dict = {}

  pos = 0
  new_char = True
  new_sequence = ""

  for _ in range(0,steps):
    while pos < len(current_sequence):
      if new_char == True:
        sequence_as_dict[int(current_sequence[pos])] = 1
      if pos < len(current_sequence) - 1:
        if current_sequence[pos] == current_sequence[pos + 1]:
          # next char matches
          sequence_as_dict[int(current_sequence[pos])] = sequence_as_dict[int(current_sequence[pos])] + 1
          # print(f"found matches {current_sequence[pos]} {current_sequence[pos+1]}, increment key {current_sequence[pos]} by one to new value {sequence_as_dict[int(current_sequence[pos])]} and pos {pos} by one")
          pos += 1
          new_char = False
        else:
          # next char doesn't match
          # print(f"didn't find match {current_sequence[pos]} {current_sequence[pos+1]}, advance pos {pos} by one")
          new_sequence += str(sequence_as_dict[int(current_sequence[pos])]) + str(current_sequence[pos])
          pos += 1
          new_char = True
      else:
        # end of sequence
        # print(f"pos {pos} is greater than or equal to {len(current_sequence)-1}")
        new_sequence += str(sequence_as_dict[int(current_sequence[pos])]) + str(current_sequence[pos])
        pos += 1
        new_char = False

    current_sequence = str(new_sequence)

    # reset variables for next step run
    pos = 0
    new_char = True
    new_sequence = ""
    sequence_as_dict = fresh_dictionary()

  return current_sequence

star1 = len(run_steps(40, input))
star2 = len(run_steps(50, input))

print("star 1", star1)
print("star 2", star2)
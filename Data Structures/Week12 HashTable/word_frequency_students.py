def max_word_count(filename):
  """
  # TODO: Use python dictionary to find the most frequent word in the input file
  # Please do not use the sorted(.) function for this exercise
  """
  max_word, max_count = '', 0

  # Phase 1: Count word occurrence
  d={}
  with open(filename, "r") as F:
    for line in F:
      words = line.strip().lower().split()
      # TODO
      # print(words)
      for w in words:
        d[w]=d.get(w, 0)+1
  # print(d)

  # Phase 2: Search a word with maximum occurrence
  # TODO: Use def items() in python dictionary to obtain a sequence of (key,value) pairs
  for k, v in d.items():
    if v>max_count:
      max_count=v
      max_word=k

  return max_word, max_count

if __name__ == '__main__':
  filename = 'inputtext2.txt'
  
  max_word, max_count = max_word_count(filename)
  
  print('The most frequent word is', max_word) # Expect: interest
  print('Its number of occurrences is', max_count) # Expect: 7

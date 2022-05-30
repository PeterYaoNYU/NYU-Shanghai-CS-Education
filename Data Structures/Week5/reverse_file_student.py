from array_stack_student import ArrayStack

def reverse_file(input_filename, output_filename):
  """Overwrite given file with its contents line-by-line reversed.
     Use with open(.) construct to read and write files as provided.
     Think about how to use ArrayStack to help you.
     You cannot use other data structures like Python List to complete this question.
  """
  # TODO
  stack=ArrayStack()

  with open(input_filename, 'r') as F:
    for line in F:
      line = line.rstrip('\n')
      # TODO
      stack.push(line)
      

  # now we overwrite with contents in LIFO order
  with open(output_filename, 'w') as F:
    # TODO
    while not stack.is_empty():
      line=stack.pop()
      F.write(line+'\n')
  

if __name__ == '__main__':
  reverse_file('DSSyllabus.txt', 'DSSyllabus_reverse.txt')

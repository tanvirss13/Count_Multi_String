# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1)
  
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

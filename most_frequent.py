from collections import Counter

def most_frequent(test_str):
    res = Counter(test_str)
    return res
  
test_str = input("Enter a string :=")
 

  
print (str(most_frequent(test_str)))


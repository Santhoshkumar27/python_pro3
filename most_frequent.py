string= input("enter a string")
  
all_freq = {}
  
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
print ("Count of all characters in, string, is :\n "+  str(all_freq))

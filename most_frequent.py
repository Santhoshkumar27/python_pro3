
string= input("Enter a string  :=  ")
  
all_freq = {}
def most_frequent():
    for i in string:
        if i in all_freq:
            all_freq[i]+= 1
            
        else:
            all_freq[i] = 1
   
most_frequent()  
print ("Count of all characters in, string, is :\n "+  str(all_freq))


#TKHERBI9999

import os
import csv
from collections import Counter
import time
from string import ascii_lowercase
start = time.time()
os.chdir('C:\\Users\\HAMZAFADIL\\Exercism\\python\\other')
with open("alice.txt",encoding="utf-8",mode="r") as alice:
    alice = alice.read()
alice = alice.lower()

lst = list(alice)
for word in lst:
    if word not in ascii_lowercase:
        del lst[lst.index(word)]
op = open("output.txt",mode="a",encoding="utf-8")
op.write(str(lst))
# for word in alice:
    
#     counts[word] +=1

# counts = sorted(counts.items())

# w = csv.writer(open("output.csv","w",encoding="utf-8"))
# for key,val in counts:
#     w.writerow([key,val])
# end = time.time()
# total = end - start
# print(f"Done in : {total} " )
#output= open("alice_word.txt",mode="a",encoding="utf-8")
#output.write(counts)

#Robert Nool III
#Ackermann's Function

import time
import sys
sys.setrecursionlimit(3000)
start = time.time()
#Start
i = 0
def ackermann(m,n):
     global i
     i = i+ 1
     if m == 0:
          return (n + 1)
     elif n == 0:
          return ackermann(m - 1, 1)
     else:
          return ackermann(m - 1, ackermann(m, n - 1)) 
          
x=int(input("What is the value for m? "))
print(x)

y=int(input("What is the value for n? "))
print(y)
print("\nThe result of your inputs according to the Ackermann Function is:")
print(ackermann(x, y)) 
print(i)
end = time.time()
total = end - start
print(f"Done in : {total}")
#End


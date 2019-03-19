
import sys
import time
sys.setrecursionlimit(15000)
start = time.time()
cache = {}
i = 0
def fib_dp(n):
    global i 
    i += 1
    if n in cache:
        return cache[n]
    if n == 0: return 0
    elif n == 1: return 1
    else:
        value = fib_dp(n-1) + fib_dp(n-2)
    cache[n] = value
    return value

print(fib_dp(3900))
print(i)
end = time.time()

total = end - start

print(total)
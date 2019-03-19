def is_armstrong(number):
    n = str(number)
    l = list(n)
    r = 0
    final = [int(i) for i in l]
    for i in final:
        r += i**len(final)
    if r == number:
        return True
    else:
        return False

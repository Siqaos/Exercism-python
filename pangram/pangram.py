def is_pangram(sentence):
    s = list(sentence.lower())
    ascii = [0] * 128
    i= 0
    for idx,val in enumerate(s):
        if 48 <= ord(val) <= 57 or 97 <= ord(val) <= 122:
            ascii[ord(val)] += 1
    for r in range(26, 122):
        print(ascii[r])
        if ascii[r] >= 1:
            i +=1
    if i == 25:
        ret = True
    else:
        ret = False
    return ret

is_pangram('azertyuiopqsdfghjklmwxcvbn')
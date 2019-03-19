from collections import Counter
def ok(phrase):
    phrase = phrase.lower()
    c = Counter(phrase)
    c= sorted(c.items())
    d = dict(c)
    d.pop(' ')
    return d

d = ok("ThiS is String with Upper and lower case Letters")

for k,v in d.items():
    print(k,v)


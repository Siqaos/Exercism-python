def two_fer(name):
    if name is None:
        name = "you"
        print(name)
    s1 = "One for "
    s2 = ", one for me."
    return s1+name+s2 
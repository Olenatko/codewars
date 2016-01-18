def multiple(x):
    x3 = x % 3
    x5 = x % 5
    if (x % 5 == 0) and (x % 3 == 0):
        return 'BangBoom'
    if x % 5 == 0:
        return 'Boom'
    if x % 3 == 0:
        return 'Bang'
    if x3 != 0 and x5 != 0:
        return 'Miss'
print(multiple(30))
print(multiple(3))
print(multiple(98))
print(multiple(65))
print(multiple(23))
print(multiple(15))
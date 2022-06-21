from functools import reduce

challenge = [2, 2, 2, 2, 2]

base = reduce(lambda a, b:a * b, challenge)

print(base)
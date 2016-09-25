import random

minval = 0
maxval = 10 ** 15

tests = []
for i in xrange(20):
    for j in xrange(20):
        x, y = (minval + i, maxval - j)
        tests.append((x, y))
        tests.append((y, x))

while len(tests) < 1000:
    a = random.randint(minval, maxval)
    b = random.randint(minval, maxval)
    tests.append((a, b))

random.shuffle(tests)

for a, b in tests:
    print a, b

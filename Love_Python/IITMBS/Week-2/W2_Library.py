import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(10,3))

import random
print(random.random()) #between 0 and 1

# let us simulate a coin toss
a=random.random()
if (a<.5):
    print("Head")
else:
    print("Tail")

# let us simulate a dice six face
print(random.randrange(1,7))

import random
import my_module

print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float_0_5 = random.randint(0,4) + random.random()
print(random_float_0_5)

random_float_0_5 = random.random() * 5
print(random_float_0_5)
import random
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
    
# height = 1146 / 7
# print(int(height))

# for n in range(1,11):
#     print(n)

# for n in range(0,11,2):
#     print(n)

# total = 0
# for n in range(1,101):
#     total += n
# print(total)

# target = 10
# for even in range(0, target + 1, 2):
#    print(even) 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

asci_table = [letters, numbers]
print(random.choice(asci_table[0]))

pass_list = ["b","e","r","n","a","t"]

random.shuffle(pass_list)
print(pass_list)
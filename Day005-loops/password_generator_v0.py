import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

ascii_table = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
password = ""
if nr_letters >= 0 and nr_numbers >= 0 and nr_symbols >= 0:
    total_char = nr_letters + nr_numbers + nr_symbols
    chars_by_type = [nr_letters, nr_numbers, nr_symbols]
    for char in range(1, total_char +1):
        char_type = random.randint(0,2)
        if chars_by_type[char_type] > 0:
            password += ascii_table[char_type][random.randint(0, len(ascii_table[char_type]) - 1)]
            chars_by_type[char_type] -= 1
        else:
            forward_or_backward = random.randint(0,1)
            if forward_or_backward == 0:
                char_type -= 1
            else:
                char_type += 1
            if char_type > 2:
                char_type = 0
            if chars_by_type[char_type] > 0:
                password += ascii_table[char_type][random.randint(0, len(ascii_table[char_type]) - 1)]
                chars_by_type[char_type] -= 1
            else:
                char_type += 1
                if char_type == 3:
                    char_type = 0
                if chars_by_type[char_type] > 0:
                    password += ascii_table[char_type][random.randint(0, len(ascii_table[char_type]) - 1)]
                else:
                    char_type += 1
                    if char_type == 3:
                        char_type = 0
                    if chars_by_type[char_type] > 0:
                        password += ascii_table[char_type][random.randint(0, len(ascii_table[char_type]) - 1)]
                    else:
                        char_type += 1
                        if char_type == 3:
                            char_type = 0
                        if chars_by_type[char_type] > 0:
                            password += ascii_table[char_type][random.randint(0, len(ascii_table[char_type]) - 1)]
                                        
    print(f"Here is your password: {password}")
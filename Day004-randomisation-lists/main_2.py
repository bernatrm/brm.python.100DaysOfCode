# Lists
fruits = ["Cherry", "Apple", "Pear"]

states_of_america =["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
                    "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", 
                    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
                    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
                    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", 
                    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
                    "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[-1])
# states_of_america[1] = "Pencilvania"
# print(states_of_america[1])
# states_of_america.append("Puerto Rico")
# print(states_of_america[-1])

# states_of_america.extend(["State_A", "State_B"])
# print(states_of_america[-1])

# num_of_states = len(states_of_america)

# print(num_of_states)

# print(states_of_america[49])

# print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", 
#             "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(dirty_dozen[0][-1])

position = "B3"
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

print(f"The indexes are letter_index = {letter_index}, number_index = {number_index}")

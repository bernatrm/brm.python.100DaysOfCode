# Rock Paper Scissors ASCII Art

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

arts = [rock, paper, scissors]

# 0 - Rock
# 1 - Paper
# 2 - Scissors
#   0 1 2 <-- human
# 0 x H C
# 1 C x H
# 2 H C x
# ^
# Computer 
result1 = ["t","h","c"]
result2 = ["c","t","h"]
result3 = ["h","c","t"]
results = [result1, result2, result3]
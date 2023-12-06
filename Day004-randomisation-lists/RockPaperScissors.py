import random
import rock_paper_scissors_helper as rps_hlp

human_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if human_choose < 0 or human_choose > 2:
    print("You typed an invalid number, you lose!")
else:
    print(f"You choose : \n{rps_hlp.arts[human_choose]}")

    computer_choose = random.randint(0,2)
    print(f"Computer choose : \n{rps_hlp.arts[computer_choose]}")


    result = rps_hlp.results[computer_choose][human_choose]
    if result == "t":
        print("It's a draw, try again")
    elif result == "h":
        print("You win")
    else:
        print("You lose")

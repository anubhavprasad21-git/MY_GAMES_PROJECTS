import random
def rps_game(inp):
    d1={1:"Rock",2:"Paper",3:"Scissor"}
    user_choice=inp
    computer_choice=random.randint(1,3)
    if user_choice==1 and computer_choice==2:
        print(f"Computer Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==2 and computer_choice==1:
        print(f"You Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==3 and computer_choice==1:
        print(f"Computer Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==1 and computer_choice==3:
        print(f"You Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==2 and computer_choice==2:
        print("Its a Draw\nComputer and You Both Choose Paper")
    elif user_choice==3 and computer_choice==2:
        print(f"You Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==1 and computer_choice==1:
        print("Its A Draw\nComputer and You Both Choose Rock")
    elif user_choice==2 and computer_choice==3:
        print(f"Computer Won\nComputer={d1.get(computer_choice)}\nUser={d1.get(user_choice)}")
    elif user_choice==3 and computer_choice==3:
        print("Its A Draw\nComputer and You Both Choose Scissor")


choose=int(input("enter number([1 for Rock] [2 for Paper] [3 for scissor]):"))
rps_game(choose)

import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == "Snake":
        if you == "Water":
            return False
        elif you =="Gun":
            return True
    elif comp == "Water":
        if you == "Gun":
            return False
        elif you =="Snake":
            return True
    elif comp == "Gun":
        if you == "Snake":
            return False
        elif you =="Water":
            return True
    
    
randno = random.randint(1, 3)
print(randno)
if randno == 1:
    comp = "Snake"
elif randno == 2:
    comp = "Water"
else:
    comp = "Gun"

print("Computer's turn:- Computer chose")
you = input("Your turn:- Snake, Water or Gun?(Type any one of them)")  
a = game(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a != "Snake":
    print("Enter a valid option and try again!")
elif a != "Water":
    print("Enter a valid option and try again!")
elif a != "Gun":
    print("Enter a valid option and try again!") 
elif a == None:
    print("The game is a tie!")
elif a:
    print("You won!")   
else:
    print("you lost lmao nubre")

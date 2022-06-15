print("welcome to my quiz game")

playing = input("Do you want to start the car quiz? ")

if playing != "yes":
    quit()

print("Okay let's start :")

answer = input("What does BOV stand for? ")
if answer == "blow off valve":
    print("Correct!")

answer = input("What does ABS stand for? ")
if answer == "anti lock braking system":
    print("Correct!")

answer = input("What does JDM stand for? ")
if answer == "japanese domestic market":
    print("Correct!")

answer = input("What does AWD stand for? ")
if answer == "all wheel drive":
    print("Correct!")

answer = input("What does AC stand for? ")
if answer == "air conditioning":
    print("Correct!")
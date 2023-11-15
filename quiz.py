print("Welcome to my quiz!")

playing=input("Do you want to play? ")


if playing !="yes":
    quit()

print("Okay!! Let's play.")
score=0

answer=input("What does OS stand for? ")
if answer=="Operating System":
    print("Correct!!")
    score=score+1
else:
    print("Incorrect!!")

answer=input("What does PC stand for? ")
if answer=="Personal Computer":
    print("Correct!!")
    score=score+1
else:
    print("Incorrect!!")

answer=input("What does CPU stand for? ")
if answer=="Central Processing Unit":
    print("Correct!!")
    score=score+2
else:
    print("Incorrect!!")

answer=input("What does RAM stand for? ")
if answer=="Random Access Memory":
    print("Correct!!")
    score=score+1
else:
    print("Incorrect!!")

print("You have answered " + str(score) + " questions correctly")

print("You have scored " + str((score/4) *100)  + "%." )


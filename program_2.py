import random

def mathProblems():
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    print(" ",num1)
    print("+",num2)
    print("-----")
    answer = int(input("Enter your answer: "))
    if answer == (num1+num2):
        print("Congratulations!")
    else:
        print("The correct answer was", num1+num2)
mathProblems()

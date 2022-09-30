import random

def get_score():
    score = float(input("Enter score: "))
    return score
def main():
    score = get_score()
    if score > 100:
        print("Your Score is Invalid")
    elif score >= 90:
        print("Your Score is Excellent")
    elif score >= 50:
        print("Your Score is Passable")
    elif score < 0:
        print("Your Score is Invalid")
    else:
        print("Your Score is Bad")
    score = random.randint(1,100)
    print("Random Score is : ", score)
    if score > 100:
        print("Your Score is Invalid")
    elif score >= 90:
        print("Your Score is Excellent")
    elif score >= 50:
        print("Your Score is Passable")
    elif score < 0:
        print("Your Score is Invalid")
    else:
        print("Your Score is Bad")


main()
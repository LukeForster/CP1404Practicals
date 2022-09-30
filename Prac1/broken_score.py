score = float(input("Enter score: "))

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
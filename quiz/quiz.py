import random
from Question import AddQuestion, SubtractQuestion, MultiplyQuestion

questioncount = 10
questionNum = 0
input("Enter name > ")

types = [
    "AddQuestion",
    "SubtractQuestion",
    "MultiplyQuestion"
]

score = 0

while questionNum < questioncount:
    questionNum += 1
    type = random.choice(types)

    question = eval(type)(questionNum)

    correct, correctanswer = question.ask()

    if correct:
        score += 1
        print ("\033[92m ✔ Correct answer!\033[0m")
    else:
        print ("\033[91m ✗ Incorrect answer! The correct answer was", correctanswer ,".\033[0m")

finalScoreString = "| Final score: " + str(score) + "/" + str(questioncount) + " |"
print("-" * len(finalScoreString))
print(finalScoreString)
print("-" * len(finalScoreString))

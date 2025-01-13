import marks                # include the marks.py
import quiz as qz           # include the quiz.py file as qz
import difficulty as df     # include the difficulty.py file as df

print('Difficulty Levels: \n1. Easy\n2. Medium\n3. Hard\n')
level = int(input("Enter the number against difficulty level: "))

test_num_range = df.difficulty_level(level)

number_of_questions = int(input("Enter number of questions: "))
ans, true_ans = qz.quiz_questions(number_of_questions, test_num_range)
score = marks.scored(ans, true_ans)
percentage = marks.percentage_scored(score, number_of_questions)
print("You scored {} marks out of {} with percentage {}%".format(score, number_of_questions, percentage))
if percentage >= 80:
    print("Congratulations!!! You Aced your quiz!!!")
elif percentage >= 50:
    print('Congratulations!!! You passed your quiz!!!')
else:
    print("Alas!!! You couldn't get lucky this time. You should give it another go.")

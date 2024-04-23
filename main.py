# This has been a student project: credit goes to my teacher Dr. Angela Udemy.com

from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

# start with empty library
question_bank = []
for question in question_data:
    # for each question loop through thr question_data module and define two new variables and make a question
    question_text = question["question"]
    # this becomes the variable of the question
    question_answer = question["correct_answer"]
    # new variable of the answer
    new_question = Question(question_text, question_answer)
    # this variable uses class Question with the two previously defined variables
    question_bank.append(new_question)
#     The new questions are added to the empty list

quiz = Quizbrain(question_bank)
# In this object we use the Quizbrain class and the question_bank list as input


while quiz.still_have_questions():
    # While the quiz still has questions = True. There will be a new question.
    quiz.next_question()

# Upon completion of the game
print("You've completed the quiz. ")
print(f"Your final score is {quiz.score}/{quiz.question_number}")






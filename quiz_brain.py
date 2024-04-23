class Quizbrain:
    """Class questions operations, uses list as input"""
    def __init__(self, q_list):
        """Uses a list as input for te Quizbrain class"""
        # These are attributes of that list with question number and score having fixed starting variables
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    """Methods"""
    def still_have_questions(self):
        """Asks if current question number is smaller than total number of questions and return True"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Check if there will be a next question or not"""
        current_question = self.question_list[self.question_number]
        # check if the current question is equal to the question in the list
        self.question_number += 1
        # add 1 to the question number because default start with 0
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Check if answer is correct with correct answer from librairy if yes add 1 score"""
        if user_answer.lower() == correct_answer.lower():
            # check if answer is the same as the correct answer and make it lowercase just in case
            self.score += 1
            print("You've got it right!")
        else:
            print("You've got it wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")






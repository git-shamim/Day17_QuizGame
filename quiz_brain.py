
class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.user_score = 0
        self.question_bank = question_bank

    def continue_play(self):
        return self.question_number < len(self.question_bank)

    def ask_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input("Q{0}: {1}. ('True' or 'False')? \n : ".format(self.question_number,
                                                                           current_question.question))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("You got it right!")
            print("You score is {}/{}".format(self.user_score, self.question_number))
            print('\n')
        else:
            print("That's wrong")
            print("You score is {}/{}".format(self.user_score, self.question_number))
            print('\n')

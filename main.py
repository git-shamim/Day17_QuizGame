
from quiz_model import Question
from quiz_data import data
from quiz_brain import QuizBrain

question_bank = []
for ques_ans in data:
    question = ques_ans["question"]
    correct_answer = ques_ans["correct_answer"]
    line_item = Question(question, correct_answer)
    question_bank.append(line_item)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.continue_play():
    quiz_brain.ask_question()

print("You have completed the Quiz")
print("Your final score is : {}/{}".format(quiz_brain.user_score, quiz_brain.question_number))

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

data_dict=[]

for question in question_data:
    data_dict.append(Question(text=question["question"],answer=question["correct_answer"]))

quizBrain = QuizBrain(data_dict)


print(quizBrain.questions_list)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've  completed the quiz")
print(f"Your final score was {quizBrain.score}/{quizBrain.question_number}")


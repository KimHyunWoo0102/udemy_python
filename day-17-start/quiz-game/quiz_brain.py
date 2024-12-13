# TODO : asking the questions
# TODO : checkingi if the answer was correct
# TODO : checking if we're the end of the quiz



class QuizBrain:
    def __init__(self,questions):
        self.question_number=0
        self.score=0
        self.questions_list=list(questions)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number} : {question.text} (True/False)? : ")


        self.check_answer(user_input=user_answer,correct_answer=question.answer)

    def still_has_questions(self):
        return self.question_number<len(self.questions_list)

    def check_answer(self,user_input,correct_answer):
        if correct_answer.lower()==user_input.lower():
            self.score+=1
            print(f'You got it right!')
        else:
            print("That's wrong")

        print(f"The correct answer if {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()


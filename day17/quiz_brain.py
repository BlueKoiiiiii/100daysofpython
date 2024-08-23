class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text}(True/False)").lower()
        self.check_answer(answer)


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Your score is {self.score}/{self.question_number+1}")
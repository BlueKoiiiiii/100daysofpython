from question_model import question
from data import question_data
from quiz_brain import QuizBrain

questionbank = []
for questions in question_data:
    q1 = question(questions["text"], questions["answer"])
    questionbank.append(q1)

quiz = QuizBrain(questionbank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.question_number += 1
print(f"You've completed the quiz \nYour final score was {quiz.score}/{len(quiz.question_list)}")
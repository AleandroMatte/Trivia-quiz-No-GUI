from question_model import Question
from data import question_data
from quiz_brain import backend


list_questions=[]
for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question(q_text=question_text,q_answer=question_answer)
    list_questions.append(new_question)

quiz=backend(list_questions)
quiz.nextquestion()
while quiz.still_has_questions():
    quiz.nextquestion()
print("contratulation, you completed the quiz")
print(f"your pontuation was {quiz.score} out of {len(quiz.question_list)}")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    


]
category_list=''
for i in question_data:
    if i['category'] not in category_list:
        category_list+=i['category']+' '


category = input(f'what category {category_list}: ').title()
for i in question_data:
    if category in i['category']:
        question_text = i['question']
        question_answer = i['correct_answer']
        
        new_question = Question(question_text,question_answer)
        question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f'final score: {quiz.score}')

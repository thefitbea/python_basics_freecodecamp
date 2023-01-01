
#wrote all prompts and choices in an array
question_promts=["What color are apples?\n(a)Red/Green\n(b)Purple\n(c)White\n\n",
                 "What color are bananas?\n(a)Red\n(b)Purple\n(c)Yellow\n\n",
                 "What color are blueberries?\n(a)Green\n(b)Blue\n(c)White\n\n"]

from question import Question# file question.py

#array with questions and their respective correct ans, passed onto run rest fn while calling
questions = [Question(question_promts[0], "a"),
             Question(question_promts[1], "c"),
             Question(question_promts[2], "b")]
#we can add more questions and it will ask..

#question objs in array, is passed as parameter to fn
def run_test(x):#x is parameter,it can be whtever name
    score=0
    for question in x:# for each ..in ..loop
        user_answer=input(question.prompt)
        if user_answer==question.answer:
            score+=1
            print("You got\t"+str(score)+"/"+str(len(questions))+"\tcorrect")


run_test(questions)
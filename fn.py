#fn is colection of code which performs a specific set of tasks
#allows to organize code, break into small chunks, reusable

def say_hi(fname,lname, age):
    print("Hi "+fname+" "+lname+"you are "+str(age))
    #code inside fn should be indented, here IDE does it for u


say_hi("Hari","Krishnan",24)

say_hi("Viktor","Drago",30)
#python fn is collection of python code that performs a specific task, when u need info back from fn, return keyword is used


#cube number demo for return stmt

output=0
result=0

def cube(num):
    result= num*num*num
    return result
    #code after return no use as it breaks u back out of fn


output=cube(3)
print(output)
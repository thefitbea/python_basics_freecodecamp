#phone, pc, person...in real life, we need custom datatypes....class for it
#with a class u can define a custome datatype

#student class

class Student:

    #inorder to map out what a student is and should be we write a initialize fn
    def __init__(self,id,name,major,gpa,is_on_probation):#typo error caused havoc, init was written int...lol
        self.id =id# id is the attribute of objt, passed value is assigned to it
        self.name =name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation





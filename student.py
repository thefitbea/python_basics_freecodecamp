#class is template for what a student is. we create an actual student, ie object
#class is overview of what a student datatype is
#object is acrtual student, just not a template anymore, instance of class

from class_objects import Student

student1=Student(1,"Future Hari","Data Science",3.1,False)
student2=Student(4,"Past Hari","Computer Science",2.3,True)

print(student1)
print(student1.id,student1.name)

print(student2.id,student2.name)

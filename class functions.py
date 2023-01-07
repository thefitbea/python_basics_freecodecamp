# object function
#class fn is a fn that we use inside a class, modify the objts or give specific info about objts
#fn that can be used by objects of the class, giving info about objects or modify values in objects
from graduate import Graduate

graduate1 = Graduate("Hari","Data Science", 3.5)
graduate2 = Graduate("Viktor","UX", 3.1)

print(graduate2.on_honor_roll())
from chef import Chef

class JapaneseChef(Chef):
    #import class to be inherited, then pass the parent clas as parameter to the child class
    #TaDa, u get inheritance

    #overideing lemon juice by apple juice
    def make_juice(self):
        print("Apple juice is ready")

    def make_special_dish(self):
        print("Sushi is ready")
    #either copy paste of regular chef or juat inherit Man
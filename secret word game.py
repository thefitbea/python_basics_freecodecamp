# user interacts to find secret word
#my logic
secret_word="vodka"
chance=3
guess=""

while guess !=secret_word and chance>0:
    guess=input("Enter your guess:")
    chance=chance-1
    print("U have " +str(chance)+" chance")


if chance==0:
    print("U lost")
else:
    print("u win")
#conditional stmts

#if, if else, if elseif else

is_male=True
is_tall=False


if is_male or is_tall: #/ i.e one of the condition is true
    print("You are a male or tall or both- OR")
else:
    print("You are neither male nor tall- OR")



if is_male and is_tall: #& i.e both of the conditions are true
    print("You are a tall male- AND")
else:
    print("You are either not male or not tall- AND")



if is_male and is_tall: #& i.e both of the conditions are true
    print("You are a tall male- AND_NOt")
elif is_male and not(is_tall):
    print("You are a short male- AND_NOt")
elif not(is_male) and is_tall:
    print("You are a short male- AND_NOt")
else:
    print("You are not male and not tall- AND")
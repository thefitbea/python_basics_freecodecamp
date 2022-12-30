def big_num(num1,num2,num3):
    if num1>=num2 and num1>=num3: #comparisson operator gives boolean values hence the logic
        return num1
    elif num2>= num1 and num2>=num3:
        return num2
    else:
        return num3



print(big_num(12,100,4))
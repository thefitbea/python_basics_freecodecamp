# try except block
try:
    value= 10/0
    num = int(input("Enter a no.:"))
    print(num)
#will except all errors unless specified
except ZeroDivisionError:
    print("Divided by zero")

#except ZeroDivisionError as err:
#    print(err)

except ValueError:
    print("Invalid Input")
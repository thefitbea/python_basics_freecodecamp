#just another python file that we import into this py file, allows us to access all fns and varaibles and stuff in this
#cool, like an extension

import fn

print(fn.output)

#import wikipedia
#result = wikipedia.page("GeeksforGeeks")
#print(result.summary)

import calendar#https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatmonth


print(calendar.prmonth(1998,3))

# This will import
# dis module
import dis


def test_fn(number):
	return (str(number)+str(number))

def newFunc(string):
	print("Hello", string)


print(test_fn(input("Enter a number:")),newFunc("Hari"))


# This will display the
# disassembly of test():
dis.dis(test_fn(10))

# This will display the
# disassembly of newFunc()
dis.dis(newFunc)

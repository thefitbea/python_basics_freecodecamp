i= 0
friends=["jym","sam", "anne"]
for letter in "hi World":
    print(letter)

print("\n")

for any_name_variable in friends:
    print(any_name_variable)

print("\n")

for index in range(4,10):
    print(index)

print("\n")

for index in range(len(friends)):#index 0 til length of friends array, not lincluding the last
    print(friends[index])

print("\n")

for index in range(5):
    if index==0:
        print("First iteration")
    else:
        print("Other than first oiteration")
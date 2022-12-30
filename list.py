#List: A list in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values, etc. It is an ordered collection supporting negative indexing. A list can be created using [] containing data values.
#Contents of lists can be easily merged and copied using python’s inbuilt functions.

#Array: An array is a vector containing homogeneous elements i.e. belonging to the same data type. Elements are allocated with contiguous memory locations allowing easy modification, that is, addition, deletion, accessing of elements. In Python, we have to use the array module to declare arrays. If the elements of an array belong to different data types, an exception “Incompatible data types” is thrown.

friends=["Rohith", "Sam","Shampoo", "Abhijith", "Rahul"]
            #0      #1      #2        #3         #4
            #-5    #-4      #-3       #-2        #-1
friends[4]="Aswin"
print(friends[4])

print(friends[0])
print(friends[-5])
print(friends[1:3])#upto but not includeing index 3
lucky_number=[4,5,8,1,9]

#list functions
#display
print(lucky_number)
friends.append("Krish")#adds to end of list
print(friends)
friends.insert(1,"Viktor")#adds in middle
print(friends)
print(friends.index("Viktor"))#if Viktor is there return index, aka position, else throws error stating not in list
#case sensitive
print(friends.count("Viktor"))
#backup copy
friends_copy= friends.copy()
print(friends_copy)
friends.remove("Krish")
print(friends)
friends.pop()#removes last element from list ie. Aswin
print(friends)
friends.clear()#reset list, empty
print(friends)

print(lucky_number)
lucky_number.sort()#sorts in asc order, works with string and numbers
print(lucky_number)
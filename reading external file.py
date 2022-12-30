
#r is read, w is write, a is append(cant modify but add to end, r+ is read and write
file=open("external_text_file.txt", "r")#same root folder so no locaton required

print(file.readable())# checking if file can be read
#print(file.readline())
#print(file.readline())

#print(file.readlines())# puts into list
#print(file.readlines()[1])#doubt with error in index
for line in file.readlines():
    print(line)

file.close()

#print(file)
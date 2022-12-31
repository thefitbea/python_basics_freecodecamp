
#r is read, w is write, a is append(cant modify but add to end, r+ is read and write
file=open("external_text_file.txt", "r")#same root folder so no locaton required

print(file.readable())# checking if file can be read
#print(file.readline())
#print(file.readline())

#print(file.readlines())# puts into list
#print(file.readlines()[0])#doubt with error in index, fixed by Vinu Cutan
#after first readline pointer reading list is set to last element and list is empty so throws error

for line in file.readlines():
    print(line)

file.close()

#print(file)

file=open("external_text_file.txt", "a")

file.write("\nAppENDed text line")

file.close()

file=open("external_text_file_copy.txt","r+")#creates a new line re writes all content
file.write("\n \n hahahaha Happy new gear, it ain't a typo")
for text in file.readlines():
    print(text)
file.close()

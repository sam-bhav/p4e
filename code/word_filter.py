fname = input("Enter file name: ")
filehandle = open(fname)
word_list = list()
for line in filehandle:
    words=line.rstrip()
    
    for selected_word in words:
        if selected_word != line:
            word_list.append(selected_word)

    
    
    

print(word_list.sort())

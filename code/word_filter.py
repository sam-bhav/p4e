fname = input("Enter file name: ")
file_handle = open(fname)
word_list = list()
for line in file_handle:
    words=line.split()
    
    for selected_word in words:
        if selected_word not in word_list:
            word_list.append(selected_word)

word_list.sort()
print(word_list)

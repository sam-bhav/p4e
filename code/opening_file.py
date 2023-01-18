#print each line
fhandle=open('mbox.txt')
for eachline in fhandle:
    print(eachline)

#count no of lines

fhand=open('mbox.txt')
count = 0

for line in fhand:
    count = count + 1
print('Lines : ', count)

#reading a file as a series of characters 
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#searching through a file
#this always prints a new line automatically

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

#fix using the code below
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#select all lines that contains @uct.ac.za
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)


#prompt for a file name
fname = input('Enter name of the file: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From:'):
        print(line)


#user can type bad file name, always use exception handling in such cases

fname = input('Enter name of the file: ')

try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

for line in fhand:
    if line.startswith('Subject:'):
        count+=1
print('There were', count,'subject lines in',fname)



#define a dictionary : dictionary_name = dict()
#dictionary_name['label']=value
#print(dictionary_name['label'])
#can make a dictionary using curly braces only
    #jjj={'chuck':1,'fred':42}
    #ooo={}

#can count frequency in dictionary


# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the
#  sender's mail address to a count of the number of times they appear in the file. 
#  After the dictionary is produced, the program reads through the dictionary using
#   a maximum loop to find the most prolific committer.

file_name=input("Enter file name:")
if len(file_name)<1:
    file_name="mbox-short.txt"

file_handle=open(file_name)
email_sender = dict()
count=0

for each_line in file_handle:
    if not each_line.startswith('From'):
        continue
    else:
        words=each_line.split()
        if len(words)>2: 
            sender_name=words[1]
            if (sender_name not in email_sender):
                email_sender[sender_name]=1
            else:
                email_sender[sender_name] +=1    
            
most_emails=max(email_sender,key=email_sender.get)
x=email_sender.get(most_emails)
print(most_emails,x)
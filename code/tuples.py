fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

file_handle = open(fname)
counts = dict()

for each_line in file_handle:
    if not each_line.startswith("From "):
        continue
    else:
        pos_time = each_line.find(':')
        words=each_line.split()
        time=words[5]
        hours=time[:2]
        counts[hours]=counts.get(hours,0) + 1
for key,val in sorted(counts.items()):
    print(key,val)
        

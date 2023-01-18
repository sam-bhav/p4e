
largest = 0
smallest = 0
num_arr=[]
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum=int(num)
        num_arr.append(fnum)
        
    except:
        print("Invalid Input")
        continue
        
for i in num_arr:
   if (i>largest):
        largest=i
num_arr.sort()
smallest=num_arr[0]
        
print("Maximum", largest)
print("Minimum", smallest)
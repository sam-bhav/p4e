x=int(input("Enter a number "))
if(x<100):
    while (x//10) !=0:
        af_d = x%10
        bf_d=x//10
        x = bf_d * af_d
        
print(x)
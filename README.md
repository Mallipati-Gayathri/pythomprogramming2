# pythomprogramming2
a,b=map(int,input().split())
if(b==a+1 or b==a-1):
    print("Yes")          #if numbers are consecutive
elif(a==1 and b==10 or a==10 and b==1):
    print("Yes")          #consecutive numbers are 1 and 10 
else:
    print("No")           #if numbers are not consecutive
    

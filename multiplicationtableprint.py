n=int(input("enter a number:"))
s=int(input("enter a starting value:"))
e=int(input("enter a ending value:"))
for i in range(s,e):
   if i%n==0:
    print(i)
    s+=1

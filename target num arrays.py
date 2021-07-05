nums=list(map(int,input().split()))
index=list(map(int,input().split()))
t=[]
for i in range(0,len(index)):
        t.insert(index[i],nums[i])
print(t)

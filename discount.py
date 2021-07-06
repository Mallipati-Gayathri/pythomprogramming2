price=list(map(int,input().split()))
discountprice=[]
for i in range(len(price)):
        for j in range(i+1,len(price)):
                if price[i]>=price[j]:
                        discountprice.append(price[i]-price[j])
                        break
        else:
                discountprice.append(price[i])
print(discountprice)                       
                        

lst = [1,2,3,8]
esum,osum=0,0
i=0
while(i<len(lst)):
    if(lst[i]%2 == 0):
        esum+=lst[i]

    else:
        osum+=lst[i]

    i+=1
    

    

print("Odd sum",osum,"Even sum", esum)
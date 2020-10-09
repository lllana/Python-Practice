def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        try:
            a, b = ar[i], ar[i+1]
        except IndexError:
            return count
        
        if abs(a-b) == 1: 
            count +=1
        
    return count

print(pairs([1,2,5,8,-4,-3,7,6,5]),3)




def pairs(arr):
    return sum( abs(a-b)==1 for a,b in zip(arr[::2],arr[1::2]) )

print(pairs([1,2,5,8,-4,-3,7,6,5]),3)




def pairs(ar):
    res=0
    for i in range(1,len(ar),2):
        if abs(ar[i]-ar[i-1])==1:
            res+=1
    return res

print(pairs([1,2,5,8,-4,-3,7,6,5]),3)
        



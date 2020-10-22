def parts_sums(ls):
    
    prime_list = ls
    result = [sum(ls)]
    
    if not prime_list:
           return result
        
    else:   
        for i in range(len(prime_list)-1):
            prime_list.pop(0)
            result.append(sum(prime_list)) 
                         
        result.append(0)
                      
    return result

print(parts_sums([1, 2, 3, 4, 5, 6]))
print(parts_sums([10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]))
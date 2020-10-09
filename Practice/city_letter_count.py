#You receive the name of a city as a string, and you need to return a string that shows 
# how many times each letter shows up in the string by using an asterisk (*).
#"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"

# 1 option 
def get_strings(city):
    
    city = city.replace(' ','').lower()
    city_string = ''
    
    for i in city:
        if i in city_string:
            pass
        else:
            city_string += i +':'+ ('*'* city.count(i))+','
        
    return result[:-1]  


print(get_strings('Los Angeles'))

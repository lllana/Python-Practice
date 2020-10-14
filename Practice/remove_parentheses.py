def remove_parentheses(s):
    deep = 0
    result = ''
    
    for char in s:
        if char == '(':
            deep += 1
            
        elif char == ')':
            deep -= 1
        
        elif deep == 0: 
            result += char
            
    return result

print(remove_parentheses("a(b(c))") == "a")
print(remove_parentheses("hello example (words(more words) here) something") == "hello example  something")
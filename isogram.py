def is_isogram(string):
    duplicates = {}
    string = string.lower()
    for char in string:
        if char in duplicates:
                return False
        else:
            duplicates[char] = 1
    
    return True
    
def main(words):
    for word in words:
        result = is_isogram(word)
        print(word, result)

main(["Tim","party","pooper"])        
 
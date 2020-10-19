#1 option

def like_v1(names):
    names_len = len(names)
    
    if names_len == 0:
        result = 'no one likes this'
    elif names_len == 1:
        result = '{} likes this'.format(names[0])
    elif names_len == 2:
        result = '{} and {} like this'.format(names[0], names[1])
    elif names_len == 3:
        result ='{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif names_len > 3:
        count = names_len - 2
        result ='{}, {} and {} others like this'.format(names[0], names[1], count)
    return result

print(like_v1(['Max', 'John', 'Mark']))

#2 option
def like_v2(names):
    names_len = len(names)

    cases = {
        0: lambda: 'no one likes this',
        1: lambda: '{} likes this'.format(names[0]),
        2: lambda: '{} and {} like this'.format(names[0], names[1]),
        3: lambda: '{}, {} and {} like this'.format(names[0], names[1], names[2]),
    }
    return cases.get(names_len, lambda: '{}, {} and {} others like this'.format(names[0], names[1], names_len - 2))()
    
print(like_v2(['Max', 'John', 'Mark']))
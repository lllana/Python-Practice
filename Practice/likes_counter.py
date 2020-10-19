#1 option

def likes(names):
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


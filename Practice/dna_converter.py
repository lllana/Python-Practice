def DNA_strand(dna):
    
    result = ''
    for i in dna:
        if i == 'A':
            result +='T'
        elif i == 'T':
            result += 'A'
        elif i == 'C':
            result += 'G'
        elif i == 'G':
            result += 'C'
            
    return result

print(DNA_strand('GTAG'))
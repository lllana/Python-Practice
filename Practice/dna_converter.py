#First attempt 
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


def DNA_strand(dna):

    dict = {'A': 'T', 'T':'A', 'G':'C', 'C':'G'}    
    result = '' 
    
    for i in dna:
        result += dict[i]
        
    return result

print(DNA_strand('GTAG'))


def DNA_strand(dna):

    dict = {'A': 'T', 'T':'A', 'G':'C', 'C':'G'}    
        
    return ''.join([dict[i] for i in dna])

print(DNA_strand('GTAG'))    
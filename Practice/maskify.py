# Your task is to write a function maskify, which changes all but the last four characters into '#'.

#1option
def maskify(cc):

    maskify = ''
    for i in cc[:-4]:
        i = '#'
        maskify += i
        
    return maskify + cc[-4:]

print(maskify('636363636636636666'))


#2option
def maskify(cc):
    return ''.join([i.replace(i,'#') for i in cc[:-4]]) + cc[-4:]

print(maskify('636363636636636666'))


#3option
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

print(maskify('636363636636636666'))
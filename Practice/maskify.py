# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):

    maskify = ''
    for i in cc[:-4]:
        i = '#'
        maskify += i
        
    return maskify + cc[-4:]

print(maskify('636363636636636666'))
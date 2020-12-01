category = df['purpose'].apply(english_stemmer.stem)

def purpose_category(purpose):
    for word in purpose:
        if 'car' in word:
            result = 'car'
            break
        elif 'hous' in word or 'est' in word or 'properti' in word:
            result = 'housing'
            break
        elif 'educ' in word or 'uni' in word:
            result = 'education'
            break
        else:
            result = 'wedding'
    return result
    
category.apply(purpose_category).value_counts()
            
print(df['category'].value_counts())
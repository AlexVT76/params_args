def single_root_words(root_word,*other_words):
    def unpacking(other_words):
        return [*other_words]
    same_words = []
    for word in other_words:
        if root_word.upper() in word.upper() :
           same_words.append(word)
        if word.upper() in root_word.upper() :
                same_words.append(word)
    return same_words


result1=single_root_words('age','age_related','Kazan','AGEISM')
result2=single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

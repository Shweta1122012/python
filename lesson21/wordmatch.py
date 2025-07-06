def match_word(words):
    ctr =0
    lst =[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            lst.append(word)
            ctr+=1
    print("list of of words that have the same start and end letter",lst)
    return ctr
count = match_word(['abc','xyx','aba','123'])
print("number of words that have the same first annd last leter are",count)

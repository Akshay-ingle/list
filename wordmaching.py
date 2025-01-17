def math_words(words):
    ctr=0
    list1=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list1.append(word)
    print(list1)
    return ctr 
list=math_words(['abc','cfc','aba','xyz','121'])    
print(list)         
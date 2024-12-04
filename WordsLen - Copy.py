def wordLen(words):
    wordleng = []
    for i, j in enumerate(words):
        wordleng.append(len(j))
    maxi = max(wordleng)
    mini = min(wordleng)
    long = words[wordleng.index(maxi)]
    short = words[wordleng.index(mini)]
    aveLen = sum(wordleng)/len(wordleng)
    result = (mini,maxi,aveLen,)
    print(short,long)
    return result


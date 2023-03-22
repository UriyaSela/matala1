##### B #####

def revword(word: str):
    word = word.lower()[::-1]
    return word




def countword():
    global key_word
    name = 'C:\\Users\\User\\Desktop\\New folder\\לימודים\\תעונ\\3_2\\DA&M\\matala1\\text.txt'
    handle = open(name)
    dic = dict()
    lst = []
    for line in handle:
        line_words = line.rstrip().split(" ")
        if len(line_words) == 1:
            key_word = line_words[0].lower().strip()
            dic[key_word] = 1
        else:
            for i in line_words:
                word = revword(i)
                lst.append(word)
                if word in lst:
                    dic[word] = dic.get(word, 0) + 1
    return print(dic[key_word])


countword()

import numpy as np

def likeness(w1, w2):
    result = 0.
    common = 0

    if w1[0] == w2[0]:
        result += 10
    if w1[-1] == w2[-1]:
        result += 10
    if len(w1) <= len(w2):
        result += len(w1)/len(w2)*30
    else:
        result += len(w2)/len(w1)*30

    result += len(set(w1)&set(w2))/len(set(w1+w2))*50

    return result

def find_word(message):
    temp = message
    for i in ',.!:?':
        temp = temp.replace(i, '')
    temp = temp.lower()
    wordlist = temp.split(' ')

    result = np.zeros((len(wordlist),len(wordlist)))
    
    for i in range(len(wordlist)-1):
        for j in range(i+1,len(wordlist)):
            result[(i,j)] = likeness(wordlist[i],wordlist[j])
    
    result = np.sum(result + result.T, axis=1)
    index = np.where(result == np.max(result))
    
    return wordlist[int(np.max(index))]
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    find_word("Friend Fred and friend Ted.")
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"

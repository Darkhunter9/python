def checkio(text, word):
    matrix = ["" for i in range(text.count("\n")+1)]
    j = 0
    for i in text:
        if i != " ":
            if i == "\n":
                j += 1
            else:
                matrix[j] += i.lower()
    word2 = word.lower()

    for i in range(len(matrix)):
        if word2 in matrix[i]:
            result0 = i+1
            result1 = matrix[i].find(word2)+1
            result3 = matrix[i].find(word2)+len(word2)
            return [result0,result1,result0,result3]

    matrix2 = []
    for i in range(max(len(matrix[i]) for i in range(len(matrix)))):
        temp = ""
        for j in range(len(matrix)):
            try:
                temp += matrix[j][i]
            except Exception:
                temp += " "
        matrix2.append(temp)
    for i in range(len(matrix2)):
        if word2 in matrix2[i]:
            result0 = matrix2[i].find(word2)+1
            result1 = i+1
            result2 = matrix2[i].find(word2)+len(word2)
            return [result0,result1,result2,result1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
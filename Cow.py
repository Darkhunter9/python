COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

'''
The cow is always the same, only quote changes.
Multiple spaces in a row are replaced by one space.
The top border consists of underscore characters. It starts from a single space and ends before the border column.
Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), space(1), quote border(1).
If line is less than 40 characters, it will fit into one string. The string is quoted in <>.
If the line is greater than or equal to 40 characters, it should be split by these rules:
Max line size is 39 chars. If any spaces are in the line, split it by the rightmost space (this space is removed from text) otherwise take the first 39 characters.
After the split align all lines to same length by adding spaces at the end of each line.
First line borders: /\
Middle line borders: ||
Last line borders: \/
The bottom border consists of the minus sign. Has same length as top.
cowsay console program has strange behavior in certain cases, this cases will not be tested here.
'''



def cowsay(text):
    result = ""
    temptext = text

    # remove multiple spaces
    i = 0
    while i < len(temptext)-1:
        if temptext[i] == " " and temptext[i+1] == " ":
            temptext = temptext[:i]+temptext[i+1:]
            i = 0
        else:
            i += 1

    # judge length 

    if len(temptext) < 40:
        temptext = "< "+temptext+" >\n"
        firstline = "\n "+"_"*(len(temptext)-3)+"\n"
        lastline = " "+"-"*(len(temptext)-3)
        return firstline+temptext+lastline+COW
    
    else:
        tempresult = []
        spacelist = []
        for i in range(len(temptext)):
            if temptext[i] == " ":
                spacelist.append(i)
        spacelist.append(len(temptext))
        
        pointer = -1
        while spacelist:
            if spacelist[0]-pointer > 40:
                tempresult.append(temptext[pointer+1:pointer+40])
                pointer += 39
            else:
                j = spacelist.pop(0)
                if spacelist:
                    if spacelist[0]-pointer > 40:
                        tempresult.append(temptext[pointer+1:j])
                        pointer = j      
                else:
                    tempresult.append(temptext[pointer+1:])

        length = max(len(tempresult[i]) for i in range(len(tempresult)))
        for i in range(len(tempresult)):
            tempresult[i] += " "*(length-len(tempresult[i]))
            if i == 0:
                tempresult[i] = "/ " +tempresult[i]+" \\"+"\n"
            elif i == len(tempresult)-1:
                tempresult[i] = "\ " +tempresult[i]+" /\n"
            else:
                tempresult[i] = "| " +tempresult[i]+" |\n"
            result += tempresult[i]

        firstline = "\n "+"_"*(length+2)+"\n"
        lastline = " "+"-"*(length+2)
        return firstline+result+lastline+COW

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
def yaml(a):
    l = a.split('\n')
    if ':' not in a:
        result = []

        for i in l:
            if not i:
                continue
            elif i == '-' or i == '- ':
                result.append(None)
            elif i[0] == '#':
                continue
            else:
                temp = ''
                comment = False
                quote = False
                for j in i[2:]:
                    if j == '"':
                        temp += '"'
                        quote = not quote
                    elif j == '#':
                        if quote:
                            temp += '#'
                        else:
                            break
                    else:
                        temp += j

                if temp[0] == ' ': temp = temp[1:] 
                if temp[-1] == ' ': temp = temp[:-1]
                if temp[0] == temp[-1] == '"': temp = temp[1:-1]
                try:
                    result.append(int(temp))
                except: 
                    result.append(temp)
    else:
        result = {}
        for i in l:
            if ':' in i:
                loc = i.find(':')
                attr = i[:loc]
                value = i[loc+2:]

                if value == '' or value == 'null':
                    value = None
                else:
                    while value[0] == ' ':
                        value = value[1:]
                    while value[-1] == ' ':
                        value = value[:-1]
                        
                    if value[0] == value[-1] == '"':
                        value = value[1:-1]
                        value = value.replace('\\','')
                
                if value == 'false':
                    value = False
                elif value == 'true':
                    value = True
                else:
                    try:
                        value = int(value)
                    except:
                        pass

                result[attr] = value
            
    return result


if __name__ == '__main__':
    yaml("name: Alex\nage: 12")
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]
    assert yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]
    assert yaml('- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5') == [1, 2, 3, 4, 5]
    assert yaml('-\n-\n-\n- 7') == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")

# Taken from mission YAML. Simple Dict

import re

def yaml(a):
    dic = {}
    data = a.split('\n')
    # print(data)

    for i in data:
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

            dic[attr] = value
    
    print(dic)
    return dic


if __name__ == '__main__':
    # print("Example:")
    # print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    # assert yaml('name: Alex Fox\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
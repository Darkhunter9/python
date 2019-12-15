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
            try:
                value = int(value)
            except:
                pass
            dic[attr] = value
    
    print(dic)
    return dic


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
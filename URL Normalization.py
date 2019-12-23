import re
alpha = ['%61', '%62', '%63', '%64', '%65', '%66', '%67', '%68', '%69', '%6A', '%6B', '%6C', '%6D', '%6E', '%6F', '%70', '%71', '%72', '%73', '%74', '%75', '%76', '%77', '%78', '%79', '%7A']
ALPHA = ['%41', '%42', '%43', '%44', '%45', '%46', '%47', '%48', '%49', '%4A', '%4B', '%4C', '%4D', '%4E', '%4F', '%50', '%51', '%52', '%53', '%54', '%55', '%56', '%57', '%58', '%59', '%5A']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def upper_repl(match):
    return match.group(0).upper()

def percent_encoded_digit(match):
    return match.group(0)[-1]

def checkio(url):
    url = url.lower()

    p1 = r'%[a-z0-9]{2}'
    url = re.sub(p1, upper_repl, url)

    url = url.replace('%2D','-')
    url = url.replace('%2E','.')
    url = url.replace('%5F','_')
    url = url.replace('%7E','~')
    p2 = r'%3[0-9]'
    url = re.sub(p2, percent_encoded_digit, url)
    for i in range(len(alpha)):
        url = url.replace(alpha[i], alphabet[i])
    for i in range(len(ALPHA)):
        url = url.replace(ALPHA[i],ALPHABET[i])

    url = url.lower()

    p1 = r'%[a-z0-9]{2}'
    url = re.sub(p1, upper_repl, url)
    
    p3 = r':80/'
    url = re.sub(p3, '/', url)
    p3 = r':80$'
    url = re.sub(p3, '', url)

    while '/./' in url:
        url = url.replace('/./', '/')
    p4 = r'/[a-z0-9%]+/\.\.'
    url = re.sub(p4, '', url)

    return url

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
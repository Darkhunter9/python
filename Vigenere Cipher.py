import re

def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    # A-Z -> 0-25
    # Ci = Ek(Mi) = (Mi + Ki) % 26
    result = ''
    keys = []

    for i in range(len(old_decrypted)):
        if old_decrypted[i] > old_encrypted[i]:
            key = 26 + ord(old_encrypted[i]) - ord(old_decrypted[i])
        else:
            key = ord(old_encrypted[i]) - ord(old_decrypted[i])
        keys.append(key)
        
        if ord(new_encrypted[i]) - 65 >= key:
            result += chr(ord(new_encrypted[i]) - key)
        else:
            result += chr(ord(new_encrypted[i]) + 26 - key)
        
        if i+1 == len(new_encrypted):
            return result
    
    if len(keys) < len(new_encrypted):
        for i in range(1,len(keys)+1):
            key = keys[:i]
            if all(keys[j] == keys[j%len(key)] for j in range(len(keys))):
                keys = key*(len(new_encrypted)//len(key)+1)
                break
    
    result = ''
    for i in range(len(new_encrypted)):
        key = keys[i]
        if ord(new_encrypted[i]) - 65 >= key:
            result += chr(ord(new_encrypted[i]) - key)
        else:
            result += chr(ord(new_encrypted[i]) + 26 - key)

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL")
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"

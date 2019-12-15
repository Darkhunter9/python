from copy import deepcopy

MONSTERS = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''

def count(word):
    d = {}
    for i in word:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    return d

c_list = []
w_list = MONSTERS.split('\n')[1:-1]
for i in w_list:
    c_list.append(count(i))

def judge(a,b):
    return all(j in a.keys() and b[j] <= a[j] for j in b.keys())

def halloween_monsters(spell: str)-> int:
    c0 = count(spell)
    candidates = []
    for i in c_list:
        if judge(c0,i):
            candidates.append(i)
    
    def max_word(c0):
        result = [0]
        for i in range(len(candidates)):
            if judge(c0,candidates[i]):
                c0_2 = deepcopy(c0)
                for j in candidates[i].keys():
                    c0_2[j] -= candidates[i][j]
                result.append(1+max_word(c0_2))
        return max(result)

    return max_word(c0)

if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    print("Your spell seem to be okay. It's time to check.")
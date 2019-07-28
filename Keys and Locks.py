import numpy as np

def keys_and_locks(lock, some_key):
    lock_list = lock.split('\n')
    key_list = some_key.split('\n')
    while '' in lock_list:
        lock_list.remove('')
    while '' in key_list:
        key_list.remove('')

    lock_array = np.zeros((len(lock_list),len(lock_list[0])),dtype=int)
    key_array = np.zeros((len(key_list),len(key_list[0])),dtype=int)

    for i in range(len(lock_list)):
        for j in range(len(lock_list[0])):
            if lock_list[i][j] == '#':
                lock_array[(i,j)] = 1
    
    for i in range(len(key_list)):
        for j in range(len(key_list[0])):
            if key_list[i][j] == '#':
                key_array[(i,j)] = 1
    
    while not np.count_nonzero(lock_array[0]):
        lock_array = lock_array[1:]
    while not np.count_nonzero(lock_array[-1]):
        lock_array = lock_array[:-1]
    while not np.count_nonzero(lock_array[:,0]):
        lock_array = lock_array[:,1:]
    while not np.count_nonzero(lock_array[:,-1]):
        lock_array = lock_array[:,:-1]
    
    while not np.count_nonzero(key_array[0]):
        key_array = key_array[1:]
    while not np.count_nonzero(key_array[-1]):
        key_array = key_array[:-1]
    while not np.count_nonzero(key_array[:,0]):
        key_array = key_array[:,1:]
    while not np.count_nonzero(key_array[:,-1]):
        key_array = key_array[:,:-1]

    for i in range(4):
        if np.all(np.rot90(key_array,i) == lock_array):
            return True
    return False

if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")

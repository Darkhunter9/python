import re
from itertools import combinations

def nonogram_row(row_string, clue_numbers):
    choice = []
    temp = []
    result = ''

    if not clue_numbers or 0 in clue_numbers:
        return row_string.replace('?','X')
    else:
        l = len(row_string)
        for i in range(l):
            if row_string[i] == '?':
                temp.append(i)
        
        t = len(temp)
        for i in range(t,0,-1):
            temp_len = len(choice)
            for j in list(combinations(temp, i)):
                temp_string = list(row_string)
                for k in j:
                    temp_string[k] = 'O'
                temp_string = ''.join(temp_string)
                choice.append(temp_string)
                for z in clue_numbers:
                    temp_result = re.search('O'*z, temp_string)
                    if not temp_result:
                        choice.pop(-1)
                        break
                    elif z != clue_numbers[-1] and temp_result.span()[-1] < len(temp_string) and temp_string[temp_result.span()[-1]] == 'O':
                        choice.pop(-1)
                        break
                    else:
                        temp_string = temp_string[temp_result.span()[-1]:]

        rm_list = []
        for i in choice:
            temp = re.findall(r'O+', i)
            if (len(temp) != len(clue_numbers) or
            any(len(temp[j]) != clue_numbers[j] for j in range(len(clue_numbers)))):
                rm_list.append(i)
        for i in rm_list:
            choice.remove(i)

        if not choice and i != t:
            return None
        # if temp_len == len(choice) and i != t:
        #     break

        for i in range(l):
            if row_string[i] == 'O':
                result += 'O'
            elif row_string[i] == 'X':
                result += 'X'
            elif all(j[i] == 'O' for j in choice):
                result += 'O'
            elif all(j[i] == '?' for j in choice):
                result += 'X'
            else:
                result += '?'
        
        return result


if __name__ == '__main__':
    assert nonogram_row('??????????', [8]) == '??OOOOOO??', 'Simple boxes_1'
    assert nonogram_row('??????????', [4, 3]) == '??OO???O??', 'Simple boxes_2'
    assert nonogram_row('???O????O?', [3, 1]) == 'X??O??XXOX', 'Simple spaces'
    assert nonogram_row('????X?X???', [3, 2]) == '?OO?XXX?O?', 'Forcing'
    assert nonogram_row('O?X?O?????', [1, 3]) == 'OXX?OO?XXX', 'Glue'
    assert nonogram_row('??OO?OO???O?O??', [5, 2, 2]) == 'XXOOOOOXXOOXOOX', 'Joining and splitting'
    assert nonogram_row('????OO????', [4]) == 'XX??OO??XX', 'Mercury'
    assert nonogram_row('???X?', [0]) == 'XXXXX', 'Empty_1'
    assert nonogram_row('?????', []) == 'XXXXX', 'Empty_2'
    assert nonogram_row('??X??', [3]) is None, 'Wrong string'
    print("Check done.")
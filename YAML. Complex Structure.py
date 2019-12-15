def count_space(w):
   space = 0
   for i in w:
      if i == ' ':
         space += 1
      else:
         return space

def make_list(l,level):
   result = []
   for i in range(len(l)):
      if l[i][:2*level+1] == ' '*(2*level)+'#':
         continue
      elif l[i] == ' '*(2*level)+'-':
         if i == len(l)-1 or count_space(l[i+1]) == 2*level:
            result.append(None)
         else:
            # judge type
            # Fine all next level words
            temp_l = []
            for j in range(i+1, len(l)):
               if count_space(l[j]) >= 2*level+1:
                  temp_l.append(l[j])
               else:
                  break

            if ':' in temp_l[0]:
               result.append(make_dict(temp_l, level+1))
            else:
               result.append(make_list(temp_l, level+1))
   
      elif count_space(l[i]) > 2*level:
         continue

      else:
         temp = l[i][2*level+2:]
         if '#' in temp and '"' not in temp:
            temp = temp[:temp.index('#')]
         if temp[0] == ' ': temp = temp[1:]
         if temp[-1] == ' ': temp = temp[:-1]
         if temp[0] == temp[-1] == '"': temp = temp[1:-1]
         try:
            result.append(int(temp))
         except:
            result.append(temp)
   
   return result

def make_dict(l,level):
   result = {}
   for i in range(len(l)):
      if count_space(l[i]) > 2*level:
         continue
      elif l[i][-1] == ':' and i != len(l)-1:
         key = l[i][2*level:l[i].index(':')]
         # judge type
         # Fine all next level words
         temp_l = []
         for j in range(i+1,len(l)):
            if count_space(l[j]) >= 2*level+1:
               temp_l.append(l[j])
            else:
               break
         if ':' in temp_l[0]:
            result[key] = make_dict(temp_l,level+1)
         else:
            result[key] = make_list(temp_l,level+1)
      else:
         key = l[i][2*level:l[i].index(':')]
         if l[i][-1] == ':':
            value = None
         else:
            value = l[i][l[i].index(':')+2:]
            if '#' in value and '"' not in value:
               value = value[:value.index('#')]
            if value[0] == ' ': value = value[1:]
            if value[-1] == ' ': value = value[:-1]
            value = value.replace('\\','')
            value = value.replace('\"','"')
            # value = value.replace('\\\"','\"')
            if value == 'null':
               value = None
            elif value[0] == value[-1] == '"': value = value[1:-1]
            

            try:
               value = int(value)
            except:
               if value == 'true':
                  value = True
               elif value == 'false':
                  value = False
         result[key] = value

   return result

def yaml(a):
   l = a.split('\n')
   while '' in l:
      l.remove('')
   while l[0][0] == '#':
      l = l[1:]
   if '-' in l[0]:
      result = make_list(l,0)
   else:
      result = make_dict(l,0)

   return result

if __name__ == '__main__':
   yaml("\nname: Alex\nage: 12")
   yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding: \"null\" ")
   yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding:")
   yaml("name: \"Alex \\\"Fox\\\"\"\nage: 12\n\nclass: 12b")
   yaml("name: \"Alex Fox\"\nage: 12\n\nclass: 12b")
   yaml("# comment\n- write some # after\n# one mor\n- \"Alex Chii #sir \"\n- 89 #bl")
   print("Example:")
   print(yaml('- Alex\n'
'-\n'
'  - odessa\n'
'  - dnipro\n'
'- Li'))

   # These "asserts" are used for self-checking and not for an auto-testing
   assert yaml('- Alex\n'
'-\n'
'  - odessa\n'
'  - dnipro\n'
'- Li') == ['Alex', ['odessa', 'dnipro'], 'Li']
   assert yaml('- 67\n'
'-\n'
'  name: Irv\n'
'  game: Mario\n'
'-\n'
'- 56') == [67,
{'game': 'Mario', 'name': 'Irv'},
None,
56]
   assert yaml('name: Alex\n'
'study:\n'
'  type: school\n'
'  number: 78\n'
'age: 14') == {'age': 14,
'name': 'Alex',
'study': {'number': 78,
         'type': 'school'}}
   assert yaml('name: Alex\n'
'study:\n'
'  - 89\n'
'  - 89\n'
'  - "Hell"\n'
'age: 14') == {'age': 14,
'name': 'Alex',
'study': [89, 89, 'Hell']}
   assert yaml('name: Alex\n'
'study:\n'
'  -\n'
'    type: school\n'
'    num: 89\n'
'  -\n'
'    type: school\n'
'    num: 12\n'
'age: 14') == {'age': 14,
'name': 'Alex',
'study': [{'num': 89,
         'type': 'school'},
         {'num': 12,
         'type': 'school'}]}
   assert yaml('name: Alex\n'
'study:\n'
'  -\n'
'    type: school\n'
'    nums:\n'
'      - 12\n'
'      - 67\n'
'  -\n'
'    type: school\n'
'    num: 12\n'
'age: 14') == {'age': 14,
'name': 'Alex',
'study': [{'nums': [12, 67],
         'type': 'school'},
         {'num': 12,
         'type': 'school'}]}
   print("Coding complete? Click 'Check' to earn cool rewards!")

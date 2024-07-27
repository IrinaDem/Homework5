immutable_var= 4,7,8, 'pineapple', True
print(immutable_var)
#immutable_var[0]=150  кортеж не поддерживает обращение по элементам
mutable_list = [1,2,3]
mutable_list.append('cat')
print(mutable_list)
mutable_list[0]='rat'
print(mutable_list)
mutable_list.extend([10,13])
print(mutable_list)
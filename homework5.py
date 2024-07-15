immutable_var = 1, 2, 3, 'a', 'b', 'c', 'avto'
print(immutable_var)
#immutable_var_[0] = 5
#print(immutable_var)
mutable_list = [1, 2, 3, 'w', "avto"]
print(mutable_list)
mutable_list[1] = 5
mutable_list.append('www')
print(mutable_list)
print('кортеж - это неизменяемая упорядоченная коллекция, используется в качестве хранилища(того,что мы не хотим трогать и менять) и занимает в памяти меньше места, чем список')
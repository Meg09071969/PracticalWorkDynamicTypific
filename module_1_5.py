immutable_var = 1, 2, "E", "D"
print(immutable_var)
#immutable_var [0] = 200
print(immutable_var ) # элементы кортежа изменить нельзя потому что кортеж является  неизменяемой коллекцией

mutable_list = [9, 7, 1969, "Дата рождения"]
print(mutable_list)
mutable_list[1] = "июля"
print(mutable_list)

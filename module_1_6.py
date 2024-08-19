my_dict = {"Eduard": 1969, "Max": 1987, "Nikita": 2003}
print(my_dict)
print(my_dict["Eduard"])
print(my_dict.get("Svetlana"))
my_dict.update({"Petr": 1984, "Elizaveta": 1987})
print(my_dict)
a = my_dict.pop("Petr")
print(my_dict)
print(a)
print(my_dict)

my_set = {9, 7, 1969, "Eduard", (1, 2, 3), "Яблоко", 12.32, "Eduard", 12.32}
print(my_set)
print(my_set.add("Urban",))
print(my_set.add(5))
print(my_set)
print(my_set.discard((1, 2, 3)))
print(my_set)


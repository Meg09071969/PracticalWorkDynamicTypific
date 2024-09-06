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

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_m = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]

students_sort = sorted(students)
print(students_sort)

dict1 = dict(zip(students_sort, grades_m))
print(dict1)


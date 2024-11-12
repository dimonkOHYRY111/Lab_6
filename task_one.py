def remove_odd(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 0]


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Оригінальний список: {my_list}")

my_list = remove_odd(my_list)
print(f"Список після видалення елементів з непарними індексами: {my_list}")
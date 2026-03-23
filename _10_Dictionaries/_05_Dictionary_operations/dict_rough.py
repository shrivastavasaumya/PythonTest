
# students = {
#     "101": {"name": "Rahul", "age": 18},
#     "102": {"name": "Amit", "age": 19},
#     "103": {"name": "Neha", "age": 17}
# }

# print(len(students))

# for i in students:
#     print(i, students[i])

# print(students['s2']['age'])
# student = {"name": "Rahul", "age": 18}

# print(student.keys())

# for number, details in students.items():
#     for j in details.items():
#         print(j)

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 10, "c": 3}

# # d3 = d1 | d2
# d1 |= d2
# print(d2)


# d1 = {"a": 1, "b": 2}
# d2 = {"b": 10, "a": 3}

# d1 |= d2
# d2 |= d1

# print(d1)

roy = {}
for i in range (1, 11):
    if i % 2 == 0: 
        roy[i] = i ** 2
    else:
        roy[i] = i ** 3
print(roy)

res = { i : i** 2  if i % 2 == 0  else i ** 3 for i in range(1 , 11)}
print(res)
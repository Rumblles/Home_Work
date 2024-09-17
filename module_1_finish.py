grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
avg = dict()
students = sorted(students)
print(students)
a = sum(grades[0])/len(grades[0])
a_1 = sum(grades[1])/len(grades[1])
a_2 = sum(grades[2])/len(grades[2])
a_3 = sum(grades[3])/len(grades[3])
a_4 = sum(grades[4])/len(grades[4])
print(a,a_1,a_2,a_3,a_4)
avg[students[0]] = a
avg[students[1]] = a_1
avg[students[2]] = a_2
avg[students[3]] = a_3
avg[students[4]] = a_4
print(avg)



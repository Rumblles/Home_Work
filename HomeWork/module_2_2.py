first = 111
second = 341
third = 111

if first == second or second == third or third == first:
    print(2)

elif first == second == third:
    print(3)


elif first != second and second != third and third != first:
    print(0)

else:
    print('Понять и простить')
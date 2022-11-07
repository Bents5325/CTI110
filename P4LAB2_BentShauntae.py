integer1 = int(input())
integer2 = int(input())

if integer1 <= integer2:
    while integer1 <= integer2:
        print(integer1, end = " ")
        integer1 = integer1 + 5
    print()
else:
    print('Second integer can\'t be less than the first.')
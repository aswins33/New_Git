"""
How many numbers you wish to enter : 4

1. Enter the number : 12
2. Enter the number : 13
3. Enter the number : 7
4. Enter the number : 4

sorted list is : [4,7,12,13]

"""
"""n = int(input("How many numbers you wish to enter : "))

numbers = []
for i in range(1, n + 1):
    num = int(input(f"{i}. Enter the number : "))"""



rows = 4

for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(i * j, end=" ")
    print()
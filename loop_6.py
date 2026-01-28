arr = [5,4,11,27,3]
n=len(arr)
for i in range(n):
    print("i = ",i)
    for j in range(0, n-i-1):
        print("j = ",j)
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

        

print(arr)
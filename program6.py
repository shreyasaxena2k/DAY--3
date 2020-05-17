def findSmallest(arr, n):
    r = 1
    for i in range(0, n):
        if arr[i] <= r:
            r = r + arr[i]
        else:
            break
    return r


n1 = int(input("Enter number of elements in list: "))
arr1 = []
print("Enter elements of list: ")
for i in range(n1):
    c = int(input())
    arr1.append(c)
arr1.sort()
print("Smallest non-representable number: ", findSmallest(arr1, n1))





# Code by shreya saxena
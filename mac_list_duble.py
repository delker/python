import time
f = open("arp.txt", "r")
arr = f.readlines()
N = len(arr)
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i] == arr[j]:
            print("Есть одинаковые")
            print(arr[i])
            print(arr[j])

print("Все элементы уникальны")
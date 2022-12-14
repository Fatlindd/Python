
def search(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

arr = [2, 3, 4, 5, 10, 40, 24, 15, 32, 4, 13, 10]
x = int(input('> Search number: '))
N = len(arr)

result = search(arr, N, x)

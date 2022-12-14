
def search(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

def checkForDuplicate(arr, num):
    sortedList = arr
    sortedList.sort()
    count = 0
    for element in sortedList:
        if element == num:
            count += 1
    
    if count > 1:
        return True
    return False

arr = [2, 3, 4, 5, 10, 40, 24, 15, 32, 4, 13, 10]
x = int(input('> Search number: '))
N = len(arr)

result = search(arr, N, x)
if result == -1:
    print('Element is not present in array')
else:
    print('Element is present at index', result)
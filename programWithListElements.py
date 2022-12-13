# Option 1
def get_largestNumber(number):
    largest = 0
    for num in number:
        if num > largest:
            largest = num
    return largest

# Option 2
def get_second_largest(listNumbers):
    largest = listNumbers[0]
    second_largest = listNumbers[0]
    for num in range(1, len(listNumbers)):
        if listNumbers[num] > largest:
            second_largest = largest
            largest = listNumbers[num]
        elif listNumbers[num] > second_largest:
            second_largest = listNumbers[num]
    return second_largest

# Option 3
def get_smallest(listNumbers):
    smallest = listNumbers[0]
    for num in listNumbers:
        if num < smallest:
            smallest = num
    return smallest

# Option 4
def get_second_smallest(listNumbers):
    smallest = listNumbers[0]
    second_smallest = listNumbers[0]
    for num in range(1, len(listNumbers)):
        if listNumbers[num] < smallest:
            second_smallest = smallest
            smallest = listNumbers[num]
        elif listNumbers[num] < second_smallest:
            second_smallest = listNumbers[num]
    return second_smallest

# Option 5
def sortNumbersList(listNumbers):
    numbers = listNumbers[:]
    numbers.sort()
    return numbers

# Option 6
def sortReverseNumbersList(listNumbers):
    numbers = listNumbers[:]
    numbers.sort(reverse = True)
    return numbers

# Option 7
def getEvenAndOddNumbers(listNumber):
    evenNumbers = list(filter(lambda x: x % 2 == 0, listNumber))
    oddNumbers = list(filter(lambda x: x % 2 == 1, listNumber))
    return 'Even numbers: {} \nOdd numbers: {}'.format(evenNumbers, oddNumbers)


print("""
        --------------------------------------------------------------------
        | Hi! Below you can see a list with some numbers element! And also | 
        | you can choose one option to play with these numbers!            |
        --------------------------------------------------------------------  
        """)

listNumbers = [22, 41, 12, 18, 34, -1, 25, 16, 11]
print('>| Choose one option: ' + 
        '\n 1. Get largest number' +
        '\n 2. Get second largest number'+
        '\n 3. Get smallest number' +
        '\n 4. Get second smallest number' +
        '\n 5. Sort list' +
        '\n 6. Get reversed list' +
        '\n 7. Get even and odd numbers' +
        '\n 8. Get sum of numbers in list' +
        '\n 9. Remove specific element from list' +
        '\n 10. Add new element in list' + 
        '\n 11. Check if specific number is in list' +
        '\n 12. How many elements are in list' +
        '\n 13. Save the list in a file named numbers.txt' +
        '\n 14. Clear list and generate new one' +
        '\n 15. Print list')
    

import csv

def addToFile():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def deleteRecord():
    file = open("Salaries.csv", "r")
    x = 0
    tmplist = []
    for row in file:
        tmplist.append(row)
    file.close()
    for row in tmplist:
        print(x, row)
        x = x + 1
    rowtodelete = int(input("Enter the row number to delte: "))
    del tmplist[rowtodelete]
    file = open("Salaries.csv", "w")
    for row in tmplist:
        file.write(row)
    file.close()

tryagain = True
while tryagain == True:
    print("1) Add To File")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")
    print()
    selection = input("Enter the number of your selection: ")
    if selection == "1":
        addToFile()
    elif selection == "2":
        viewrecords()
    elif selection == "3":
        deleteRecord()
    elif selection == "4":
        tryagain = False
    else:
        print("Incorrect option")
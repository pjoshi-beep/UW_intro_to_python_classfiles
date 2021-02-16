# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PJoshi, 2.15.2021, added code to complete the assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
"""  # A menu of user options

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "w")
dicRow1 = {"TASK": "Clean kitchen", "PRIORITY": "high"}
dicRow2 = {"TASK": "Write Essay", "PRIORITY": "medium"}
dicRow3 = {"TASK": "Organize bookshelf", "PRIORITY": "low"}
objFile.write(dicRow1["TASK"] + ',' + dicRow1["PRIORITY"] + '\n')
objFile.write(dicRow2["TASK"] + ',' + dicRow2["PRIORITY"] + '\n')
objFile.write(dicRow3["TASK"] + ',' + dicRow3["PRIORITY"] + '\n')
objFile.close()

objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"TASK": lstRow[0], "PRIORITY": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Enter a task: ")
        priority = input("Enter priority level (low/med/high): ")
        newdicRow = {"TASK":task, "PRIORITY":priority}
        lstTable.append(newdicRow)
        continue

    # Step 5 - Remove an item from the list/Table based on its name
    elif (strChoice.strip() == '3'):
        edit = input("Enter the task you wish to remove: ")
        for row in lstTable:
            if row["TASK"].lower() == edit.lower():
                lstTable.remove(row)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["TASK"]) + "," + str(row["PRIORITY"]) + '\n')
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program

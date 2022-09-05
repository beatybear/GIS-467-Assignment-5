# -*- coding: utf-8 -*-
"""
1. Write a script that continues to prompt a user for integers until the user hits 
    enter without a value.  The program should then determine and report the count 
    and average of the numbers entered.
2. Iterate over a list of a numbers. From this list create two new lists; one with 
    only the odd numbers and one with only the even numbers.
    Extra credit: Use the random module and the randint function to generate your 
    list. Extra extra credit if you use list comprehension
3. Write a program that reads earthquake information from a file (included with this 
    PowerPoint on moodle) and prints the count of earthquakes with a magnitude of 
    4.0 or greater.
4. Create a shopping list script:
    Check whether or not the item that the user enters is already on the shopping 
    list. If it isn’t on the list yet, add it. If it is on the list, alert them with 
    a message and don’t add it.  Include logic to handle casing of letters.
    When the user is done entering items (hits enter without entering another value), 
    print the shopping list as a comma delimited string
"""
import random
import csv

class AssignmentFive:
    #1 input numbers
    numbers = [input("Please enter integers separated by hitting the enter key.\nOnce you are done, hit enter with an empty value.\n")]
    while(numbers[len(numbers)-1] != ""):
        numbers.append(input())
    numbers.remove(numbers[len(numbers)-1])
    count = 0
    avg = 0
    for num in numbers:
        count += 1
        avg += int(num)
    avg /= len(numbers)
    print(f"There were {count} numbers input.\nThe average is {round(avg, 3)}.")
    
    #2 number list
    randomNumbers = []
    for i in range (random.randint(1, 100)):
        randomNumbers.append(random.randint(1, 100))
    print(f"\nThe list is:\n{randomNumbers}")
    evenNums = [x for x in randomNumbers if (x%2 == 0)] #populate the lists using list comprehension
    oddNums = [x for x in randomNumbers if (x%2 != 0)]    
    '''
    To try the basic way first, so I know it works.
    evenNums = []
    oddNums = []
    for num in randomNumbers:
        if(num%2 == 0):
            evenNums.append(num)
        else:
            oddNums.append(num)
    '''
    print(f"The even numbers are:\n{evenNums}")
    print(f"The odd numbers are:\n{oddNums}")
    
    #3 earthquake information
    earthquakes = []
    csv_file = r"C:/Users/beaty/Desktop/SP 2022/GIS 467-667/GIS 467 assignment 5/earthquakes.csv"
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        header = next(csv_reader) #the first row has the column headers
        for row in csv_reader:
           earthquakes.append(row)
    quakeCount = 0
    for event in earthquakes:
        if(float(event[4]) >= 4.0):
            quakeCount += 1
    print(f"\nThere are {quakeCount} earthquakes of magnitude 4.0 or higher in the dataset.\n")
    
    #4 shopping list
    shoppingList = [input("Please enter items for your shopping list separated by hitting the enter key.\nOnce you are done, hit enter with an empty value.\n")]
    while(shoppingList[len(shoppingList)-1] != ""):
        temp = input()
        contains = False
        if temp.lower() in shoppingList:
            print("This item is already in your list.")
        else:
            shoppingList.append(temp.lower())
    shoppingList.remove(shoppingList[len(shoppingList)-1])
    ShoppingList = ",".join(shoppingList) #creates a comma delimited string by combining the elements of the list with a given delimiter
    print(f"Here is your shopping list:\n{ShoppingList}")

    input("Press enter to exit.")
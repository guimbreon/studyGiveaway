import json
from constants import *

def readFile(fileName):
    """
    Reads data from a JSON file and returns it.

    Requires:
    - fileName (str): The name of the JSON file to read.

    Ensures:
    - Reads the JSON file specified by fileName.
    - Returns the loaded data as a Python object.
    """
    with open(fileName, 'r') as file:
        fileJson = json.load(file)
    return fileJson

def writeFile(fileName, fileData):
    """
    Writes data to a JSON file.

    Requires:
    - fileName (str): The name of the JSON file to write to.
    - fileData (object): The data to write to the JSON file.

    Ensures:
    - Writes the provided data to the JSON file specified by fileName.
    """
    with open(fileName, 'w') as jsonFile:
        json.dump(fileData, jsonFile, indent = 2)

def selection(file):
    """
    Selects and returns a list of people who are students and aged between 18 and 26.

    Requires:
    - file (list): List of people with associated information.

    Ensures:
    - Selects individuals who are students and aged between 18 and 26.
    - Returns a list of selected people.
    """
    selected = []
    for person in file:
        if person[AGE] <= 26 and person[AGE] >= 18 and person[STUDENT]:
            selected.append(person)
    return selected

def medianGrade(allPeople):
    """
    Calculates and returns a list of people whose median grade is above 75%.

    Requires:
    - allPeople (list): List of people with associated information, including grades.

    Ensures:
    - Calculates the median grade for each person.
    - Selects individuals with a median grade above 75%.
    - Returns a list of qualified people.
    """
    medianPeople = []
    for people in allPeople:
        grade = 0
        for i in range(3):
            grade += people[GRADES][i]
        grade = round(grade/3,2)
        #checks if the median grade is over 75% and if it is, it qualifies for the giveAway
        if grade >= 75:
            people[GRADES] = grade
            medianPeople.append(people)
    return medianPeople

def sortPeople(allPeople):
    """
    Sorts a list of people first by city and then by descending grades.

    Requires:
    - allPeople (list): List of people with associated information.

    Ensures:
    - Sorts the list of people by city and then by descending grades.
    - Returns the sorted list.
    """
    allPeople = sorted(allPeople, key = lambda people: (people[CITY],-people[GRADES]))
    return allPeople

def getCities(allPeople):
    """
    Returns a list of unique cities from a list of people.

    Requires:
    - allPeople (list): List of people with associated information.

    Ensures:
    - Extracts and returns a list of unique cities from the input data.
    """
    cities = []
    for person in allPeople:
        if person[CITY] not in cities:
            cities.append(person[CITY])
    return cities

def top5(allPeople, city):
    """
    Returns the top 5 people from a specific city, sorted first by city and then by descending grades.

    Requires:
    - allPeople (list): List of people with associated information.
    - city (str): The specific city to filter by.

    Ensures:
    - Filters people from the specified city.
    - Sorts the filtered list by city and then by descending grades.
    - Returns the top 5 people from the sorted list.
    """
    fromCity = []
    for people in  allPeople:
        if people[CITY] == city:
            fromCity.append(people)
    fromCity = sortPeople(fromCity)
    top5P = []
    if len(fromCity) > 5:
        for i in range(5):
            top5P.append(fromCity[i])
        return top5P
    else:
        return fromCity

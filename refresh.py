import dataWork
import copy
import sys
from constants import *
def refresh(fileName, minAge = MINAGE, maxAge = MAXAGE, medGrade = MEDGRADE):
    """
    Refreshes data by applying a series of operations and writes the result to a new file.

    Requires:
    - fileName (str): The name of the JSON file containing the original data.

    Ensures:
    - Creates a new file with the name 'lastData' instead of 'data'.
    - Selects people who are students and aged between 18 and 26.
    - Calculates the median grade for the selected individuals.
    - Retrieves a list of unique cities from the selected data.
    - Retrieves the top 5 people for each city, sorted by city and then by descending grades.
    - Writes the combined top 5 lists to the new file.
    - Prints "finished" after completing the refresh process.
    """
    newFile = copy.deepcopy(fileName).replace("data","lastData")
    file = dataWork.readFile(fileName)
    people = dataWork.selection(file, minAge , maxAge)
    people = dataWork.medianGrade(people, medGrade)
    cities = dataWork.getCities(people)
    allTop5 = []
    for city in cities:
        allTop5.append(dataWork.top5(people, city))
    allInOne = []
    for top5 in allTop5:
        for top in top5:
            allInOne.append(top)
    dataWork.writeFile(newFile, allInOne)
    print("finished")
try:
    fileName = sys.argv[1]
    refresh(fileName)
except:
    print("Enter a valid filePath in the format\npython3 refresh.py filePath")
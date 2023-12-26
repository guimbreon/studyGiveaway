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
    print("a")
    people = dataWork.selection(file, minAge , maxAge)
    print("b")
    people = dataWork.medianGrade(people, medGrade)
    print("c")
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
    custom = len(sys.argv)
    print(custom)
    if custom <= 5:
        if custom == 2:
            refresh(fileName)
        elif custom == 3:
            refresh(fileName, int(sys.argv[2]), 122) # 122 being the age of the oldest person to ever live.
        if sys.argv[2] <= sys.argv[3]:
            if custom == 4:
                refresh(fileName, int(sys.argv[2]), int(sys.argv[3])) 
            elif custom == 5:
                refresh(fileName, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])) 
        else:
            print("The amount given in minAge should be smaller than maxAge!")
    else:
        print("""The amount of arguments given for custom refresh is greater than 3.
              python3 refresh.py filePath minAge maxAge medGrade
              This is the biggest run you should do.""")
except:
    print("Enter a valid filePath in the format\npython3 refresh.py filePath")
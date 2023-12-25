from constants import *
import random
import json
from faker import Faker
import sys
faker = Faker()
def randomGen(count,fileName):
    """
    Generates a random list of people with associated information and writes it to a JSON file.

    Requires: 
    - count (int): The number of people to generate.
    - fileName (str): The name of the JSON file to write the generated data to.

    Ensures:
    - Generates a list of people with random names, ages, cities, student status, and grades.
    - Writes the generated data to a JSON file specified by fileName.
    """
    allPeople = []
    cities = []
    #get x cities
    for i in range(count//random.randint(26, 52)):
        cities.append(faker.city())
    while count > 0:
        person = {}
        person[NAME] = faker.name()
        person[AGE] = random.randint(10,100)
        person[CITY] = random.choice(cities)
        person[STUDENT] = random.choice([True,False])
        person[GRADES] = []
        for i in range(3):
            person[GRADES].append(random.randint(5,100))
        allPeople.append(person)
        count -= 1
    with open(fileName, 'w') as jsonFile:
        json.dump(allPeople, jsonFile, indent = 2)

count = sys.argv[1]
fileName = sys.argv[2]
randomGen(count, fileName)
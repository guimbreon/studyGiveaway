# Data Processing README

## Prerequisites
Make sure to install the required library before running the program:

```bash
pip install faker
```

## Program Overview

This set of Python scripts is designed to process and organize data from a JSON file containing information about individuals. The goal is to filter and organize the data based on specific criteria and generate new files for each city, further organized according to specified requirements.

## JSON Data Structure

Each person in the JSON file is structured as follows:

```json
{
    "name": "Brian Kim",
    "age": 83,
    "city": "Walkermouth",
    "isStudent": false,
    "grades": [21, 24, 62]
}
```

## Selection Criteria

- `isStudent` must be true.
- The top 5 grades for each city are considered.

### Standart Criteria:
To be included, individuals must meet the following criteria:
- Grades must be equal to or greater than 75.
- Age must be between 18 and 26.

### Custom Criteria:
- mininum median grade;
- min and max age.

They should be represented by this order:
   ```python
   python3 refresh.py "your_original_data.json" minAge maxAge medianGrade
   ```
You can personalize it by only giving:
- minAge;
- minAge + maxAge;
- minAge + maxAge + medianGrade;

## Overall Organization
The complete JSON file is organized based on the following criteria:
1. **City:** Individuals are grouped by their respective cities.
2. **Grades:** Within each city, individuals are further organized based on their grades.

## Program Execution

### Refresh Operation
The `refresh` function performs the following operations:
1. Reads data from the original JSON file specified by `fileName`.
2. Selects individuals based on the defined criteria.
3. Calculates the median grade for the selected individuals.
4. Retrieves a list of unique cities from the selected data.
5. Retrieves the top 5 people for each city, sorted by city and then by descending grades.
6. Writes the combined top 5 lists to a new file named 'lastData'.
7. Prints "finished" after completing the refresh process.

## Execution Instructions

1. Install the required library:

   ```bash
   pip install faker
   ```

2. Run the `refresh` function by providing the original JSON file name:

   ```python
   python3 refresh.py "your_original_data.json"
   ```

## Additional Notes

- Ensure that the original JSON file follows the required structure for successful execution.
- The output files will be generated with the name 'lastData' instead of 'data' to avoid overwriting the original data file.
- If you don't have any personal data to use, you can run randomGen.py with:

   ```python
   python3 randomGen.py count "your_original_data.json"
   ```
   
   count is the amount of people you want to generate


Feel free to reach out if you encounter any issues or have further questions!

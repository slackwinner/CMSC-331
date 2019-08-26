# File: hw2.py
# Author: Dane Magbuhos
# Date: 9/23/18
# E-mail: mag4@umbc.edu
# Description: This program reads in a file,
#              analyzes the content, and outputs
#              the statistical results.

# Used as index indicators
DATE          = 0
MATCH         = 1
DISTANCE      = 2
PLAYER        = 3
RESULT        = 4
ERROR         = 5

# Helper Variables
DEFAULT       = 0
INCREMENT     = 1
COLUMN        = 5

def average(shotDistance):

    summation = DEFAULT
    average   = DEFAULT
    zeroError = DEFAULT
    
    averageResults = []

    # Adds up all values within list
    for x in range (len(shotDistance)):
        summation = summation + shotDistance[x]

    try:
        # Calculates average shot distance
        average = summation / len(shotDistance)

    # Handles Zero Division Error Exception
    except ZeroDivisionError:
        zeroError += INCREMENT
        average = DEFAULT

    # Rounds value to nearest two decimal places
    average = round(average, DISTANCE)

    # Stores results into list
    averageResults.append(average)
    averageResults.append(zeroError)

    # Returns list 
    return averageResults

def analyzeData(data):

    row        = DEFAULT
    indexError = DEFAULT
    valueError = DEFAULT
    dataCount  = DEFAULT

    shotDistance = []
    dataResult = []

    # Traverses through 2D list
    while row < len(data):

        col = DEFAULT
        
        while col < len(data[row]):
           
            try:
                # Typecasts DISTANCE and RESULT index values
                if col == DISTANCE :
                    data[row][RESULT] = int(data[row][RESULT])
                    data[row][DISTANCE] = float(data[row][DISTANCE])
                   
                    # Stores DISTANCE values within list 
                    if data[row][col + DISTANCE] == MATCH:
                       shotDistance.append(data[row][DISTANCE])
                                                  
            # Handles the Index Error Exception
            except IndexError:
            
                if len(data[row]) < COLUMN:
                    indexError += INCREMENT
                pass

            # Handles the Value Error Exception
            except ValueError:
            
                if col == DISTANCE or col == RESULT:
                    valueError += INCREMENT

                pass

            # Increments column index
            col += INCREMENT

        # Counts total amount of data within 2D list
        dataCount += INCREMENT
     
        # Increments row index
        row += INCREMENT

    # Calculates the average of shot distance
    averageResults = average(shotDistance) 
    
    # Adds dervied data results to list
    dataResult.append(dataCount)
    dataResult.append(len(shotDistance))
    dataResult.append(averageResults[DATE])
    dataResult.append(indexError)
    dataResult.append(valueError)
    dataResult.append(averageResults[MATCH])

    return dataResult

def readData(fileName):

    fileObj = open(fileName)
    
    # Skips over headers
    newLine = fileObj.readline()
    
    # Reads in rest of data
    newLines = fileObj.readlines()

    # Closes file
    fileObj.close()

    resultList = []
    index = DEFAULT

    # Stores data within 2D list as strings
    while index < len(newLines):
         line = newLines[index].strip().split(",")
         resultList.append(line)

         index += INCREMENT
        
    return resultList
        
                                          
def main():

    fileName = "test-data.csv"

    # Calls readData function to read in file 
    data = readData(fileName)

    # Calls analyzeData function to calculate the statistics of data
    statResult = analyzeData(data)

    # Outputs statistical results from data
    print "Total number of records: ", statResult[DATE]
    print "The number of records used for calculation: ", statResult[MATCH]
    print "The average successful shot distance: ", statResult[DISTANCE]
    print "Number of index errors: ", statResult[PLAYER]
    print "Number of value errors: ", statResult[RESULT]
    print "Number of division by zero errors: ", statResult[ERROR]

main()

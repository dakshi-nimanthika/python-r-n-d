import csv
import statistics
import numpy as np

# Insert the user input origin, destination, route  using folowing commands

selectedOrigin = input('Enter Origin (default "BUTLER, IN")')    
selectedDestination = input('Enter Destination  (default "ARBELA, MS")')  
selectedRoute = input('Enter Route (default "CSXT-BRKWA-CAGY")')

# If the user didnt input anything the values will assigned to the below mention  origin, destination and route.

if selectedOrigin == '':
    selectedOrigin = "BUTLER, IN"
    
if  selectedDestination == '':
    selectedDestination = "ARBELA, MS"

if  selectedRoute == '':
    selectedRoute = "CSXT-BRKWA-CAGY" 

# Read data csv file 

with open('data.csv', newline='') as csvfile:
    dataset = csv.reader(csvfile, delimiter=',', quotechar='"')

# Extract time for given inputs 
    arrayTime = []
    for row in dataset:
        if row[0] == selectedOrigin and row[1] == selectedDestination and row[2] == selectedRoute:
            arrayTime.append(float(row[3]))

arrayTimeLength = len(arrayTime)

# If the sizee of the data set is less than 5 
# then the mean vallue of the data are calculated as the New Eta
if arrayTimeLength > 0 and arrayTimeLength < 5:
    
    print('=== New ETA (when sample size less than 5) ===', round(statistics.mean(arrayTime),2))

# If the sizee of the data set  is greater than 5 and less than 30 
# then first sort the array and  remove 25% from the both end 
# and calculated the  mean vallue of the data as the New Eta

elif arrayTimeLength > 5 and arrayTimeLength < 30:
  
    sortedArray = sorted(arrayTime)
  
    index25 = int(arrayTimeLength * 0.25)
    index75 = int(arrayTimeLength * 0.75)
##    print('=== index 25  ===\n', index25)
##    print('=== index 75  ===\n', index75)
##    print('=== index 25  ===\n', sortedArray[index25])
##    print('=== index 75  ===\n', sortedArray[index75])

    array25To75 = []
    for i in range(index25,index75):
            array25To75.append(sortedArray[i])
            
    print('=== Original Data Set  ===\n', sortedArray)
    print('=== 25%-75% array Data Set  ===\n', array25To75)
    print('=== New ETA 25%-75% array  ===', round(statistics.mean(array25To75),2))
    
# If the sizee of the data set  is greater than 30 
# then  first sort the array and remove outliers from the data set
# which are lie outside i.e  1.5* interquartile range away from the mean
# and take the mean value as the New Eta
elif arrayTimeLength > 30:
    
    sortedArray = sorted(arrayTime)

    higher = np.percentile(sortedArray, 75, interpolation='higher')
    lower = np.percentile(sortedArray, 25, interpolation='lower')
   
    qRange =  higher - lower

    print('=== higher  ===\n', higher)
    print('=== lower  ===\n', lower)
    print('=== Inter Quartile range  ===\n', qRange)
    
    mean = statistics.mean(sortedArray)
    
    arrayQuartile = []
    
    q1 = int( mean - (1.5 * qRange))
    q2 = int( mean + (1.5 * qRange))
    
    for i in sortedArray:
        if i >= q1 and i <= q2:
            arrayQuartile.append(i)              

    print('=== Original Data Set  ===\n', sortedArray)
    print('=== Data Set without Outliers ===\n', arrayQuartile)
    print('=== New ETA from quaritle array ========= \n', round(statistics.mean(arrayQuartile),2))

else:
    print('=== There is no raw data set for selected inputs =========')


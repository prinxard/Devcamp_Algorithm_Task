 
import math 
arr = [600, 470, 170, 430, 300]
arrayLen = len(arr)
# Function for calculating variance 
def variance(a, arrayLen): 
  
    # Compute mean (average of 
    # elements) 
    sum = 0
    for i in range(0 ,arrayLen): 
        sum += a[i] 
    mean = sum /arrayLen 
  
    # Compute sum squared  
    # differences with mean. 
    squareDifference = 0
    for i in range(0 ,arrayLen): 
        squareDifference += ((a[i] - mean)  * (a[i] - mean)) 
    return squareDifference / arrayLen 
  
  
def standardDeviation(arr, arrayLen): 
  
    return math.sqrt(variance(arr, arrayLen))  
print("Standard Deviation: ", round(standardDeviation(arr, arrayLen), 2)) 
  

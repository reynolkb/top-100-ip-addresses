# import defaultdict, random for int generation and time for printing out how long each function takes to run
from collections import defaultdict
import random
import time

# Create a default dictionary sortable by value, all the values are integers
# Default dictionary allows you to add a new key/value pair only if the key doesn't already exists
# If the key does exist then do not create a new key/value pair
ipAddresses = defaultdict(int)

def requestHandled(ipAddress):
    '''
    Function that takes in one ip address at a time and assigns the key to the ip address
    If the ip address doesn't exist already in the dictionary, then create value of 1
    If the ip address does exist, increment the value by 1
    '''
    ipAddresses[ipAddress] += 1

def top100():
    '''
    Sort the ipAddresses dictionary by the value which is the number of times the ip address has been requested
    Key in the sort is getting each value in the ipAddresses dictionary
    Order the sorted dictionary in descending order with the largest value first
    '''
    for ipAddress in sorted(ipAddresses, key=ipAddresses.get, reverse=True)[:100]:
        # For the first 100 ip addresses in the sorted dictionary, print the ipAddress along with the request count
        print(ipAddress, ipAddresses[ipAddress])

def clear():
    '''
    Clear out the dictionary at the start of each day
    '''
    ipAddresses.clear()

def run():
    '''
    I used random integers instead of random ip addresses for testing so I could create multiple requests from the same integer
    I did convert these integers into strings
    '''
    # StartTime for run function
    startTime = time.time()
    
    # Call requestHandled with random ip adresses ranging from 1 - 1 million, 10 million times
    for _ in range(10000000):
        ip = str(random.randint(1,1000000))
        requestHandled(ip)
    
    # Print how long it took to run request_handled() function
    print('request_handled() called 10,000,000 times ' + str(time.time() - startTime))

    # Reintialize startTime
    startTime = time.time()
    
    # Call top100 to get the ip addresses with the most requests
    top100()

    # Print how long it took to run top100() function
    print('top100() called ' + str(time.time() - startTime))

    # Clear out the dictionary and print to show it's cleared
    print('clearing out dictionary')
    clear()
    print(ipAddresses)

run()
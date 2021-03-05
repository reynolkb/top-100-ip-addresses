from collections import defaultdict

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

# function to return top 100 ip addresses by count, with highest traffic ip address first
# def top100():

# clear ip addresses and count at the start of each day
# def clear():
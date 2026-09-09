import re

# prompts user for filename
filename = input('File name please: ')
# creates dict to store ip adresses and how many failed logins
addresses = {}

file = open(filename, 'r')

# for each line in file check has keywords
for line in file:
    if 'invalid' or 'failed' in line:
        # extract ip address from line
        ip_address = str(re.find(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'))
        # checks if ip address already in dict and adds to count of failed logins
        if ip_address in addresses:
            addresses[ip_address] += 1
        # otherwise, creates new dict entry
        else:
            addresses[ip_address] = 1 

# for each address, checks if failed to log in 5 or more times and prints out information if so
for address in addresses:
    if addresses[address] >= 5:
        print(f"Suspicious user, IP address {address} has failed to log in {addresses[address]} times")
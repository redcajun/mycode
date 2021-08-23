#!/usr/bin/env python3
# create a list with at least two ip addresses to be displayed
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
# display only the ip addresses adding up the strings
print("IP addresses are: ",  iplist[3] + " and " +  iplist[4])
# alternative method 1 using f-string
print(f"IP addresses are: {iplist[3]} and {iplist[4]}")
# alternative method 2 using comma seperator
print("IP addresses are: ", iplist[3], " and ", iplist[4])

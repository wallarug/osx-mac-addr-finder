#!/bin/python27

# Script for getting OSX MAC Addresses
# Created by Cian Byrne 2017

from subprocess import call, check_output

# DEBUG TOGGLE SWITCH #
DEBUG = False
FINDSERIAL = False

# set up variables...
macaddr = {}
serial_number = ""
inter_count = 0
company = "Marist College North Shore"

# display a message to the user informing them this could take a minute
#  to run on there device...
print "***************************"
print "* MAC ADDRESS FINDER 2017 *"
print "***************************"
print "Welcome to the {0} MAC Address Finder.\n".format(company)
print "This script will find the MAC addresses of all your network cards.  It can also get your device serial number.\n"
print "This script will take about 1 minute to run, please be patient during this process.\n"
print "Thank you.\n"

print "INFO: Program started..." 

# get a list of all the interfaces present on the device...
interfaces = check_output(["ifconfig", "-l"]).strip("\n").split(" ")
if DEBUG: print interfaces

# get the MAC addresses of any wireless or ethernet cards...
for inter in interfaces:
    if "en" in inter:
        if DEBUG: print inter
        temp = check_output(["ifconfig", inter])
        index = temp.find("ether")
        macaddr[inter] = temp[index+6:index+23]
        inter_count += 1
        if DEBUG: print macaddr[inter]

# find the Serial Number of this macbook...
if FINDSERIAL:
    if DEBUG: print "Starting System Profiler..."
    temp_serial = check_output(["system_profiler"])
    index_serial = temp_serial.find("Serial Number (system)")
    serial_number = temp_serial[index_serial+24:index_serial+35]


# Output to the user the serial number and MAC addresses to the user...
print "\n** Results **"
if FINDSERIAL: print "Serial Number: {0}".format(serial_number)
for inter in macaddr:
    if inter_count > 1:
        # Interface 0 is ethernet
        print "LAN ({0}) MAC Address: {1}".format(inter, macaddr[inter])
        inter_count -= 1
    else:
        print "WiFi ({0}) MAC Address: {1}".format(inter, macaddr[inter])

print "\nThank you.  Have a nice day!"

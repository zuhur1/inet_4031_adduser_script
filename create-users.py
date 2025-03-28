#!/usr/bin/python3

# INET4031
# Zuhur Hashi
# 03/27/2025
# 03/27/2025

#os - provides functions to interact with the operating system, re - used for working with regular expression, sys allows input/output
import os
import re
import sys


def main():
    for line in sys.stdin:

        #Check if the line starts with a '#' character. These lines will be ignored
        match = re.match("^#",line)

        #This strips whitespace and splits line by ':' . This is done to separate the line into fields such as username, password etc
        fields = line.strip().split(':')

        #This if checks if the line either starts with a '#' or if the fields do not equal 5.
        # The prior lines is important because ^ the fields variable is declare and the .split determine how fields are determined

        if match or len(fields) != 5:
            continue

        #The next three lines take the split up fields and assign them variables
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #The split is happening here because a user can have multiple groups and groups are separated using ',' in the input file
        groups = fields[4].split(',')

        #The point of the next print statement is to display to the user the name of the user being created 
        print("==> Creating account for %s..." % (username))
        #stores the command that will be used to create the user (this is the format we use in terminal)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #if uncommented os.system will communicate the command with the os and create the user
        print (cmd) 
        os.system(cmd)

        #the print statement displays that a password is being for username, this is a verification step and can be used for debugging purposes
        print("==> Setting the password for %s..." % (username))
        #stores the command to set the password for the user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #The first time I ran this, I DID NOT uncomment os.system(cmd) because I wanted to make sure the code worked. Then i uncommented
        #add parantheses to the print ststament
        print (cmd)
        os.system(cmd)

        for group in groups:
            #the if statement check for '-'. this character indicates that the group is not assigned. if there no '-' then the group that is there will be assigned to the user
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print (cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

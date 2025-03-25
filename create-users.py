#!/usr/bin/python3

# INET4031
# Zuhur Hashi
# Data Created: 03/25/2025
# Date Last Modified: 03/25/2025

# identify what each of these imports is for: imports modules, os is used to execute system commands, re- used for regular expression matching, sys - provides access to system input and output 
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:
	#checks if the line is a comment or not 
        match = re.match("^#",line)

        #splits the line by where there is ':'
        fields = line.strip().split(':')

        #REPLACE THESE COMMENTS with a single comment describing the logic of the IF 
        #what would an appropriate comment be for describing what this IF statement is checking for?
        #what happens if the IF statement evaluates to true?
        #how does this IF statement rely on wat happened in the prior two lines of code? The match and fields lines.
        #the code clearly shows that the variables match and the length of fields is being checked for being != 5  so why is it doing that?
	#the if statement skips procressing if the line is a comment or does not contain exactly 5 fields

        if match or len(fields) != 5:
            continue

        # extracts user info from fields, the username is info at the index 0 and the password at index 1,
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #it is being split so that it can handle multiple groups per user
        groups = fields[4].split(',')

        #the purpose of the print statement is to confirm that the account is being created for the 'username'
        print("==> Creating account for %s..." % (username))
        #construct the command to create a user with a disabled password and GECOS information
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
	#if uncommented, this command will create a new user account
       	print cmd
        os.system(cmd)

        #the purpose of this print statement is to indicate the start of password setup
        print("==> Setting the password for %s..." % (username))
        #consreuct system command to set the user's password securely using echo and passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

	# the first time I run the code I should uncomment the next line. If uncommented, it will execute the command to set the user's password 
       	print cmd
        os.system(cmd)

        for group in groups:
            #if the group field is not '-', it assigns the user to the specified group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group),
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()

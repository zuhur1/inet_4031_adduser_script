#!/usr/bin/python3
# Importing modules
import os
import re
import sys

# Function that will process the create-users.input file and either dry run or actual based on user input
def process_user_file(filename, dry_run):
    with open(filename, 'r') as file:
        # Opens the file
        for line in file:
            # Goes through the lines in the file, strips them of whitespace and newlines 
            line = line.strip()
            if not line or line.startswith('#'):
                # Checks to see if the line is a comment or not
                if dry_run:
                    print(f"Skipping line: {line}")
                continue
                # If the user chose dry-run mode, it will print that the line is skipped and displays the line

            fields = line.split(':')
            # Line is broken up by where there is ':', which separates based on username, password, last name, first name, and group

            if len(fields) < 5:
                # Checks that there are at least 5 fields, all the necessary fields
                if dry_run:
                    # If in dry-run mode, it will print "not enough fields"
                    print(f"Error: Line does not have enough fields - {line}")
                continue

            username, fullname, password = fields[:3]
            command = f"sudo useradd -m -c \"{fullname}\" -p {password} {username}"

            if dry_run:
                print(f"Dry-run: Would execute: {command}")
            else:
                os.system(command)
                print(f"User {username} created successfully.")

if __name__ == "__main__":
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().upper()
    # Takes user input for dry-run or actual run
    dry_run = dry_run_input == 'Y'
    process_user_file("create-users.input", dry_run)
    # Runs the process_user_file function with whatever dry-run answer the user stated AND the create-users.input that contains user input info

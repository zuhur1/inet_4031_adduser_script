# INET4031 Add Users Script and User List

## Program Description

The Add Users Script is designed to automate the process of adding users to your system, saving you the hassle of manually typing useradd commands. 
Typically, a user would type the following into their terminal to add users: 
sudo useradd -m -c "Full Name" -p "password" username
However, the create-users.py and create-users2.py make the process easier by creating a whole file of users at the same time rather than individually


## Program User Operation
To get the create-users.py running script running, follow the following steps: 
1. ensure that you are in the correct directory
2. use this syntax to run $./create-users.py <'the name of the file contains user info'
However, for the create-users2.py file, you would have to edit the file
1. use sudo nano create-users2.py to edit the file
2. navigate to follow lines: 
if __name__ == "__main__":
	process_user_file("create-users.input", dry_run)
3. change the file to the file you would like to take user info from. the default right now is "create-users.input"
4. click control + o, to save. Click return key. Finally control + X to navigate out of editing
 
### Input File Format
In order for the program to work, it is import to understand how to format your input file correctly. 
Here is the anticipated formatt: 
username:password:lastname:firstname:group1,group2,...

If you would like to skip a line in the input file, make sure to put a # at the start of the line
example: #user08:pass08:Last08:First08:group01

###Command Execution
To run the script, first make it executable by running: 
chmod +x create-users.py
Next run it by: 
./create-users.py < create-users.input 

### "Dry Run"
if you want to check everything before actually adding a user to the system, you can use dry-run mode. 
Dry run mode will print comments of what WOULD happen if you choose to not run dry run


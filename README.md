# How to Run Kin Code Challenge:

Dependencies:

Python 3 or higher

Instructions:

1. After forking the project you'll see a folder called 'kin'. 
2. Inside the 'kin' folder are several files including:

	- books.csv
	- librarysystem.py
	- README

Please note, this is a Command Line Interface program

3. The books.csv file will act as a lightweight database and holds the records of books.
4. The librarysystem.py file is a Python file will all the code to run the program
5. The README has all the instructions to run the code for the project
6. To run the code on a Mac download the 'kin' folder to your Desktop, making sure the 3 aforementioned files are in that folder
7. Cd into the folder by doing the following: $ cd Desktop/kin
8. Then run the program by running the library system.py file by doing this: $ python3 librarysystem.py
9. The output will be displayed in the console. You should see the following in the console:

Total Pages Read: 1402
By Category:
     Philosophy & Psychology:1257
     Applied Science:145

10. To run a different csv file do the following:
    A. Create and add a csv file to the kin folder
    B. Open the librarysystem.py file and in the function called 'create_list_of_dicts' change the first line: 'with open("books.csv") as csv_file' to point to the new csv file. 
    C. Save the file
    D. Run with the program
 

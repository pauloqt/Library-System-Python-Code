import csv

from tkinter import messagebox

borrowerList = []     #Initializing an empty list of Cborrower objects          datasruct: list

class CBorrower:
    # Object Constructor
    def __init__(self, name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed, borrowedborrowers = []) :
        self.name = name
        self.TUP_ID = TUP_ID
        self.password = password
        self.yearSection = yearSection
        self.contactNum = contactNum
        self.email = email
        self.noOfBorrowed = noOfBorrowed
        self.borrowedborrowers = []

    #lahat ng mga naka-indent dito ay kasama sa Cborrower Class

#######################  METHODS   ##############################################
def getInfoBorrower():
    name = input("Enter your name: ")
    TUP_ID = input("Enter your TUP_ID: ")
    password = input("Enter your password: ")
    yearSection = input("Enter your Year and Section: ")
    contactNum = input("Enter your contact number: ")
    email = input("Enter your email: ")

    if locateBorrower(TUP_ID) >= 0:               #if existing na sa borrowerList
        messagebox.showerror("REGISTRATION ", "THE STUDENT ALREADY EXISTS IN THE RECORD")
    elif not checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):    #if di complete fields
        messagebox.showerror("REGISTRATION", "PLEASE FILL IN ALL THE FIELDS")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="Confirmation",
            message="DO YOU WANT TO PROCEED?",
            icon=messagebox.QUESTION

        )
        if response:                        #if yes
            borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed=0)
            addBorrower(borrower)



def addBorrower(borrower):
    # Find the index to insert the borrower alphabetically based on the name
    index = 0
    while index < len(borrowerList) and borrower.name > borrowerList[index].name:
        index += 1
    # Insert the borrower at the determined index
    borrowerList.insert(index, borrower)
    #Note: Pakitawag ang saveBorrower() after mag-add ng borrower sa main.

def locateBorrower(TUP_ID):
                for i in range(len(borrowerList)):  # loop through the borrowerList
                    if borrowerList[i].TUP_ID == TUP_ID:  # if nahanap, return index, else return -1
                        return i

                return -1

def displayBorrower():
    for borrower in borrowerList:
        print(borrower.name +" "+ borrower.TUP_ID +" "+ borrower.yearSection +" " + borrower.contactNum + " " +borrower.email)


def changePass():
        index = 0
        tries = 3
        flag = 0

        while tries > 0:
            currPass = input("Enter your old password: ")

            if borrowerList[index].password != currPass:  # if password doesn't match the current password
                print("PASSWORD DIDN'T MATCH!")
                tries -= 1
                print("YOU HAVE", tries, "TRIES LEFT.")
                print()
            else:
                break

        if tries == 0:
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
            print()
            return flag

        newPass = input("Enter your new password: ")
        rePass = input("Re-enter your new password: ")

        if rePass != newPass:  # if the re-entered password doesn't match the new password
            print("PASSWORD DIDN'T MATCH!")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()
        else:
            print("CHANGE PASSWORD SUCCESSFULLY!")
            flag = 1


        if tries == 0:
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
            print()

        return flag

def updateBorrower():
    TUP_ID = input("ENTER TUP ID: ")
    index = locateBorrower(TUP_ID)

    if index >= 0:  # if existing ang STUDENT
        print("[1] NAME\n[2] TUP ID\n[3] YEAR AND SECTION\n[4]CONTACT NUMBER\n[5] EMAIL\n[6] CHANGE PASSWORD\n")
        attributeChoice = int(input("ENTER ATTRIBUTE TO UPDATE: "))

        print("ENTER THE UPDATED INFORMATION: ")
        if attributeChoice > 7:
            updatedInfoInt = int(input())
        else:
            updatedInfo = input()

        # INSERT ASK IF CONFIRM UPDATING

        if attributeChoice == 1:
            borrowerList[index].name = updatedInfo
        elif attributeChoice == 2:
            borrowerList[index].TUP_ID = updatedInfo
        elif attributeChoice == 3:
            borrowerList[index].yearSection = updatedInfo
        elif attributeChoice == 4:
            borrowerList[index].contactNum = updatedInfo
        elif attributeChoice == 5:
            borrowerList[index].email = updatedInfo
        elif attributeChoice == 6:
            changePass()

        response = messagebox.askyesno(  # creates a yes or no message box
                title="Confirmation",
                message="ARE YOU SURE TO UPDATE THE INFORMATION?",
                icon=messagebox.QUESTION
            )

        if response:
            saveBorrower()
            messagebox.showerror("UPDATE BORROWER INFORMATION ", "UPDATED SUCCESSFULLY!")
        else:
            return

    else:
        print("STUDENT NOT FOUND!")

#login
def logInBorrower():
    tries = 3
    flag = 0

    while tries > 0 and flag == 0:
        print("LOG IN STUDENT")
        enteredID = input("TUP ID (Ex. 123456): TUP-M ")
        enteredPass = input("PASSWORD: ")

        index = locateBorrower(enteredID)

        if index >= 0 and enteredPass == borrowerList[index].password:
            print("LOG IN SUCCESSFULLY!")
            flag = 1
            saveBorrower()
            # loggedInIndex = index
        else:
            print("INCORRECT TUP ID OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()

    if tries == 0:
        print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
        print()

    return flag


def logInAdmin():
    tries = 3
    flag = 0

    while tries > 0 and flag == 0:
        print("LOG IN ADMIN")
        enteredUsername = input("Username: ")
        enteredPass = input("PASSWORD: ")

        if enteredUsername == "ADMIN" and enteredPass == "1234":
            print("LOG IN SUCCESSFULLY!")
            flag = 1
            # PUNTA SA STUDENT PORTAL
            # loggedInIndex = index
        else:
            print("INCORRECT USERNAME OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()

    if tries == 0:
        print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
        print()

    return flag

def searchBorrower():
    print("Select an attribute for searching")
    print("[1] Name")
    print("[2] TUP ID")
    print("[3] Year and Section")
    print("[4] Contact Number")
    print("[5] Email")
    choice = int(input("Enter search category: "))

    keyword = input("Enter the search keyword or substring: ")

    foundMatch = False
    for borrower in borrowerList:
        attributeValue = ""
        if choice == 1:
            attributeValue = borrower.name()
        elif choice == 2:
            attributeValue = borrower.TUP_ID()
        elif choice == 3:
            attributeValue = borrower.yearSection()
        elif choice == 4:
            attributeValue = borrower.contactNum()
        elif choice == 5:
            attributeValue = borrower.email()

        if keyword.lower() in attributeValue.lower():
            print(borrower.name(), "\t", borrower.TUP_ID(), "\t", borrower.yearSection(), "\t", borrower.contactNum(), "\t", borrower.email())
            foundMatch = True

    if not foundMatch:
        print("NO MATCHING BORROWERS FOUND.")

def saveBorrower():
    filename = "borrowerRecords.csv"  # Specify the filename for the CSV file

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object

        # Write the header row
        writer.writerow(["Name", "TUP_ID", "Password", "Year and Section", "Contact Number", "Email","No. of Borrowed Books", "Borrowed Book(s)"])

        # Write each borrower's data row
        for borrower in borrowerList:
            writer.writerow([borrower.name, borrower.TUP_ID, borrower.password, borrower.yearSection,
                             borrower.contactNum, borrower.email, borrower.noOfBorrowed])

def retrieveBorrower():

    with open("borrowerRecords.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader objectatego
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the data from each row and create a CBorrower object
            name = row[0]
            TUP_ID = row[1]
            password = row[2]
            yearSection = row[3]
            contactNum = row[4]
            email = row[5]
            noOfBorrowed = row [6]
            #borrowedborrowers [0] = row[6]


            #create an object of the retrieved borrower
            borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed=0)#noOfBorrowed,  borrowedborrowers
            #add borrower in the borrowerList
            addBorrower(borrower)


def checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):

    if (name == "" or
        TUP_ID == "" or
        password == "" or
        yearSection == "" or
        contactNum == "" or
        email == "" ):
        return False
    else:
        return True

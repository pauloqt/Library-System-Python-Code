import csv
from tkinter import messagebox

borrowerList = []     #Initializing an empty list of Cborrower objects          datasruct: list
loggedInAccount = 0     #once na nakapag-log in, di na magpapa-enter uli ng TUP_ID, ito na yung index na gagamitin

class CBorrower:
    # Object Constructor
    def __init__(self, name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed):
        self.name = name
        self.TUP_ID = TUP_ID
        self.password = password
        self.yearSection = yearSection
        self.contactNum = contactNum
        self.email = email
        self.noOfBorrowed = noOfBorrowed

    #lahat ng mga naka-indent dito ay kasama sa Cborrower Class

#######################  METHODS   ##############################################
def getInfoBorrower():
    print("ENTER COMPLETE INFORMATION BELOW")
    TUP_ID = input("Enter your TUP_ID: ")
    name = input("Enter your name: ")
    yearSection = input("Enter your Year and Section: ")
    contactNum = input("Enter your contact number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    repassword = input("Re-enter password: ")
    noOfBorrowed = 0

    if locateBorrower(TUP_ID) >= 0:               #if existing na sa borrowerList
        messagebox.showerror("REGISTRATION ", "YOUR TUP ID IS ALREADY REGISTERED")
    elif not checkBorrowerFields(name, TUP_ID, password, yearSection, contactNum, email):    #if di complete fields
        messagebox.showerror("REGISTRATION", "PLEASE FILL IN ALL THE FIELDS")
    elif len(TUP_ID) != 6:
        messagebox.showerror("REGISTRATION", "TUP ID MUST BE 6 DIGITS LONG")
    elif password != repassword:
        messagebox.showerror("REGISTRATION", "PASSWORD DIDN'T MATCH")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="REGISTRATION",
            message="DO YOU WANT TO SUBMIT YOUR REGISTRATION?",
            icon=messagebox.QUESTION

        )
        if response:                        #if yes
            borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed)
            addBorrower(borrower)
            saveBorrower()
            messagebox.showinfo("REGISTRATION", "YOUR ACCOUNT IS SUCCESSFULLY REGISTERED!")

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
        print(borrower.name +" "+ borrower.TUP_ID +" "+ borrower.yearSection +" " + borrower.contactNum + " " +borrower.email + " " +str(borrower.noOfBorrowed))
        displayBorrowedBook(borrower.TUP_ID)

def displayBorrowedBook(TUP_ID):
    from CTransaction import transactionList
    i=0

    bookBorrowed=["", "", ""]
    for transaction in transactionList:
        if transaction.TUP_ID == TUP_ID and transaction.status == "TO RETURN":
            bookBorrowed[i] = transaction.title
            i=i+1

    print(bookBorrowed[2] + bookBorrowed[1] + bookBorrowed[0])



changePassTries = 3
def changePass():
        global changePassTries

        #TUP_ID = input("Enter your TUP ID:")
        currentPass = input("Enter current password: ")
        newPass = input("Enter new password: ")
        reEnterPass = input("Re-enter new password: ")

        index = loggedInAccount

        if index < 0:
            messagebox.showerror("CHANGE PASSWORD", "ACCOUNT NOT FOUND")
        elif currentPass != borrowerList[index].password:
            messagebox.showerror("CHANGE PASSWORD", "INCORRECT CURRENT PASSWORD")
            changePassTries -= 1
        elif newPass != reEnterPass:
            messagebox.showerror("CHANGE PASSWORD", "NEW PASSWORD DOESN'T MATCH THE RE-ENTERED PASSWORD!")
        elif currentPass == newPass:
            messagebox.showerror("CHANGE PASSWORD", "YOU CAN'T CHANGE IT TO YOUR CURRENT PASSWORD")
        else:
            response = messagebox.askyesno(  # creates a yes or no message box
                title="CHANGE PASSWORD",
                message="CONFIRM CHANGES?",
                icon=messagebox.QUESTION
            )
            if response:
                borrowerList[index].password = newPass      #set password to new pass
                saveBorrower()
                messagebox.showinfo("CHANGE PASSWORD", "YOUR PASSWORD HAS BEEN SUCCESSFULLY CHANGED!")
                #CLEAR FIELDS

        if changePassTries == 0:
            messagebox.showerror("CHANGE PASSWORD", "YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES. TRY AGAIN LATER")
            #EXIT FRAME

def updateBorrower():
    #TUP_ID = input("ENTER TUP ID: ")
    index = loggedInAccount

    if index >= 0:  # if existing ang STUDENT
        print("[1] NAME\n[2] TUP ID\n[3] YEAR AND SECTION\n[4]CONTACT NUMBER\n[5] EMAIL\n[6] CHANGE PASSWORD\n")
        attributeChoice = int(input("ENTER ATTRIBUTE TO UPDATE: "))

        print("ENTER THE UPDATED INFORMATION: ")
        if attributeChoice > 7:
            updatedInfoInt = int(input())
        else:
            updatedInfo = input()

        #CONFIRM UPDATE
        response = messagebox.askyesno(  # creates a yes or no message box
            title="Confirmation",
            message="ARE YOU SURE TO UPDATE THE INFORMATION?",
            icon=messagebox.QUESTION
        )

        if response:
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

            saveBorrower()
            messagebox.showinfo("UPDATE BORROWER INFORMATION ", "UPDATED SUCCESSFULLY!")

    else:
        print("STUDENT NOT FOUND!")

#login
def logInBorrower():
    tries = 3
    exit = False

    while tries > 0 and exit == False:
        print("LOG IN STUDENT")
        enteredID = input("TUP ID (Ex. 123456): TUP-M ")
        enteredPass = input("PASSWORD: ")

        index = locateBorrower(enteredID)

        if index >= 0 and enteredPass == borrowerList[index].password:
            #messagebox.showinfo("LOG IN ", "LOG IN SUCCESSFULLY!")
            saveBorrower()
            global loggedInAccount      #accessing global variable
            loggedInAccount = index     #modifying global variable
            exit = True

        elif enteredID == "ADMIN" and enteredPass == "1234":
            messagebox.showinfo("LOG IN ", "LOG IN SUCCESSFULLY!")
            exit = True

        elif index <0:
            messagebox.showerror("LOG IN", "YOUR TUP ID IS NOT YET REGISTERED")

        else:
            messagebox.showerror("LOG IN", "INCORRECT TUP ID OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")

        if tries == 0:
            messagebox.showerror("LOG IN", "YOU HAVE REACHED THE MAXIMUM NUMBER OF ATTEMPTS.\nTRY AGAIN LATER")
            exit = True

def logInAdmin():
    tries = 3
    exit = False

    while tries > 0 and exit == False:
        print("LOG IN ADMIN")
        enteredUsername = input("Username: ")
        enteredPass = input("PASSWORD: ")

        if enteredUsername == "ADMIN" and enteredPass == "1234":
            print("LOG IN SUCCESSFULLY!")
            exit = True
            # PUNTA SA STUDENT PORTAL
            # loggedInIndex = index
        else:
            print("INCORRECT USERNAME OR PASSWORD")
            tries -= 1
            print("YOU HAVE", tries, "TRIES LEFT.")
            print()

        if tries == 0:
            print("YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIES.")
            exit = True

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
            attributeValue = borrower.name
        elif choice == 2:
            attributeValue = borrower.TUP_ID
        elif choice == 3:
            attributeValue = borrower.yearSection
        elif choice == 4:
            attributeValue = borrower.contactNum
        elif choice == 5:
            attributeValue = borrower.email
        else:
            attributeValue = borrower.TUP_ID

        if keyword.lower() in attributeValue.lower():
            print(borrower.name, "\t", borrower.TUP_ID, "\t", borrower.yearSection, "\t", borrower.contactNum, "\t", borrower.email)
            foundMatch = True

    if not foundMatch:
        messagebox.showinfo("SEARCH BORROWER", "NO MATCH FOUND ")

def saveBorrower():
    filename = "borrowerRecords.csv"  # Specify the filename for the CSV file

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object

        # Write the header row
        writer.writerow(["TUP_ID", "Password", "Year and Section", "Contact Number", "Email","No. of Borrowed Books"])

        # Write each borrower's data row
        for borrower in borrowerList:
            #ENCRYPTED - encrypts every variable, then write it in the file
            writer.writerow([encrypt(borrower.name), encrypt(borrower.TUP_ID), encrypt(borrower.password), encrypt(borrower.yearSection),
                             encrypt(borrower.contactNum), encrypt(borrower.email), encrypt(str(borrower.noOfBorrowed))])
            #NOT ENCRYPTED
            #writer.writerow([borrower.name, borrower.TUP_ID, borrower.password, borrower.yearSection,
            #                 borrower.contactNum, borrower.email, borrower.noOfBorrowed])

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

            #create an object of the retrieved borrower
            #DECRYPTYED
            borrower = CBorrower(decrypt(name), decrypt(TUP_ID), decrypt(password), decrypt(yearSection), decrypt(contactNum), decrypt(email), decrypt(noOfBorrowed))

            #NOT DECRYPTED
            #borrower = CBorrower(name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed)# borrowedBook

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

def encrypt(text):
    encrypted = ""  # Initialize an empty string to store the encrypted text
    for char in text:  # Iterate through each character in the input text
        encrypted += chr(ord(char) + 29)  # Encrypt the character by adding 29 to its ASCII value
    return encrypted  # Return the encrypted text

def decrypt(text):
    decrypted = ""  # Initialize an empty string to store the decrypted text
    for char in text:  # Iterate through each character in the input text
        decrypted += chr(ord(char) - 29)  # Decrypt the character by subtracting 29 from its ASCII value
    return decrypted  # Return the decrypted text


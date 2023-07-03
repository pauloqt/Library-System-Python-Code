import csv
from tkinter import messagebox
from CBorrower import borrowerList
from CBook import bookList
from CBorrower import loggedInAccount
import CBorrower
import CBook

transactionList = []       #Initializing an empty list of CTransaction objects          datasruct: list

class CTransaction:
    # Object Constructor
    def __init__(self, title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine):
        self.title = title
        self.ISBN = ISBN
        self.TUP_ID = TUP_ID
        self.dateBorrowed = dateBorrowed
        self.dateToReturn = dateToReturn
        self.status = status
        self.refNum = refNum
        self.borrower = borrower
        self.author = author
        self.librarian = librarian
        self.fine = fine


    #lahat ng mga naka-indent dito ay kasama sa CTransaction Class

#######################  METHODS   ##############################################
def getInfoTransaction():
    print("ENTER COMPLETE INFORMATION BELOW")
    loggedInAccount= CBorrower.loggedInAccount      #Stores the index of loggedInAccount

    TUP_ID = borrowerList[loggedInAccount].TUP_ID
    borrower = borrowerList[loggedInAccount].name
    ISBN = input("ENTER ISBN OF THE BOOK: ")
    index = CBook.locateBook(ISBN)
    title = bookList[index].title
    author = bookList[index].author
    dateBorrowed = input("ENTER DATE BORROWED: ")
    dateToReturn = input("ENTER DATE TO RETURN: ")
    librarian = "MS. LAICA YGOT"
    fine = "0"
    refNum = "0000"
    status = "TO APPROVE"

    if index < 0:
        messagebox.showerror("BORROW BOOK", "BOOK DOES NOT EXIST")
    elif borrowerList[loggedInAccount].noOfBorrowed == 3:
        messagebox.showerror("BORROW BOOK", "YOU CAN ONLY BORROW MAXIMUM OF 3 BOOKS")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="Confirmation",
            message="DO YOU WANT TO PROCEED BORROWING?",
            icon=messagebox.QUESTION
        )
        if response:                        #if yes
            transaction = CTransaction(title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine)
            addTransaction(transaction)
           # saveTransaction()
            messagebox.showinfo("BORROW BOOK", "TRANSACTION SUCCESSFULLY SUBMITTED. PROCEED TO THE LIBRARIAN TO APPROVE TRANSACTION")

def addTransaction(transaction):
    #Add each transaction at the beginning of the list
    index = 0

    # Insert the transaction at the determined index
    transactionList.insert(index, transaction)
    #Note: Pakitawag ang savetransaction() after mag-add ng transaction sa main.


def locateTransaction(refNum):
                for i in range(len(transactionList)):  # loop through the transactionList
                    if transactionList[i].refNum == refNum:  # if nahanap, return index, else return -1
                        return i

                return -1

def displayTransaction():
    for transaction in transactionList:
        print(transaction.title +" "+ transaction.ISBN +" "+ transaction.TUP_ID +" " + transaction.dateBorrowed + " " + transaction.dateToReturn +" "+ transaction.status +" "+ transaction.refNum +" "+ transaction.borrower +" "+ transaction.author +" "+ transaction.librarian +" "+ transaction.fine)

def updateTransaction():
    refNum = input("ENTER THE REFERENCE NUMBER OF THE TRANSACTION: ")
    index = locateTransaction(refNum)

    if index >= 0:
        print("[1] TITLE \n[2] ISBN \n[3] TUP ID\n[4] DATE BORROWED\n[5] DATE TO RETURN\n[6] STATUS\n[7] REFERENCE NUMBER\n[8] BORROWER\n[9] AUTHOR\n[10] LIBRARIAN \n[11] FINE")
        attributeChoice = int(input("ENTER ATTRIBUTE TO UPDATE: "))

        print("ENTER THE UPDATED INFORMATION: ")
        updatedInfo = input()

        # INSERT ASK IF CONFIRM UPDATING

        if attributeChoice == 1:
            transactionList[index].title = updatedInfo
        elif attributeChoice == 2:
            transactionList[index].ISBN = updatedInfo
        elif attributeChoice == 3:
            transactionList[index].TUP_ID = updatedInfo
        elif attributeChoice == 4:
            transactionList[index].dateBorrowed = updatedInfo
        elif attributeChoice == 5:
            transactionList[index].dateToReturn = updatedInfo
        elif attributeChoice == 6:
            transactionList[index].status = updatedInfo
        elif attributeChoice == 7:
            transactionList[index].refNum = updatedInfo
        elif attributeChoice == 8:
            transactionList[index].borrower = updatedInfo
        elif attributeChoice == 9:
            transactionList[index].author = updatedInfo
        elif attributeChoice == 10:
            transactionList[index].librarian = updatedInfo
        elif attributeChoice == 11:
            transactionList[index].fine = updatedInfo

        saveTransaction()

    else:
        print("TRANSACTION NOT FOUND!")

def deleteTransaction():
    refNum = input("Enter the reference No. of the transaction you want to delete: ")
    index = locateTransaction(refNum)
    if index >= 0:
        #ASK CONFIRMATION
        choice = input("Are you sure to delete the information? (Y/N): ")
        if choice.upper() == "Y":
            deleted_transaction = transactionList.pop(index)
            print(deleted_transaction.title + " is deleted successfully!")
            saveTransaction()
        else:
            print("Transaction deletion canceled.")
    else:
        print("Transaction not found!")

def searchTransaction():
    print("Select an attribute for searching")
    print("[1] Title")
    print("[2] ISBN")
    print("[3] TUP ID")
    print("[4] Date Borrowed")
    print("[5] Date To Return")
    print("[6] Status")
    choice = int(input("Enter search category: "))

    keyword = input("Enter the search keyword or substring: ")

    foundMatch = False
    for transaction in transactionList:
        attributeValue = ""
        if choice == 1:
            attributeValue = transaction.title
        elif choice == 2:
            attributeValue = transaction.ISBN
        elif choice == 3:
            attributeValue = transaction.TUP_ID
        elif choice == 4:
            attributeValue = transaction.dateBorrowed
        elif choice == 5:
            attributeValue = transaction.dateToReturn
        else:
            attributeValue = transaction.fine

        if keyword.lower() in attributeValue.lower():
            print(transaction.title +" "+ transaction.ISBN +" "+ transaction.TUP_ID +" " + transaction.dateBorrowed + " " + transaction.dateToReturn +" "+ transaction.status +" "+ transaction.refNum +" "+ transaction.borrower +" "+ transaction.author +" "+ transaction.librarian +" "+ transaction.fine)
            foundMatch = True

    if not foundMatch:
        messagebox.showinfo("SEARCH TRANSACTION", "NO MATCH FOUND ")


def saveTransaction():
    filename = "transactionRecords.csv"  # Specify the filename for the CSV file

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object

        # Write the header row
        writer.writerow(["Title", "Author", "ISBN", "Edition", "Year Published", "Material", "Category", "Shelf No.", "Total Stocks", "No. of Borrower"])

        # Write each transaction's data row
        for transaction in transactionList:
            writer.writerow([transaction.title, transaction.ISBN, transaction.TUP_ID, transaction.dateBorrowed, transaction.dateToReturn, transaction.status, transaction.refNum, transaction.borrower, transaction.author, transaction.librarian, transaction.fine])

def retrieveTransaction():

    with open("transactionRecords.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader objectatego
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the data from each row and create a CTransaction object
            title = row[0]
            ISBN = row[1]
            TUP_ID = row[2]
            dateBorrowed = row[3]
            dateToReturn = row[4]
            status = row[5]
            refNum = row[6]
            borrower = row[7]
            author = row[8]
            librarian = row[9]
            fine = row[10]

            #create an object of the retrieved transaction
            transaction = CTransaction(title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine)
            #add transaction at the end of the transactionList
            transactionList.append(transaction)

def checkTransactionFields(title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine):

    if (title == "" or
        ISBN == "" or
        TUP_ID == "" or
        dateBorrowed == "" or
        dateToReturn == "" or
        status == "" or
        refNum == "" or
        borrower == "" or
        author == "" or
        librarian == "" or
        fine == ""):

        return False
    else:
        return True


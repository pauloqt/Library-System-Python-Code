import csv
import random
import tkinter as tk
import tkcalendar as tkcalendar
from datetime import date
from datetime import datetime, timedelta
from tkcalendar import DateEntry
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

indexBook = 0
indexBorrower = 0
def getInfoTransaction():
    global indexBook
    global indexBorrower

    root = tk.Tk()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)
    # Set the background color

    ISBN = input("ENTER ISBN: ")
    indexBook = CBook.locateBook(ISBN)                #kinuha index ng book na hihiramin
    title = bookList[indexBook].title
    author = bookList[indexBook].author

    indexBorrower = CBorrower.loggedInAccount        #kinuha index ng currently account logged in.
    TUP_ID = borrowerList[indexBorrower].TUP_ID
    borrower = borrowerList[indexBorrower].name
    yearSection = borrowerList[indexBorrower].yearSection

    borrower = borrowerList[indexBorrower].name
    # Create labels and entry fields
    tk.Label(main_frame, text="\t\tTUP READS\t\t").grid(row=0, columnspan=2)
    tk.Label(main_frame, text="\t\tWELCOME TO TUP READS, {}\t\t".format(borrower)) \
        .grid(row=1, columnspan=2)

    # Create and pack the label for TUP ID
    TUP_ID_label = tk.Label(root, text="TUP ID:")
    TUP_ID_label.pack(padx=10, pady=10)
    # Create and pack the non-editable entry field for TUP ID
    TUP_ID_entry = tk.Entry(root, state="normal")  # set to editable
    TUP_ID_entry.insert(tk.END, TUP_ID)  # Insert the actual value
    TUP_ID_entry.pack(padx=10)
    TUP_ID_entry.config(state="disabled")  # Disable the entry field

    # Create and pack the label for YEAR AND SECTION
    yearSection_label = tk.Label(root, text="YEAR AND SECTION:")
    yearSection_label.pack(padx=10, pady=10)
    # Create and pack the non-editable entry field for YEAR AND SECTION
    yearSection_entry = tk.Entry(root, state="normal")  # set to editable
    yearSection_entry.insert(tk.END, yearSection)  # Insert the actual value
    yearSection_entry.pack(padx=10)
    yearSection_entry.config(state="disabled")  # Disable the entry field

    # Create and pack the label for TITLE
    title_label = tk.Label(root, text="BOOK TITLE:")
    title_label.pack(padx=10, pady=10)
    # Create and pack the non-editable entry field for YEAR AND SECTION
    title_entry = tk.Entry(root, state="normal")  # set to editable
    title_entry.insert(tk.END, title)  # Insert the actual value
    title_entry.pack(padx=10)
    title_entry.config(state="disabled")  # Disable the entry field

    # Create and pack the label for "DATE BORROWED"
    dateBorrowed_label = tk.Label(root, text="DATE BORROWED:")
    dateBorrowed_label.pack(padx=10, pady=10)
    today = date.today()
    # Create the date picker widget and pack it into the root window
   # dateBorrowed_entry = DateEntry(root, state="readonly")
    #today.pack(padx=10)
    dateBorrowed_entry = DateEntry(root, state="readonly")  # set to read-only
    dateBorrowed_entry.set_date(today)  # format the date as desired
    dateBorrowed_entry.pack(padx=10)
    dateBorrowed_entry.config(state="disabled")

    # Create and pack the label for "DATE BORROWED"
    dateToReturn_label = tk.Label(root, text="DATE TO BE RETURN:")
    dateToReturn_label.pack(padx=10, pady=10)

    # Create the date picker widget and pack it into the root window
    dateToReturn_entry = DateEntry(root, state="readonly")
    dateToReturn_entry.pack(padx=10)

    def submit():
        # Get values from other entry fields
        dateBorrowed = dateBorrowed_entry.get()
        dateToReturn = dateToReturn_entry.get()
        librarian = "MS. LAICA YGOT"
        refNum = generateReferenceNumber()
        status = "TO APPROVE"
        fine = "0"

        # ERRORS AND CONFIRMATION ...
        currentStock = int(bookList[indexBook].totalStocks) - int(bookList[indexBook].noOfBorrower)
        remainingDays = calculateRemainingDays(dateToReturn)

        if indexBook < 0:
            messagebox.showerror("BORROW BOOK", "BOOK DOES NOT EXIST")
        #INSERT IF WALANG SELECTED ROW
        elif currentStock < 1:
            messagebox.showerror("BORROW BOOK", "BOOK SELECTED IS OUT OF STOCK")
        elif int(borrowerList[indexBorrower].noOfBorrowed) >= 3:
            messagebox.showerror("BORROW BOOK", "YOU CAN ONLY BORROW MAXIMUM OF 3 BOOKS")
        elif remainingDays >7:
            messagebox.showerror("BORROW BOOK", "RETURN DATE MUST BE WITHIN 7 DAYS FROM THE DATE BORROWED")
        else:
            response = messagebox.askyesno(
                title="BORROW BOOK",
                message="DO YOU WANT TO PROCEED BORROWING?",
                icon=messagebox.QUESTION
            )
            if response:
                transaction = CTransaction(title, ISBN, TUP_ID, dateBorrowed, dateToReturn, status, refNum, borrower, author, librarian, fine)
                addTransaction(transaction)
                saveTransaction()
                bookList[indexBook].noOfBorrower = int(bookList[indexBook].noOfBorrower) + 1       #add noOfBorrower if nanghiram
                CBook.saveBook()
                borrowerList[indexBorrower].noOfBorrowed = int(borrowerList[indexBorrower].noOfBorrowed) + 1  # add noOfBorrowed if nanghiram
                CBorrower.saveBorrower()
                #INSERT SUMMARY OF TRANSACTION
                messagebox.showinfo("BORROW BOOK", "TRANSACTION SUCCESSFULLY SUBMITTED. PROCEED TO THE LIBRARIAN TO APPROVE TRANSACTION")
                root.destroy()  # Close the form after submitting
    def cancel():
        root.destroy()  # Close the form

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(padx=20, pady=10)  # Adjust the side and pady values as needed
    cancel_button = tk.Button(root, text="Cancel", command=cancel)
    cancel_button.pack(padx=40, pady=10)  # Adjust the side and pady values as needed

    root.mainloop()

def calculateRemainingDays(dateToReturn):
    today = date.today()
    dateToReturn = datetime.strptime(dateToReturn, "%m/%d/%y").date()

    remaining_days = (dateToReturn - today).days
    return remaining_days

def addTransaction(transaction):
    #Add each transaction at the beginning of the list
    index = 0

    # Insert the transaction at the index 0
    transactionList.insert(index, transaction)
    #Note: Pakitawag ang savetransaction() after mag-add ng transaction sa main.

def locateTransaction(refNum):
                for i in range(len(transactionList)):  # loop through the transactionList
                    if transactionList[i].refNum == refNum:  # if nahanap, return index, else return -1
                        return i

                return -1

def displayTransaction():
    for transaction in transactionList:
        remainingDays = str(calculateRemainingDays(transaction.dateToReturn))
        print(transaction.title +" "+ transaction.ISBN +" "+ transaction.TUP_ID +" " + transaction.dateBorrowed + " " + transaction.dateToReturn +" "+ transaction.status +" "+ transaction.refNum +" "+ transaction.borrower +" "+ transaction.author +" "+ transaction.librarian +" "+ transaction.fine +" "+ remainingDays)

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

def generateReferenceNumber():
    reference_number = random.randint(100000, 999999)
    return str(reference_number)

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

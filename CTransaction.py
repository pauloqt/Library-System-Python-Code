import csv
from tkinter import messagebox
from CBorrower import loggedInAccount
from CBorrower import borrowerList
from CBook import bookList
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
    # Find the index to insert the transaction alphabetically based on the name
    index = 0
    while index < len(transactionList) and transaction.title > transactionList[index].title:
        index += 1

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


import CBook
import CBorrower
import CTransaction



def adminPortal():
    while True:
        print("ADMIN PORTAL")
        print("[1] MANAGE BOOK RECORD")
        print("[2] MANAGE BORROWING RECORD")
        print("[3] MANAGE BORROWER RECORD")
        print("[4] BACK")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("MANAGE BOOK RECORD")
            bookMenu()
        elif choice == "2":
            print("MANAGE BORROWING RECORD")
            transactionMenu()
        elif choice == "3":
            print("MANAGE BORROWER RECORD")
            borrowerMenu()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def studentPortal():
    while True:
        print("STUDENT PORTAL")
        print("[1] DISPLAY ALL BOOKS")
        print("[2] SEARCH BOOKS")
        print("[3] BORROW BOOK")
        print("[4] CHANGE PASSWORD")
        print("[5] BACK")
        choice = input("Enter your choice: ")

        if choice == "1":
            CBook.displayBooks()
        elif choice == "2":
            pass
            CBook.searchBook()
        elif choice == "3":
            pass
            CTransaction.getInfoTransaction()
            CTransaction.saveTransaction()
        elif choice == "4":
            CBorrower.changePass()

        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def bookMenu():
    while True:
        print("[1] ADD BOOK")
        print("[2] DISPLAY BOOK")
        print("[3] UPDATE BOOK")
        print("[4] DELETE BOOK")
        print("[5] SEARCH BOOK")
        print("[6] BACK")
        choice = input("Enter your choice: ")
        if choice == "1":
            CBook.getInfoBook()
            CBook.saveBook()
        elif choice == "2":
            CBook.displayBooks()
            pass
        elif choice == "3":
            CBook.updateBook()
            pass
        elif choice == "4":
            CBook.deleteBook()
            pass
        elif choice == "5":
            CBook.searchBook()
            pass
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again.")


def borrowerMenu():
    while True:
        print("[1] DISPLAY BORROWER")
        print("[2] SEARCH BORROWER")
        print("[3] UPDATE BORROWER")
        print("[4] BACK")
        choice = input("Enter your choice: ")
        if choice == "1":
            CBorrower.displayBorrower()

        elif choice == "2":
           CBorrower.searchBorrower()

        elif choice == "3":
            CBorrower.updateBorrower()

        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def transactionMenu():
    while True:
        print("[1] UPDATE")
        print("[2] SEARCH")
        print("[3] DISPLAY")
        print("[4] BACK")
        choice = input("Enter your choice: ")
        if choice == "1":
            CTransaction.updateTransaction()
            pass
        elif choice == "2":
            CTransaction.searchTransaction()
            pass
        elif choice == "3":
            CTransaction.displayTransaction()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")


#MAIN

CBook.retrieveBook()
CBorrower.retrieveBorrower()
CTransaction.retrieveTransaction()

while True:
    print("MAIN SCREEN")
    print("[1] STUDENT PORTAL")
    print("[2] ADMIN PORTAL")
    print("[3] BACK")
    choice = input("ENTER CHOICE: ")  #input function always return a string, kaya need i-cast to int

    if choice == "1":
        print("[1] LOG IN")
        print("[2] REGISTER")
        logInOrRegister = input("ENTER CHOICE: ")
        if logInOrRegister == "1":
            CBorrower.logInBorrower()
            studentPortal()
        elif logInOrRegister == "2":
            CBorrower.getInfoBorrower()
            studentPortal()
        else:
            print("INVALID CHOICE")
    elif choice == "2":
        print()
        CBorrower.logInAdmin()
        adminPortal()
    elif choice == "3":
        pass    #walang gagawin
    else:
        print("INVALID CHOICE")


import csv
from tkinter import messagebox

bookList = []     #Initializing an empty list of CBook objects          datasruct: list

class CBook:
    # Object Constructor
    def __init__(self, title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks, noOfBorrower):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.edition = edition
        self.yearPublished = yearPublished
        self.material = material
        self.category = category
        self.shelfNo = shelfNo
        self.totalStocks = totalStocks
        self.noOfBorrower = noOfBorrower

    #lahat ng mga naka-indent dito ay kasama sa CBook Class

#######################  METHODS   ##############################################

def getInfoBook():
    title = input("Enter title: ")
    author = input("Enter author: ")
    ISBN = input("Enter ISBN: ")
    edition = input("Enter edition: ")
    yearPublished = input("Enter year published: ")
    material = input("Enter material: ")
    category = input("Enter category: ")
    shelfNo = int(input("Enter shelf no.: "))
    totalStocks = int(input("Enter total number of stocks: "))
    noOfBorrower = int(input("Enter total number of borrowers: "))

    if locateBook(ISBN) >= 0:               #if existing na sa bookList
        messagebox.showerror("ADD BOOK", "THE BOOK ALREADY EXISTS IN THE RECORD")
    elif not checkBookFields(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks):    #if di complete fields
        messagebox.showerror("ADD BOOK", "THE BOOK ALREADY EXISTS IN THE RECORD")
    else:
        response = messagebox.askyesno(    #creates a yes or no message box
            title="Confirmation",
            message="ARE YOU SURE TO ADD THIS BOOK IN THE RECORD?",
            icon=messagebox.QUESTION
        )
        if response:                        #if yes
            book = CBook(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks, noOfBorrower)
            addBook(book)

def addBook(book):
    # Find the index to insert the book alphabetically based on the title
    index = 0
    while index < len(bookList) and book.title > bookList[index].title:
        index += 1
    # Insert the book at the determined index
    bookList.insert(index, book)
    #Note: Pakitawag ang saveBook() after mag-add ng book sa main.

def displayBooks():
    for book in bookList:
        currentStock = str(int(book.totalStocks) - int(book.noOfBorrower))
        print(book.title +" "+ book.author +" "+ book.ISBN +" "+ book.edition +" "+ book.yearPublished +" "+ book.material +" "+ book.category +" "+ str(book.shelfNo) +" "+ str(book.totalStocks) +" "+ str(book.noOfBorrower) +" "+ currentStock)


def updateBook():
    ISBN = input("ENTER THE ISBN OF THE BOOK: ")
    index = locateBook(ISBN)

    if index >= 0:  # if existing ang book
        print("[1] TITLE\n[2] AUTHOR\n[3] ISBN\n[4] EDITION\n[5] YEAR PUBLISHED\n[6] MATERIAL\n[7] CATEGORY\n[8] SHELF NO.\n[9] TOTAL NO. OF STOCK\n[10] TOTAL NO. OF BORROWER")
        attributeChoice = int(input("ENTER ATTRIBUTE TO UPDATE: "))

        print("ENTER THE UPDATED INFORMATION: ")
        if attributeChoice > 7:
            updatedInfoInt = int(input())
        else:
            updatedInfo = input()

        # INSERT ASK IF CONFIRM UPDATING

        if attributeChoice == 1:
            bookList[index].title = updatedInfo
        elif attributeChoice == 2:
            bookList[index].author = updatedInfo
        elif attributeChoice == 3:
            bookList[index].ISBN = updatedInfo
        elif attributeChoice == 4:
            bookList[index].edition = updatedInfo
        elif attributeChoice == 5:
            bookList[index].yearPublished = updatedInfo
        elif attributeChoice == 6:
            bookList[index].material = updatedInfo
        elif attributeChoice == 7:
            bookList[index].category = updatedInfo
        elif attributeChoice == 8:
            bookList[index].shelfNo = updatedInfo
        elif attributeChoice == 9:
            bookList[index].totalStocks = updatedInfoInt
        elif attributeChoice == 10:
            bookList[index].noOfBorrower = updatedInfoInt

        saveBook()

    else:
        print("BOOK NOT FOUND!")

def deleteBook():
    ISBN = input("Enter the ISBN of the book you want to delete: ")
    index = locateBook(ISBN)
    if index >= 0:
        #ASK CONFIRMATION
        choice = input("Are you sure to delete the information? (Y/N): ")
        if choice.upper() == "Y":
            deleted_book = bookList.pop(index)
            print(deleted_book.title + " is deleted successfully!")
            saveBook()
        else:
            print("Book deletion canceled.")
    else:
        print("Book not found!")

def searchBook():
    print("Select an attribute for searching")
    print("[1] Title")
    print("[2] Author")
    print("[3] Year Published")
    print("[4] Material")
    print("[5] Category")
    choice = int(input("Enter search category: "))

    keyword = input("Enter the search keyword or substring: ")

    foundMatch = False
    for book in bookList:
        attributeValue = ""
        if choice == 1:
            attributeValue = book.title
        elif choice == 2:
            attributeValue = book.author
        elif choice == 3:
            attributeValue = book.yearPublished
        elif choice == 4:
            attributeValue = book.material
        elif choice == 5:
            attributeValue = book.category
        else:
            attributeValue = book.title

        if keyword.lower() in attributeValue.lower():
            currentStock = str(int(book.totalStocks) - int(book.noOfBorrower))
            print(book.title +" "+ book.author +" "+ book.ISBN +" "+ book.edition +" "+ book.yearPublished +" "+ book.material +" "+ book.category +" "+ str(book.shelfNo) +" "+ str(book.totalStocks) +" "+ str(book.noOfBorrower) +" "+ book.currentStock)
            foundMatch = True

    if not foundMatch:
        messagebox.showinfo("SEARCH BOOK", "NO MATCH FOUND ")


def locateBook(ISBN):
    for i in range(len(bookList)):      #loop through the bookList
        if bookList[i].ISBN == ISBN:    #if nahanap, return index, else return -1
            return i

    return -1

def saveBook():
    filename = "bookRecords.csv"  # Specify the filename for the CSV file

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object

        # Write the header row
        writer.writerow(["Title", "Author", "ISBN", "Edition", "Year Published", "Material", "Category", "Shelf No.", "Total Stocks", "No. of Borrower"])

        # Write each book's data row
        for book in bookList:
            writer.writerow([book.title, book.author, book.ISBN, book.edition, book.yearPublished, book.material, book.category, book.shelfNo, book.totalStocks, book.noOfBorrower])

def retrieveBook():

    with open("bookRecords.csv", "r") as csvfile:
        reader = csv.reader(csvfile)  # Create a CSV reader objectatego
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the data from each row and create a CBook object
            title = row[0]
            author = row[1]
            ISBN = row[2]
            edition = row[3]
            yearPublished = row[4]
            material = row[5]
            category = row[6]
            shelfNo = row[7]
            totalStocks = row[8]
            noOfBorrower = row[9]

            #create an object of the retrieved book
            book = CBook(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks,
                         noOfBorrower)
            #add book in the bookList
            addBook(book)

def checkBookFields(title, author, ISBN, edition, yearPublished, material, category, shelfNo, totalStocks):

    if (title == "" or
        author == "" or
        ISBN == "" or
        edition == "" or
        yearPublished == "" or
        material == "" or
        category == "" or
        shelfNo == 0 or
        totalStocks == 0):
        return False
    else:
        return True


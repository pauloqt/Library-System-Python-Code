borrowerList = []     #Initializing an empty list of CBook objects          datasruct: list

class CBorrower:
    # Object Constructor
    def __init__(self, name, TUP_ID, password, yearSection, contactNum, email, noOfBorrowed, borrowedBooks = []):
        self.name = name
        self.TUP_ID = TUP_ID
        self.password = password
        self.yearSection = yearSection
        self.contactNum = contactNum
        self.email = email
        self.noOfBorrowed = noOfBorrowed
        self.borrowedBooks = []

    #lahat ng mga naka-indent dito ay kasama sa CBook Class

#######################  METHODS   ##############################################


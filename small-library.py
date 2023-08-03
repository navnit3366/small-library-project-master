class books:
    def __init__(self):
        self.bookList = {}
    def readBooks(self, fileLocation):
        bookFile = 0
        try:
            bookFile = open(fileLocation)
        except:
            print("Can't open file")
            return False
        for i in bookFile:
            j = i.strip("\r\n").strip("\n")
            if not self.checkAvailability(j):
                self.bookList[j] = ""
        bookFile.close()
        return True
    def printBooks(self):
        print("Here's the list of books:")
        for i in self.bookList.keys():
            print(i)
    def checkAvailability(self, book):
        if book in self.bookList.keys():
            return self.bookList[book] == ""
        else:
            return False
    def borrow(self, user, book):
        if self.checkAvailability(book):
            self.bookList[book] = user
            return True
        else:
            return False
            #print("Your due is 2 weeks from now dear %s." % user)
    def returnBook(self, user, book):
        if self.bookList[book] in self.bookList.keys():
            self.bookList[book] = ""
            return True
            #print("Thanks dear %s. Please come again." % user)
        else:
            #print("No such book available")
            return False
    def printBorrowers(self):
        print("Here's the list of books and their corresponding borrowers:")
        for k in self.bookList.keys():
            if self.bookList[k] != "":
                print("Book %s is borrowed by %s" % (k, self.bookList[k]))
    def addBook(self, book):
        if not self.checkAvailability(book):
            self.bookList[book] = ""
            #print("Book added successfully")
            return True
        else:
            #print("Book already exists!")
            return False
class users:
    def __init__(self):
        self.userList= {}
    def readUsers(self, fileLocation):
        userFile = 0
        try:
            userFile = open(fileLocation)
        except:
            print("Can't open file")
            return False
        for i in userFile:
            j = i.strip("\r\n").strip("\n")
            if not self.checkExistance(j):
                self.userList[j] = []
        userFile.close()
        return True
    def printUsers(self):
        print("Here's the list of users:")
        for i in self.userList.keys():
            print(i)
    def checkExistance(self, user):
        return user in self.userList.keys()
    def borrow(self, user, book):
        if self.checkExistance(user):
            self.userList[user].append(book)
            return True
        else:
            return False
    def returnBook(self, user, book):
        if user in self.userList.keys():
            try:
                self.userList[user].remove(book)
                return True
            except:
                return False
        else:
            #print("No such user available")
            return False
    def printBorrowers(self):
        for k in self.userList.keys():
            if len(self.userList[k]) > 0:
                print("Here's the books borrowed by %s:" % k)
                for j in self.userList[k]:
                    print(j)
    def addUser(self, user):
        if not self.checkExistance(user):
            self.userList[user] = []
            #print("User added successfully.")
            return True
        else:
            #print("User already exists.")
            return False
# creating instance
u = users()
b = books()
if __name__ == '__main__':
    loop = True
    while (loop == True): # loop forever
        print("---Library---")
        print("1. Read book lists from file")
        print("2. Read user lists from file")
        print("3. Show user lists")
        print("4. Show book lists")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Show borrowed books from a user")
        print("8. Add new book")
        print("9. Add new user")
        print("10. Exit")
        userInput = list(map(int, input("\n\nYour choice: ")\
                             .strip("\r\n").strip("\n").split()))[0]
        # switch case
        if userInput == 1:
            location = input("Enter file name: ")
            if b.readBooks(location):
                print("Done.")
            else:
                print("Wrong input")
        elif userInput == 2:
            location = input("Enter file name: ")
            if u.readUsers(location):
                print("Done.")
            else:
                print("Wrong input")
        elif userInput == 3:
            u.printUsers()
        elif userInput == 4:
            b.printBooks()
        elif userInput == 5:
            u1 = input("Enter the name of user: ")
            b1 = input("Enter the name of book: ")
            if u.borrow(u1, b1) and b.borrow(u1, b1):
                print("Book's available dear %s." % u1)
                print("Your due is 2 weeks from now.")
            else:
                print("Sorry!")
        elif userInput == 6:
            u1 = input("Enter the name of user: ")
            b1 = input("Enter the name of book: ")
            if u.returnBook(u1, b1) and b.returnBook(u1, b1):
                print("Thanks.")
            else:
                print("Sorry!")
        elif userInput == 7:
            u1 = input("Enter the name of user: ")
            u.printBorrowers()
        elif userInput == 8:
            b1 = input("Enter the name of book: ")
            if b.addBook(b1):
                print("Done.")
            else:
                print("Sorry!")
        elif userInput == 9:
            u1 = input("Enter the name of user: ")
            if u.addUser(u1):
                print("Done.")
            else:
                print("Sorry!")
        elif userInput == 10:
            loop = False
        else:
            print("Try Again.")
        input("Press Enter to continue...")

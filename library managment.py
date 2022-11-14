#This is simple Library managment program for teams project
class library :
    def __init__(self,list):
        self.book=list
        self.lendDict={}
    def displayBook(self):
        print ("we have following books in our library: ")
        for book in self.book:
            print(book)
    def lendBook ( self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict[book]= user
            print("Lender-book Database has been updated... you can take the book now")
        else:
            print("book is already in use by" , {self.lendDict[book]})
    def addBook (self,book):
        self.booklist.append(book)
        print("book has been added to your list")
    def returnBook (self,book):
        self.lendDict.pop(book)

NSST = library(["Python","Math","Astronautics","Aerodynamics","Thermodynamics","Orbital"])
while(True):
    print("welcome to the NSST library ... Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend Books")
    print("3. Add Books")
    print("4. Return Books")
    user_choice = int(input())
    if user_choice == 1:
        NSST.displayBook()
    elif user_choice == 2:
        book= input("Enter the name of book you want to lend: ")
        user= input ("Enter your name: ")
        NSST.lendBook(user,book)
    elif user_choice == 3:
        book= input ("Enter the name of the book you want to add: ")
        NSST.addBook(book)
    elif user_choice == 4:
        book= input ("Enter the name of book you want to return: ")
        NSST.returnBook(book)
    else:
        print("NOT A VALID OPTION!")

    print("Press q to QUIT or c to CONTINUE")
    user_choice2 = ""
    while (user_choice2 != "c" and user_choice2 != "q"):
        user_choice2 = input("Enter your choice: ")
        if user_choice2 == "q":
            exit()
        elif user_choice2 =="c":
            continue

#THANK YOU FOR USING OUR PROGRAM--------->  <3

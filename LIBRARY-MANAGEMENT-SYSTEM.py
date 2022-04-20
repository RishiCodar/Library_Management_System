# LIBRARY MANAGEMENT SYSTEM

class Library:
    def __init__(self, list ,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def DisplayBooks(self):
        print(f"We have following Books in our Library : {self.name}")
        for book in self.booklist:
            print(book)

    def LendBooks(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now :)")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def AddBooks(self,book):
        self.booklist.append(book)
        print("Book has been added to the Book List")

    def ReturnBooks(self,book):
        self.lendDict.pop(book)
 

if __name__=='__main__':
    Rishi=Library(["Harry Poter","The Secert","Five Point Someone"],"ARYA")
    
    while True:
        print(f"WELCOME TO THE  {Rishi.name} LIBRARY :")
        print("1.DisplayBooks")
        print("2.LendBook")
        print("3.AddBook")
        print("4.ReturnBooks")
        user_choice=input("Enter your choice : ")
        if user_choice not in ['1','2','3','4']:
            print("Please Enter a valid option")
        else:
            user_choice=int(user_choice)


        if user_choice ==1:
            Rishi.DisplayBooks()
        elif user_choice==2:
            book=input("Enter the name of book you want to lend : ")
            user=input("Enter your name : ")
            Rishi.LendBooks(user,book)
        elif user_choice==3:
            book=input("Enter the name of book you want to add : ")
            Rishi.AddBooks(book)
        elif user_choice==4:
            book=input("Enter the name of book you want to return : ")
        else:
            print("Not a Valid option !!")

        print("Press q is quit and c to continue")
        user_choice2=""
        while user_choice2!="q" and user_choice2!="c":
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue







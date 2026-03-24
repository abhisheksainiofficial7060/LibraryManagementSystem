# library management system in python 


book_list = []
member_list = []
# prints main menu items
def displayMenu():
    print("""
    ---------------------------------
    Library Management System
    ---------------------------------
    1. Add Book
    2. Register Member
    3. Display Books
    4. Search Book
    5. Borrow Book
    6. Return Book
    7. Show Member Borrowed Books
    8. Show Unique Genres
    9. Exit
    ---------------------------------
    """)


# take userinput, displaymainmenu and check user menu items
def userInput():
    displayMenu()
    user_input = int(input("Enter your choice:"))
    if user_input == 1:
        addBook()
    elif user_input == 2:
        addMember()
    elif user_input == 3:
        displayBooks()
    elif user_input == 4:
        searchBook()
    elif user_input == 5:
        borrowBook()




# add book functionality 
def addBook():
    book = {}
    book_id = int(input("Book ID:"))
    book["book_id"] = book_id
    book_title = input("Title:")
    book["book_title"] = book_title
    book_author = input("Author:")
    book["book_author"] = book_author
    book_publication_year = int(input("Publication Year:"))
    book["book_publication_year"] = book_publication_year
    genre = []

    # only add maximum 100 genre
    for i in range(5):
        book_genre = input("Genres:")
        genre.append(book_genre)

        print("press 1 to enter",i+2,"genre or press 2 to exit")
        genre_con = int(input())
        if genre_con == 1:
            pass
        elif genre_con == 2:
            break
        else:
            print("invalid choice")
            i -=1
        
        if i == 4:
            print("max limit hit:")

    book["Genre"] = genre

    book_quantity = int(input("Quantity:"))
    book["book_quantity"] = book_quantity

    book_status = input("Status:")
    book["Status"] = book_status

    book_list.append(book)
    print("""----------------------------------
                   book successfully added     
    --------------------------------------------""")
    userInput()



    # print(book)
    # print(book_list)
    # userInput()


# Register a Member

def addMember():
    member = {}
    count=0
    member_id = int(input("Member Id:"))
    for i in range(len(member_list)):
        if member_list[i]["member_id"] == member_id:
            count+=1
    
    if count >0:
        print("Member already exist add new member:")
        userInput()
    else:
        member["member_id"] = member_id
        member_name = input("Name:")
        member["member_name"] = member_name
    print(member)
    member_list.append(member)
    print(member_list)
    userInput()




# display all books 
def displayBooks():
    print("--------------------All Books Available--------------------- ")
    for i in range(len(book_list)):
        # print(book_list[i].keys())
        print("Book ID:",book_list[i]["book_id"])
        print("Title:",book_list[i]["book_title"])
        print("Book Author:",book_list[i]["book_author"])
        print("Genre:",book_list[i]["Genre"])
        print("Status:",book_list[i]["Status"])
        print("-----------------------------------------------------------")




def searchBook():
    # print("press 1 to search book by id or press 2 to search by title:")
    choice = int(input("press 1 to search book by id or press 2 to search by title:"))
    if choice == 1:
        book_id = int(input("Book ID:"))
        for i in range(len(book_list)):
            if book_list[i]["book_id"] == book_id:
                print("----------------------------------")
                print("Book is found:",book_id)
                print("----------------------------------")
                print("Book ID:",book_list[i]["book_id"])
                print("Title:",book_list[i]["book_title"])
                print("Book Author:",book_list[i]["book_author"])
                print("Genre:",book_list[i]["Genre"])
                print("Status:",book_list[i]["Status"])
                print("-----------------------------------------------------------")

    elif choice ==2:
        book_title = input("Book Title:")
        for i in range(len(book_list)):
            if book_list[i]["book_title"] == book_title:
                print("----------------------------------")
                print("Book is found:",book_title)
                print("----------------------------------")
                print("Book ID:",book_list[i]["book_id"])
                print("Title:",book_list[i]["book_title"])
                print("Book Author:",book_list[i]["book_author"])
                print("Genre:",book_list[i]["Genre"])
                print("Status:",book_list[i]["Status"])
                print("-----------------------------------------------------------")
        
                
    else:
        print("Invalid Choice:")
        searchBook()


# Borrow a Book functionality
"""
5️⃣ Borrow a Book

A member should be able to borrow a book if:

The book exists

The book is available

When borrowed:

Update book availability

Add book ID to the member’s borrowed book list"""

def borrowBook():
    print("-----------------------------Borrow a Book -------------------------------------------------")
    choice = int(input("Press 1 to borrow by using BOOK_ID and Press 2 to borrow by using BOOK_NAME:"))
    count = 0
    if choice == 1:
        # print("Search by using book_id")
        book_id = int(input("Book_ID:"))
        for i in range(len(book_list)):
            if book_list[i]["book_id"] == book_id:
                count+=1
                print("book is founded:")
                if book_list[i]["book_quantity"]>0:
                    print("book is available for borrowing:")
                    print("****************************************")
                    inp1 = int(input("press 1 to borrow or 2 to exit:"))
                    count1 = 0
                    if inp1 == 1:
                        member_id = int(input("MEMBER_ID:"))
                        for i in range(len(member_list)):
                            if member_list[i]["member_id"] == member_id:
                                count+=1
                                print("member is exist")
                                pass
                            
                        if count1 == 0:
                            print("Member is not exist:")
                    else:
                        userInput()

                else:
                    print("book is not available for borrowing:")
        
        if count==0:
            print("Book is not added in stock:")
        
    elif choice == 2:
        print("serach by using book_name")
        pass
    else:
        print("Invalid choice")
        borrowBook()
    print("---------------------------------------------------------------------------------------------")



userInput()
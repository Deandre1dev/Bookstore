
# Import module.
import sqlite3

# Create table.
try:
    # Create the database and connection to database.
    db = sqlite3.connect('ebookstore')
    # Cursor bject.
    cursor = db.cursor()
    # Check if the table 'exist' if it does it should not be created again.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(id INTEGER(4) PRIMARY KEY, Title TEXT, Author VARCHAR(15),
                    Qty INTEGER)
    ''')
    db.commit()
except Exception as e :
    raise e

# Values for database.
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = "Harry Potter and the Philosopher's Stone"
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C. S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

id6 = 3006
Title6 = 'The picture of Dorian Gray'
Author6 = 'Oscar Wilde'
Qty6 = 17

id7 = 3007
Title7 = 'Trust'
Author7 = 'Herman Diaz'
Qty7 = 23

#Adding values to the table.
#Insert book 1.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id1, Title1, Author1, Qty1))
print('Book 1 inserted')

# Insert book 2.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id2, Title2, Author2, Qty2))
print('Book 2 inserted')

# Insert book 3.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id3, Title3, Author3, Qty3))
print('Book 3 inserted')

# Insert book 4.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id4, Title4, Author4, Qty4))
print('Book 4 inserted')

# Insert book 5.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id5, Title5, Author5, Qty5))
print('Book 5 inserted')

# Insert book 6.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id6, Title6, Author6, Qty6))
print('Book 6 inserted')

# Insert book 7.
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id7, Title7, Author7, Qty7))
print('Book 7 inserted')

db.commit()

# Functions for the bookstore.2
# Add a new book to the database.
def add_book():
    print('\nEnter the following information to add a new book : ')
    while True:
        cursor.execute('''SELECT id FROM books''')
        ids = [row[0]for row in cursor.fetchall()]
        cursor.execute('''SELECT Title FROM books''')
        titles = [row[0]for row in cursor.fetchall()]
        cursor.execute('''SELECT Author FROM books''')
        authors = [row[0]for row in cursor.fetchall()]

        try:
            id = int(input('Enter the id for the new book : '))
            if id not in ids:
                try:
                    Title = (input('Enter the title of the book : '))
                    if Title not in titles:
                        Author = (input('Enter the Author of the book : '))
                        if Author not in authors:
                            try:
                                Qty = int(input('Enter the quantity of the book on hand : '))
                                cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''',(id, Title, Author, Qty))
                                db.commit()
                                print('The book has been added successfully\n')
                                break
                            except ValueError:
                                print('\nEnter numerical values for the quantity')
                        else:
                            print('\nThe Author already exist')
                    else:
                        print('\nThe Title already exist')   
                except TypeError:
                    print('\nPlease enter a valid input')        
            else:
                print('\nid exist try again')                     
        except ValueError:
            print('\nEnter numerical values')   
        
# Update a books information.
def Update_book():
    print('Which information do you want to update on a specific book : ')
    while True:
        try:
            choice = int(input('''Enter one of the choices below :
        1.Title of a book.
        2.Author of a book.
        3.Qty of a book.
        0.Go back to the main menu.
        
        \nEnter choice here : '''))
            # Update the title of the book.
            if choice == 1:
                Title = (input('Enter the title of the book : '))
                new_title = (input('Enter the new title of the book : '))
            
                cursor.execute('''UPDATE books SET Title = ? WHERE Title = ?''',(new_title, Title))
                db.commit()
                print('The title of the book has been updated successfully.\n')
                break
            # Update the Author of the book.
            elif choice == 2:
                Title = (input('Enter the title of the book you wish to update the Author on : '))
                Author = (input('Enter the Author of the book : '))
                new_author = (input('Enter the new Author of the book : '))

                cursor.execute('''UPDATE books SET Author = ? WHERE Author = ? AND Title = ?''',(new_author, Author, Title))
                db.commit()
                print('The Author of the book has been successfully updated.\n')
                break
            # Update the Qty of a book.
            elif choice == 3:
                while True:
                    try:
                        Title = (input('Enter the title of the book you wish to update the quantity on : '))
                        new_qty = int(input('Enter the updated quantity of the specified book : '))

                        cursor.execute('''UPDATE books SET Qty = ? WHERE Title = ?''',(new_qty, Title))
                        db.commit()
                        print('Quantity has successfully updated.\n')
                        break
                    except ValueError:
                        print('Incorrect value entred.Please try again!...')
            elif choice == 0:
                    break
        except ValueError:
            print('Incorrect information has been entered.Please try again!...')

# Delete a book from the database.
def delete_book():
    print('Enter the following information to delete the specified book : ')
    while True:
        try:
            Title = (input('Enter the title of the book : '))
            Author = (input('Enter the Author of the book : '))
            cursor.execute('''DELETE FROM books WHERE Title = ? AND Author = ?''',(Title, Author))
            db.commit()
            print('Book has been deleted successfully\n')
            break
        except ValueError:
            print('Incorrect information has been entered.Please try again!...')

# Search the database for a specific book.
def search_book():
    print('Enter the following information to search for the specified book : ')
    while True:
            cursor.execute('''SELECT Title FROM books''')
            titles = [row[0]for row in cursor.fetchall()]
            cursor.execute('''SELECT Author FROM books''')
            authors = [row[0]for row in cursor.fetchall()]
            
            Title = (input('Enter the title of the book : '))
            Author = (input('Enter the Author of the book : '))
            if Title in titles and Author in authors:
                cursor.execute('''SELECT * FROM books WHERE Title = ? AND Author = ?''',(Title, Author))
                book = cursor.fetchone()
                print('\nData retrieved about book with Title %s:' % Title)
                print('The book that you have searched for :')
                print(str(book)+"\n")

                db.commit()
                break
            else:
                print('The book you have searched for does not exist!')
          
# Menu 
print('\t\t\t\tBookstore\n')
while True:
    try:
        print('Main Menu\n')
        menu = int(input('''Select one of the options below :
1.Enter a book
2.Update a book
3.Delete book
4.Search books
0.Exit\n
Enter choice here :  '''))

        if menu == 1:
            add_book()
            
        elif menu == 2:
            Update_book()
            
        elif menu == 3:
            delete_book()

        elif menu == 4:
            search_book()

        elif menu == 0:
            # Save changes to database before exiting.
            db.commit()
            db.close()
            print('Goodbye!')
            break
    except ValueError:
        print('Enter the correct value.Please try again!...\n')

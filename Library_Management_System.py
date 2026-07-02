class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f'This book is added {book}')
        
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'This {book} Book issued')
        else:
            print(f'This {book} is Not Available')
    
    def display_books(self):
        print(f'Available Books : {self.books}')
        
lib = Library()
lib.add_book('Python')
lib.add_book('SQL')
lib.add_book('Machine Learning')
print()
lib.display_books()
print()
lib.issue_book('Machine Learning') 
print()
lib.display_books()           
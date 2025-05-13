# Base Class - Book
class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
    
    def display_info(self):
        print(f"📖 Title: {self.title}")
        print(f"📝 Author: {self.author}")
        print(f"📚 Genre: {self.genre}")
        print(f"📅 Publication Year: {self.publication_year}")
    
    def update_info(self, title=None, author=None, genre=None, publication_year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if publication_year:
            self.publication_year = publication_year
        print("\n✅ Book information updated successfully!")

# Creating a Book object
my_book = Book("Python Mastery", "Adigun Faslul Haq", "Programming", 2025)
my_book.display_info()

# Updating the book info
my_book.update_info(title="Python Mastery - Advanced", publication_year=2026)
my_book.display_info()

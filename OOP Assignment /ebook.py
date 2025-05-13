# Derived Class - EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, genre, publication_year, file_size, file_format):
        super().__init__(title, author, genre, publication_year)
        self.file_size = file_size
        self.file_format = file_format
    
    def display_info(self):
        super().display_info()
        print(f"💾 File Size: {self.file_size} MB")
        print(f"📂 File Format: {self.file_format}")

# Derived Class - Audiobook (inherits from Book)
class Audiobook(Book):
    def __init__(self, title, author, genre, publication_year, duration, narrator):
        super().__init__(title, author, genre, publication_year)
        self.duration = duration
        self.narrator = narrator
    
    def display_info(self):
        super().display_info()
        print(f"⏱️ Duration: {self.duration} hours")
        print(f"🎙️ Narrator: {self.narrator}")

# Creating instances
ebook = EBook("AI for Beginners", "Adigun Faslul Haq", "Technology", 2024, 5, "PDF")
audiobook = Audiobook("The Art of Focus", "Adigun Faslul Haq", "Self-Help", 2023, 6.5, "Yusuf Ibrahim")

print("\n🖥️ E-Book Details:")
ebook.display_info()

print("\n🔊 Audiobook Details:")
audiobook.display_info()

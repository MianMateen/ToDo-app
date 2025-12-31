# Exercise: Create a Book class that:
# 1. Initializes with title, author, and pages
# 2. Has a method to mark pages read (can't read more pages than the book has)
# 3. Shows reading progress (like "You've read 50 out of 200 pages (25%)")
# 4. Has a method to reset reading progress

class Book:
    def __init__(self, title, author, total_pages):
        # Your code here: store title, author, total_pages
        # Add a pages_read variable starting at 0
        self.title = title
        self.author = author
        self.pages = total_pages
        self.pages_read = 0
        pass
    
    def read_pages(self, pages):
        # Your code here: add to pages_read
        # Don't allow reading more pages than the book has
        if (self.pages_read + pages) > self.pages:
            print(f"Can't read more pages then in {self.title}!!!")
        else:
            self.pages_read += pages
            return self.pages_read
        pass
    
    def show_progress(self):
        # Your code here: show pages read, total pages, and percentage
        self.progress: int = self.pages_read / self.pages * 100
        print(f"You've read {self.pages_read} out of {self.pages} pages ({self.progress}%)")
        pass
    
    def reset_progress(self):
        # Your code here: reset pages_read to 0
        self.pages_read = 0
        pass

# Test your code:
book = Book("Harry Potter", "J.K. Rowling", 200)
book.read_pages(50)
book.show_progress()  # Should show "You've read 50 out of 200 pages (25%)"
book.read_pages(250)  # Should show some error message
book.reset_progress()
book.show_progress()  # Should show "You've read 0 out of 200 pages (0%)"
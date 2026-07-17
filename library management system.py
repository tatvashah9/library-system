class book:
    
    def __init__(self, book_id: str,title: str,author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def __str__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"book_id {self.book_id} | title: '{self.title}' | author: {self.author} |[{status}]"
    
    class student:
        
        def __init__(self,student_id, name):
            self.student_id = student_id
            self.name = name
            self.borrowed = borrowed = []
        def __str__(self):
            borrowed_titles = ",". join if"{b.title}" for b in self.borrowed_books else "none"
            return f"student ID: {self.student_id} | name: {self.name} | borrowed: {borrowed_titles}"
        
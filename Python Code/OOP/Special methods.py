class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


# Use repr to display a representation other that the class object


    def __str__(self):
        return f"Title: {self.title}, Author {self.author}"

    def __len__(self):
        return self.pages


mybook = Book('Python', 'Lee Roberts', 200)

print(mybook)
print(len(mybook))

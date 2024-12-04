class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn, self.title, self.author, self.publisher, self.pages, self.price, \
        self.copies = [isbn, title, author, publisher, pages, price, copies]
    def display(self):
        print(self.isbn, self.title, self.author, self.publisher, \
        self.pages, self.price, self.copies)
    def in_stock(self):
        if self.copies != 0:
            return True
        else:
            return False
    def sell(self):
        if self.in_stock() == True:
            self.copies -= 1
        else:
            print('Out of Stock')
    @property
    def price(self):
        return self.book_price
    @price.setter
    def price(self, amount):
        if 50 < amount < 1000:
            self.book_price = amount
        else:
            raise Exception('Price must between 50 and 1000')
book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)
books = [book1, book2, book3, book4]
comprehension = []
for j in books:
    j.display()
    if j.author == 'Jack':
        comprehension.append(j)


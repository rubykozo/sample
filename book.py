# 本クラス
class Book:
    def __init__(self, title):
        self._title = title

    
    def show(self):
        print('{}'.format(self._title))


if __name__ == '__main__':
    book = Book('Python programming II')
    book.show()

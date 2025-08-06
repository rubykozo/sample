class Author:
    def __init__(self, name):
        self._name = name


    def show(self):
        print(self._name)


if __name__ == '__main__':
    tarou = Author('伊藤太郎')
    tarou.show()

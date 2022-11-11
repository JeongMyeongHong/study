class Names:
    def __init__(self):
        self.name1 = '홍정명'
        self.name2 = '송혜린'

    def print(self):
        print(self.name1)
        print(self.name2)


if __name__ == '__main__':
    name = Names()
    name.print()

    def swap(cls):
        cls.name1 = '바보'
        cls.name2 = '천재'

    swap(name)
    name.print()

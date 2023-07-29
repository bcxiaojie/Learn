class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def out(self):
        print(self.name, self.age)

if __name__ == '__main__':
    p = Person("你好",10)
    p.out()
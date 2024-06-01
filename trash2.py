class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
    
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

p = Person('miroslav', 13)
p.old = 23
print(p.old)
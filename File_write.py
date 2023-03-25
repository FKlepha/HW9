class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def Write_file(self):
        file = open('text.txt', 'a+')
        file.write(f'{self.name}, {self.lastname}, {self.age} \n')
        file.close()

    def Read_file(self):
        file = open('text.txt', 'r')
        file.read()
        file.close()


    def info(self):
        print(f'name = {self.name}, age = {self.age}, '
              f'lastname = {self.lastname}')




ivan = Person('Ivan', 'Ivanov', 25)
petr = Person('Petr', 'Petrov', 33)
masha = Person('Masha', 'Olegovna', 16)
ivan.Write_file()
petr.Write_file()
masha.Write_file()

li = []
ivan.Read_file()
li.append(ivan)
petr.Read_file()
li.append(petr)
masha.Read_file()
li.append(masha)
for i in li:
    i.info()
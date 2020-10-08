class Student:
    def __init__(self, surname, name, lastname, group):
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.group = group
    def introduce(self):
        print("Виконавець:",self.surname)
        print("\t   ", self.name)
        print("\t   ", self.lastname)
        print("     Група:", self.group)
        
def check_type(expression):
    print(str(expression), "is ", type(expression), " type")
def task_2(number):
    print(number % 10)
    print(number % 2)


check_type(2*4%7)
check_type(2*(4%7))
check_type(51//6%7)
check_type((-3+5)*(2%7//3+4*2))
check_type((3 // 5.0)*20+32.0)
check_type(float(int(1.56)))
check_type(bool(-0.0))
check_type(int(bool(13.56)))
check_type(float("inf"))

task_2(5)

print((10.001 / 9.001)**345 * (13.001/11.001)**249 / (9.001**10) / (11.001**20))

person = Student("Ільницький", "Ростислав", "Степанович", "K-13(2)")
person.introduce()

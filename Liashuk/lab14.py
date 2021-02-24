class Teplica():

    def set(self, zapobiznyk, w, o, windows_v, obigrivach_v, vologist, temperatura, zmina):
        self.zapobiznyk = zapobiznyk
        self.w = w
        self.o = o
        self.windows_v = windows_v
        self.obigrivach_v = obigrivach_v
        self.vologist = vologist
        self.temperatura = temperatura
        self.zmina = zmina

    def __init__(self, zapobiznyk = 1, w = 2, o = 3, windows_v = 0, obigrivach_v = 0, vologist = 36.2, temperatura = 10, zmina = -1):
        self.set(zapobiznyk, w, o, windows_v, obigrivach_v, vologist, temperatura, zmina)

    def window(self):
        print('There are windows: ' + str(self.w))
        print('There are open windows: ' + str(self.windows_v))

    def obigrivach(self):
        print('There are heaters: ' + str(self.o))
        print('Heaters are included: ' + str(self.obigrivach_v))

    def w_vologist(self):
        print('At the moment there is vologist: ' + str(self.vologist))

    def temperatur(self):
        print('At the moment there is temperatura: ' + str(self.temperatura))

    def zapobiz(self):
        if self.zapobiznyk == 0:
            print('zapobiznyk: 0')
            print('Fuse used!\n')
            self.w = 2
            self.o = 3
            self.windows_v = 0
            self.obigrivach_v = 0
        print('Diagnostyka')
        self.window()
        self.obigrivach()
        self.w_vologist()
        self.temperatur()

    def heater_on(self):
        self.zmina = 0
        if self.o == 0:
            print('Неможли ввімкнути обігрівач')
        else:
            print('Обігрівач ввімкнено')

    def window_open(self):
        self.zmina = 1
        if self.w == 0:
            print('Неможливо відкрити вікно')
        else:
            print('Вікно відкрито')

    def window_close(self):
        self.zmina = 2
        if self.obigrivach_v == 2:
            print('Неможливо закрити вікно')
        else:
            print('Вікно закрито')

    def heater_off(self):
        self.zmina = 3
        if self.obigrivach_v == 3:
            print('Неможливо вимкнути обігрівач')
        else:
            print('Обігрівач вимкнено')

def starts(a, b, c, d):
    print('Теплиця запущена')
    print('Показники на даний момент:\n')
    my_teplica.window()
    my_teplica.obigrivach()
    my_teplica.w_vologist()
    my_teplica.temperatur()
    print('\nнормальна відносна вологість 30-50% \nнормальтна температура 5-20')
    print(f'При вмиканні одного обігрівача температура збільшується на {a} градусів', end ='')
    print(f'а відносна вологість зменшується на {b}')
    print(f'При відкриванні одного вікна температура зменшується на {c} градусів', end ='')
    print(f'а відносна вологість збільшується на {d}\n')

def programa(a, b, c, d):
    if (my_teplica.zmina == 0) and (my_teplica.o != 0):
        my_teplica.vologist -= b
        my_teplica.temperatura += c
        my_teplica.o -= 1
        my_teplica.obigrivach_v += 1
    elif (my_teplica.zmina == 1) and (my_teplica.w != 0):
        my_teplica.vologist += a
        my_teplica.temperatura -= d
        my_teplica.w -= 1
        my_teplica.windows_v += 1
    elif (my_teplica.zmina == 2) and (my_teplica.windows_v != 2):
        my_teplica.vologist -= a
        my_teplica.temperatura += d
        my_teplica.w += 1
        my_teplica.windows_v -= 1
    elif (my_teplica.zmina == 3) and (my_teplica.obigrivach_v != 3):
        my_teplica.vologist += b
        my_teplica.temperatura -= c
        my_teplica.o += 1
        my_teplica.obigrivach_v -= 1

def ODZ():
    a1, a2 = 30, 50
    b1, b2 = 5, 20
    if (a1 <= my_teplica.vologist <= a2) and (b1 <= my_teplica.temperatura <= b2):
        print('', end= '')
    else:
        my_teplica.zapobiznyk = 0
        my_teplica.zapobiz()

my_teplica = Teplica()

a, b, c, d = 8, 5, 7, 4    # Збільшення, зменшення -- вологості, температури
starts(a, b, c, d)
programa(a, b, c, d)
ODZ()

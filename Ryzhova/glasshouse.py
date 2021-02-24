from glasshouse import *

glasshouse = Glasshouse()
glasshouse.show_status()

while glasshouse.state:
    command = input('What do you want to change?\nWindows, heaters, t, humidity: ')
    if command == 't':
        glasshouse.change_temperature()
        glasshouse.protector()
    elif command == 'windows':
        glasshouse.control_windows()
    elif command == 'heaters':
        glasshouse.control_heaters()
    elif command == 'humidity':
        glasshouse.change_relative_humidity()
        glasshouse.protector()
    else:
        continue
    glasshouse.show_status()

class Glasshouse():
    """
    Class for create and control glasshouse
    """
    def __init__(self):
        self.state = True
        self.num_windows = 2
        self.open_windows = 0
        self.num_heaters = 3
        self.on_heaters = 0
        self.relative_humidity = 36.2
        self.temperature = 10

    def show_status(self):
        """
        Show information about glasshouse
        """
        if self.state:
            print('Status: working')
        else:
            print('Status: non-working')
        print('Number of windows: ' + str(self.num_windows),
              'Open: ' + str(self.open_windows),
              'Number of heaters: ' + str(self.num_heaters),
              'On: ' + str(self.on_heaters),
              'Relative humidity: ' + str(self.relative_humidity),
              'Temperature: ' + str(self.temperature), sep='\n')

    def protector(self):
        """
        Control climate of glasshouse
        """
        if self.temperature > 30 or self.temperature < 8 \
                or self.relative_humidity > 80:
            self.state = False
            self.open_windows = 2
            self.on_heaters = 0

    def control_windows(self):
        """
        Manage state of windows
        """
        command = input('Close or open window?')
        if command == 'open':
            if self.open_windows != self.num_windows:
                self.open_windows += 1
            else:
                print('All windows are already open')
        if command == 'close':
            if self.open_windows != 0:
                self.open_windows -= 1
            else:
                print('All windows are already close')

    def control_heaters(self):
        """
        Manage state of heaters
        """
        command = input('On or off heater?')
        if command == 'on':
            if self.on_heaters != self.num_heaters:
                self.on_heaters += 1
            else:
                print('All heaters are already on')
        if command == 'off':
            if self.on_heaters != 0:
                self.on_heaters -= 1
            else:
                print('All heaters are already off')

    def change_temperature(self):
        """
        Control temperature
        """
        self.temperature = int(input('Enter information about temperature: '))

    def change_relative_humidity(self):
        """
        Control relative humidity
        """
        self.relative_humidity = int(input('Enter information about relative humidity(%): '))
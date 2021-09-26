class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formatDate(self):
        print("{:02d}/{:02d}/{}".format(self.day, self.month, self.year))

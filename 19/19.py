#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


class DateRange():

    def __init__(self, start, end): # strings 'DD-MM-YYYY'
        self.months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
                       7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        self.days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 
                     4:'Friday', 5:'Saturday', 6:'Sunday'}
        self.date_to_data('1-1-1900', start)
        self.start_day_of_week = self.count_days() % 7
        self.start_name = self.days[self.start_day_of_week]
        self.date_to_data('1-1-1900', end)
        self.end_name = self.days[self.count_days() % 7]
        self.date_to_data(start, end)
        self.days_in_range = self.count_days(self.start_day_of_week)

    def count_days(self, day_of_week=0):
        spec_sun_count = 0
        count = 0
        day = self.start_day
        month = self.start_month
        year = self.start_year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_year = True
        else:
            leap_year = False

        while (day != self.end_day or month != self.end_month or 
               year != self.end_year):
            if day_of_week == 6 and day == 1:
                spec_sun_count += 1
            print "%d/%d/%d" % (month, day, year)
            day += 1
            day_of_week += 1
            count += 1
            if day_of_week == 7:
                day_of_week = 0
            if leap_year and month == 2 and day == 29:
                continue
            elif day > self.months[month]:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
                    if year % 4 == 0 and (
                            year % 100 != 0 or year % 400 == 0):
                        leap_year = True
                    else:
                        leap_year = False
        self.day_of_week = day_of_week
        self.spec_suns = spec_sun_count
        return count

    def date_to_data(self, start, end):

        def get_day(date_string):
            return int(date_string[:date_string.find('-')])

        def get_month(date_string):
            return int(date_string[date_string.find('-')+1:
                                   date_string.rfind('-')])

        def get_year(date_string):
            return int(date_string[date_string.rfind('-')+1:])

        self.start_day = get_day(start)
        self.start_month = get_month(start)
        self.start_year = get_year(start)
        self.end_day = get_day(end)
        self.end_month = get_month(end)
        self.end_year = get_year(end)


if __name__ == '__main__':
    start = raw_input("\nEnter Start Date (DD-MM-YYYY): ")
    if start == '':
        start = '1-1-1901'
    end = raw_input("Enter End Date (DD-MM-YYYY): ")
    if end == '':
        end = '31-12-2000'
    date_range = DateRange(start, end)
    print "\nDays in range: %d" % date_range.days_in_range
    print "Special Sundays: %d" % date_range.spec_suns

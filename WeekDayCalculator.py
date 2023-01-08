class WeekDayError(Exception):
    def __init__(self):
        pass


class DayOfWeek:
    __days = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 7: 'Sun'}

    def __init__(self, day_var):
        if day_var in DayOfWeek.__days.values():
            self.__day = day_var
        else:
            raise WeekDayError

    def __str__(self):
        return str(self.__day)

    def add_days(self, n):
        day_value = int(DayOfWeek.get_key(self.__day))
        added = (day_value + int(n)) % 7
        if added == 0:
            added = 7
        self.__day = DayOfWeek.__days.get(added)
        return self.__day

    def subtract_days(self, n):
        day_value = int(DayOfWeek.get_key(self.__day))
        subtracted = ((day_value - (int(n) % 7)) + 7) % 7
        if subtracted == 0:
            subtracted = 7
        self.__day = DayOfWeek.__days.get(subtracted)
        return self.__day

    @staticmethod
    def get_key(val):
        for key, value in DayOfWeek.__days.items():
            if val == value:
                return key
        return 8


try:
    day = input("Enter the day (Mon, Tue, Wed, Thu, Fri, Sat, Sun): ")
    weekday = DayOfWeek(day)
    number = int(input("Enter the number of days you want to add or subtract: "))
    if number >= 0:
        weekday.add_days(number)
    else:
        weekday.subtract_days(abs(number))

    print(weekday)
except WeekDayError:
    print("Sorry! you entered incorrect day format, I can't serve your request.")

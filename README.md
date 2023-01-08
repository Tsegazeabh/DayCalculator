# DayCalculator
This python code will help you find the name of the day after adding or subtracting certain amount of days. 
You will first select the initial day and enter a positive or negative number to add or subtract certain amount of days
The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only 
acceptable values must come from the following set: Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception 
(define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

Objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored 
inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
All object's properties should be private;

This is an answer to the Python Institute Associate certification exercise on this link 'https://edube.org/learn/pe-2/days-of-the-week-1'

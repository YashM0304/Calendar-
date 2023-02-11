import calendar

x = int(input("Enter a year : "))

print("\n\n********CALENDAR********")
Cal = calendar.TextCalendar(calendar.SUNDAY)

i = 1
while i<12:
    Cal.prmonth(x,i)
    i+=1

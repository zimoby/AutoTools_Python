import curses
from datetime import datetime
# import calendar
import calendar

screen = curses.initscr()

curses.curs_set(0)

y = 0
for x in range(0, 20):
    if x%3 == 0:
        y += 1
        screen.addstr(2, int(x), str(y))
    
screen.refresh()
curses.napms(3000)

# month = prmonth(2019, 11, w=0, l=0)
# tc = calendar.TextCalendar(firstweekday=0)
# month = tc.formatmonth(2019, 11, w=0, l=0)
tc = calendar.Calendar(firstweekday=0) 
month = tc.monthdayscalendar(2019, 11)

# curses.curs_set(1)
screen.addstr(1, 1, str(month))
screen.refresh()
curses.napms(3000)

curses.endwin()
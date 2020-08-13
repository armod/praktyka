from datetime import datetime

#wejście musi być stringiem
def timeConversion(s):
    #teraz = datetime.datetime.now()
    # %H - godziny, %M - minuty, %d - dzień miesiąca, %m - miesiac, %Y - rok
    # %I - godzinmy w systemie 12h, %p - PM/AM

    #gdy w zestawieniu mamy czasy podane z końcówka 'p' lub 'a' dodajemy do str +'m'
    #datetime.strptime(str(time_value) + 'm', '%I:%M%p').strftime('%H:%M')
    czas = datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')
    print(czas)
    return czas


s = '12:40:22AM'
timeConversion(s)
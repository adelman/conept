"""
Matt Adelman
Conception Conncection
Based on SMBC 2922
"""

import sys
import urllib2
import datetime

def main(argv):

    s = "(no leading zeros): "

    year = input("Enter your birth year (yyyy): ")
    month = input("Enter your birth month as a number: ")
    day = input("Enter your birth day " + s)

    date1 = datetime.date(year, month, day)

    conception = date1 - datetime.timedelta(days = 266)

    new_month = _month_conversion(conception.month)
    str_year = "%d" % (conception.year)
    str_day = "%d" % (conception.day)

    if new_month == "not valid":
        print "You didn't enter a valid month!"

    rest = str_year + "/" + new_month + "/" + str_day
    date = (new_month + ", " + str_day + " " + str_year).title()

    request = urllib2.Request("http://www.historyorb.com/date/" + rest)
    result = (urllib2.urlopen(request)).read()

    index1 = result.find("</h2>")
    index2 = result.find("<p>-", index1)
    index3 = result.find("<", index2+5)

    if index2 == -1:
        print "Nothing found"

    else:
        event = result[index2 + 5:index3]
        print ""
        print "Your approximate conception date was " + date
        print "The event most likely to have cause your conception is..."
        print event

    return
        
def _month_conversion(month):
    if month == 1:
        return "january"
    elif month == 2:
        return "february"
    elif month == 3:
        return "march"
    elif month == 4:
        return "april"
    elif month == 5:
        return "may"
    elif month == 6:
        return "june"
    elif month == 7:
        return "july"
    elif month == 8:
        return "august"
    elif month == 9:
        return "september"
    elif month == 10:
        return "october"
    elif month == 11:
        return "november"
    elif month == 12:
        return "december"
    else:
        return "not valid"


if __name__ == "__main__":
    main(sys.argv)

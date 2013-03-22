"""
Matt Adelman
Conception Conncection
Based on SMBC 2922
"""

import sys
import urllib2

def main(argv):

    s = "(no leading zeros): "

    year = input("Enter your birth year (yyyy): ")
    month = input("Enter your birth month as a number: ")
    day = raw_input("Enter your birth day " + s)

    if month < 10:
        year = year - 1

    new_month = _month_conversion(month)
    str_year = "%d" % year

    if new_month == "not valid":
        print "You didn't enter a valid month!"

    rest = str_year + "/" + new_month + "/" + day
    date = (new_month + ", " + day + " " + str_year).title()

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
    if month < 10:
        new_month =  (month - 9 + 12) % 12
    else:
        new_month =  month - 9

    if new_month == 1:
        return "january"
    elif new_month == 2:
        return "february"
    elif new_month == 3:
        return "march"
    elif new_month == 4:
        return "april"
    elif new_month == 5:
        return "may"
    elif new_month == 6:
        return "june"
    elif new_month == 7:
        return "july"
    elif new_month == 8:
        return "august"
    elif new_month == 9:
        return "september"
    elif new_month == 10:
        return "october"
    elif new_month == 11:
        return "november"
    elif new_month == 12:
        return "december"
    else:
        return "not valid"


if __name__ == "__main__":
    main(sys.argv)

#!/usr/bin/env ruby

# A version of conception connection written in ruby
# Soon to be ported to rails, hopefully
require 'rubygems'
require 'curb'
require 'curb-fu'
require 'date'

def main
    
    s = "(no leading zeros): "
    print "Input your birth year (yyyy): "
    year = Integer(gets.chomp)
    print "Enter your birth month as a number #{s}"
    month = Integer(gets.chomp)
    print "Enter your birth day as a number #{s}"
    day = Integer(gets.chomp)

    unless month <= 12 && month >= 1
        puts "Not a valid month"
        return
    end

    con = (Date.new(year, month, day) - 266)

    new_month = month_conversion(con.month)

    rest = "#{con.year}/#{new_month}/#{con.day}"
    date = "#{new_month}, #{day} #{year}".capitalize!

    req = Curl.get("http://www.historyorb.com/date/" + rest)
    result = req.body_str

    index1 = result.index("</h2>")
    index2 = result.index("<p>-", index1) + 5
    index3 = result.index("<", index2) - 1

    if index2 == -1
        print "Nothing found"

    else
        event = result[index2..index3]
        puts ""
        puts "Your approximate conception date was " + date
        puts "The event most likely to have cause your conception is..."
        puts event
    end

    return


end

def month_conversion(new_month)
    if new_month == 1
        return "january"
    elsif new_month == 2
        return "february"
    elsif new_month == 3
        return "march"
    elsif new_month == 4
        return "april"
    elsif new_month == 5
        return "may"
    elsif new_month == 6
        return "june"
    elsif new_month == 7
        return "july"
    elsif new_month == 8
        return "august"
    elsif new_month == 9
        return "september"
    elsif new_month == 10
        return "october"
    elsif new_month == 11
        return "november"
    elsif new_month == 12
        return "december"
    else
        return "not valid"
    end

end

main

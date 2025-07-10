# 1 Jan 1900 was a Monday.
# Thirty days has September,　April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

##year%400 ==0 not leap years
##year%4==0 leap years
##How many Sundays fell on the first of the month 
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# 1 Jan 1900 was a Monday.
def leep_year(year):
    if year%4 == 0 and (year%100 !=0 or year%400 == 0):
        return True

month_days = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]
month_days_leep = [31, 29, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]


current_day =2 ##2 tuesday
count =0
## if day == 1 count++
for year in range(1901,2001):
    if leep_year(year):
        days_in_months = month_days_leep
    else:
        days_in_months = month_days
    
    for days in days_in_months:
        if current_day == 0: # sunday
            count +=1
        current_day = (current_day + days) % 7

print(count)










##30%7 2 曜日が2日ずれる
##31 %7 3 曜日が3ずれる
##1900年は閏年じゃない365日％7 1 monday

## 1 Jan 1901

# week_days =[0,1,2,3,4,5,6] #week_days =[sun,mon...]


def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def lastDay(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m[1] = 29 if isLeapYear(year) else 28
    return m[month - 1]

def totalDay(year, month, day):
    total = (year -1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400
    for i in range (1, month):
        total += lastDay(year, i)
    return total + day

# 요일을 숫자로 리턴하는 함수
# 일(0), 월(1), 화(2), 수(3), 목(4), 금(5), 토(6)
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7
    



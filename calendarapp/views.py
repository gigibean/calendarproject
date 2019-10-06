from django.shortcuts import render
import datetime
#현재 연도를 가져오기 위해 사용(필요하지 x)
from . import calendarmodule
# Create your views here.
def home(request):
    
    now = datetime.datetime.now()
    
    return render(request, 'home.html', {'now':now})

def monthCalendar(request):
    month_input = request.GET['monthInput']
    year = datetime.datetime.now().year
    # day = datetime.datetime.now().day
    month = int(month_input)
    print(year,"년 ", month,"월 ")
    rows = 6
    cols = 7
    snum = []
    # # 달력에서 요일과 1일의 위치 맞추기
    preDay = []
    nextDay = []
    numCals = []
    
    # 이달 전 날짜 
    for i in range(1, calendarmodule.weekDay(year,month,1)+1):
        preDay.append(calendarmodule.lastDay(year, month-1)+1 - i)
    preDay.sort()
    # 날짜 받기
    for i in range(1, calendarmodule.lastDay(year, month)+1):
        numCals.append(i)
    # 다음 달 날짜
    for i in range(1, calendarmodule.lastDay(year,month+1)+1):
        nextDay.append(i)
    for row in range(rows):
        snum += [[0]*cols]
    dayExtend = 0
    dayExtend2 = 0
    dayExtend3 =0
    count = 0

    print("{:^7}".format("일"), end=" ")
    print("{:^7}".format("월"), end=" ")
    print("{:^7}".format("화"), end=" ")
    print("{:^7}".format("수"), end=" ")
    print("{:^7}".format("목"), end=" ")
    print("{:^7}".format("금"), end=" ")
    print("{:^7}".format("토"))

    for row in range(rows):
        for col in range(cols):    
            if dayExtend == calendarmodule.weekDay(year,month,1):
                if dayExtend2+1 <= len(numCals):
                    snum[row][col] = numCals[dayExtend2]
                    dayExtend2 += 1
                    count += 1
                else:
                    snum[row][col] = nextDay[dayExtend3]
                    dayExtend3 += 1
            else:
                snum[row][col] = preDay[dayExtend]
                dayExtend += 1
            print("{:^8}".format(snum[row][col]), end=" ")
        print()
        
    

    return render(request, 'monthCalendar.html', {'monthInput':month_input, 'rows': range(0,rows,1), 'cols': range(0,cols,1) ,'year': year, 'month': month, 'numCals':numCals, 'preDay':preDay, 'snum': snum})
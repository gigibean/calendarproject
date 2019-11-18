from django.shortcuts import render, get_object_or_404
import datetime
from tkinter import *
import calendar
import datetime
from django.http import HttpResponseRedirect
from . import calendarmodule
from . import xsFileReadModule
from . import lunar_cal_module
# Create your views here.
def home(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
 
    def writeCalendar(year,month):
        str1 = calendar.month(year, month)
        label1.configure(text=str1)
    
    def mesAnterior():
        global month,year
        month-=1
        if month==0:
            month=12
            year-=1
    
        writeCalendar(year,month)
    
    def mesSiguiente():
        global month,year
        month+=1
        if month==13:
            month=1
            year+=1
    
        writeCalendar(year,month)
    
    root = Tk()
    root.title("캘린더")
    root.wm_geometry("600x400+20+40")
    photo = PhotoImage(file="D:\LIKELION\calendarproject\calendarapp\imgs\giphy.gif")
    photo_label = Label(image = photo) 
    photo_label.place(x = -2,y = -2)
    label1 = Label(root, text="", font=('courier', 14, 'bold'), bg='white', justify=LEFT)
    label1.grid(row=1,column=1)
    
    
    writeCalendar(year,month)
    
    root.mainloop()
    
    now = datetime.datetime.now()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    # day = datetime.datetime.now().day
    
    print(year,"년 ", month,"월 ")
    rows = 6
    cols = 7
    snum = []
    # # 달력에서 요일과 1일의 위치 맞추기
    preDay = []
    nextDay = []
    numCals = []
    luna_month = []
    luna_day = []
    luna = []
    # 이달 전 날짜 
    for i in range(1, calendarmodule.weekDay(year,month,1)+1):
        preDay.append(calendarmodule.lastDay(year, month-1)+1 - i)
    preDay.sort()
    # 날짜 받기
    for i in range(1, calendarmodule.lastDay(year, month)+1):
        numCals.append(i)
        #음력 받기
        luna.append([month, i ,lunar_cal_module.luna_month(year, month, i), lunar_cal_module.luna_day(year, month, i)])
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
    # value_e = 0
    # def event_find(value_e):
    # for d in xsFileReadModule.st_m:
    #     if d[4] == str(value_e) and d[3] == str(month):
    #         print(d[0] , "의 생일 입니다")
    snum1 = []
    for row in range(rows):
        snum1 += [[0]*cols]
    for row in range(rows):
        for col in range(cols): 
            snum1[row][col] = str(snum[row][col])
    month1 = str(month)
    return render(request, 'home.html', {'luna':luna,'luna_month':luna_month,'luna_day':luna_day,'now':now,'rows': range(0,rows,1), 'cols': range(0,cols,1) ,'year': year, 'month': month, 'numCals':numCals, 'preDay':preDay, 'snum': snum, 'nextDay':nextDay ,'numCals':numCals, 'st_d': xsFileReadModule.st_d, 'st_m': xsFileReadModule.st_m, 'snum1':snum1, 'month1':month1})

def monthCalendar(request):
    month_input = request.GET["monthInput"]
    month = int(month_input)
    year = datetime.datetime.now().year
    
    #앞에 달이랑 뒤에 달이랑 설정
    monthPre = str(int(month_input) - 1)
    if int(month_input) > 1 and int(month_input) <= 12:
        monthPre = str(int(month_input) - 1)
        month_input = str(int(monthPre) + 1)
    elif int(month_input) == 0 or int(monthPre) == -1:
        monthPre = "12"
        return HttpResponseRedirect("../2018/?monthInput=12")
    monthNext = str(int(month_input) + 1)
    if int(month_input) > 0 and int(month_input) <= 12:
        monthNext = str(int(month_input) + 1)
        month_input = str(int(monthPre) - 1)
    elif int(monthNext) > 13 or int(month_input) == 13:
            return HttpResponseRedirect("../2020/?monthInput=1")

    
    # day = datetime.datetime.now().day
    
    print(year,"년 ", month,"월 ")
    rows = 6
    cols = 7
    snum = []
    # # 달력에서 요일과 1일의 위치 맞추기
    preDay = []
    nextDay = []
    numCals = []
    
    # 이달 전 날짜 
    if month is not 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year, month-1)+1 - i)
    elif month is 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year - 1, 12)+1 - i)
            
    preDay.sort()
    # 날짜 받기
    for i in range(1, calendarmodule.lastDay(year, month)+1):
        numCals.append(i)
    # 다음 달 날짜
    if month is not 12:
        for i in range(1, calendarmodule.lastDay(year,month+1)+1):
            nextDay.append(i)
    else:
        for i in range(1, calendarmodule.lastDay(year+1,1)+1):
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
    # value_e = 0
    # def event_find(value_e):
    # for d in xsFileReadModule.st_m:
    #     if d[4] == str(value_e) and d[3] == str(month):
    #         print(d[0] , "의 생일 입니다")
    snum1 = []
    for row in range(rows):
        snum1 += [[0]*cols]
    for row in range(rows):
        for col in range(cols): 
            snum1[row][col] = str(snum[row][col])
    month1 = str(month)
    return render(request, 'monthCalendar.html', {'month_input':month_input, 'monthNext':monthNext, 'monthPre':monthPre, 'rows': range(0,rows,1), 'cols': range(0,cols,1) ,'year': year, 'month': month, 'numCals':numCals, 'preDay':preDay, 'snum': snum, 'nextDay':nextDay ,'numCals':numCals, 'st_d': xsFileReadModule.st_d, 'st_m': xsFileReadModule.st_m, 'snum1':snum1, 'month1':month1})


def monthCalendar2018(request):
    month_input = request.GET["monthInput"]
    month = int(month_input)
    year = 2018
    
    #앞에 달이랑 뒤에 달이랑 설정
    monthPre = str(int(month_input) - 1)
    if int(month_input) > 1 and int(month_input) <= 12:
        monthPre = str(int(month_input) - 1)
        month_input = str(int(monthPre) + 1)
    elif int(month_input) == 0 or int(monthPre) == -1:
        monthPre = "12"
    monthNext = str(int(month_input) + 1)
    if int(month_input) > 0 and int(month_input) <= 12:
        monthNext = str(int(month_input) + 1)
        month_input = str(int(monthPre) - 1)
    elif int(monthNext) > 13 or int(month_input) == 13:
            return HttpResponseRedirect("../2019/?monthInput=1")

    # day = datetime.datetime.now().day
    
    print(year,"년 ", month,"월 ")
    rows = 6
    cols = 7
    snum = []
    # # 달력에서 요일과 1일의 위치 맞추기
    preDay = []
    nextDay = []
    numCals = []
    
    # 이달 전 날짜 
    if month is not 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year, month-1)+1 - i)
    elif month is 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year - 1, 12)+1 - i)
            
    preDay.sort()
    # 날짜 받기
    for i in range(1, calendarmodule.lastDay(year, month)+1):
        numCals.append(i)
    # 다음 달 날짜
    if month is not 12:
        for i in range(1, calendarmodule.lastDay(year,month+1)+1):
            nextDay.append(i)
    else:
        for i in range(1, calendarmodule.lastDay(year+1,1)+1):
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
    # value_e = 0
    # def event_find(value_e):
    # for d in xsFileReadModule.st_m:
    #     if d[4] == str(value_e) and d[3] == str(month):
    #         print(d[0] , "의 생일 입니다")
    snum1 = []
    for row in range(rows):
        snum1 += [[0]*cols]
    for row in range(rows):
        for col in range(cols): 
            snum1[row][col] = str(snum[row][col])
    month1 = str(month)
    return render(request, 'monthCalendar.html', {'month_input':month_input, 'monthNext':monthNext, 'monthPre':monthPre, 'rows': range(0,rows,1), 'cols': range(0,cols,1) ,'year': year, 'month': month, 'numCals':numCals, 'preDay':preDay, 'snum': snum, 'nextDay':nextDay ,'numCals':numCals, 'st_d': xsFileReadModule.st_d, 'st_m': xsFileReadModule.st_m, 'snum1':snum1, 'month1':month1})


def monthCalendar2020(request):
    month_input = request.GET["monthInput"]
    month = int(month_input)
    year = 2020
    
    #앞에 달이랑 뒤에 달이랑 설정
    monthPre = str(int(month_input) - 1)
    if int(month_input) > 1 and int(month_input) <= 12:
        monthPre = str(int(month_input) - 1)
        month_input = str(int(monthPre) + 1)
    elif int(month_input) == 0 or int(monthPre) == -1:
        monthPre = "12"
        return HttpResponseRedirect("../2019/?monthInput=12")

    monthNext = str(int(month_input) + 1)
    if int(month_input) > 0 and int(month_input) <= 12:
        monthNext = str(int(month_input) + 1)
        month_input = str(int(monthPre) - 1)
    elif int(monthNext) > 13 or int(month_input) == 13:
        monthNext = "1"

    # day = datetime.datetime.now().day
    
    print(year,"년 ", month,"월 ")
    rows = 6
    cols = 7
    snum = []
    # # 달력에서 요일과 1일의 위치 맞추기
    preDay = []
    nextDay = []
    numCals = []
    
    # 이달 전 날짜 
    if month is not 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year, month-1)+1 - i)
    elif month is 1:
        for i in range(1, calendarmodule.weekDay(year,month,1)+1):
            preDay.append(calendarmodule.lastDay(year - 1, 12)+1 - i)
            
    preDay.sort()
    # 날짜 받기
    for i in range(1, calendarmodule.lastDay(year, month)+1):
        numCals.append(i)
    # 다음 달 날짜
    if month is not 12:
        for i in range(1, calendarmodule.lastDay(year,month+1)+1):
            nextDay.append(i)
    else:
        for i in range(1, calendarmodule.lastDay(year+1,1)+1):
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
    # value_e = 0
    # def event_find(value_e):
    # for d in xsFileReadModule.st_m:
    #     if d[4] == str(value_e) and d[3] == str(month):
    #         print(d[0] , "의 생일 입니다")
    snum1 = []
    for row in range(rows):
        snum1 += [[0]*cols]
    for row in range(rows):
        for col in range(cols): 
            snum1[row][col] = str(snum[row][col])
    month1 = str(month)
    return render(request, 'monthCalendar.html', {'month_input':month_input, 'monthNext':monthNext, 'monthPre':monthPre, 'rows': range(0,rows,1), 'cols': range(0,cols,1) ,'year': year, 'month': month, 'numCals':numCals, 'preDay':preDay, 'snum': snum, 'nextDay':nextDay ,'numCals':numCals, 'st_d': xsFileReadModule.st_d, 'st_m': xsFileReadModule.st_m, 'snum1':snum1, 'month1':month1})
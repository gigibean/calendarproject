# -*- coding:utf-8 -*-
import openpyxl
from pprint import pprint as pp
import collections

#엑셀 파일 열기
filename = "st_bd_file.xlsx"
book = openpyxl.load_workbook(filename)

#맨 앞의 시트 추출하기
sheet = book.worksheets[0]
# 시트의 각 행을 순서대로 추출하기
data = []

# birth_day_counts = [] #row3번째인덱스에있는것들넣기
for row in sheet.rows:
    data.append([row[1].value, row[2].value, row[3].value])
    # birth_day_counts.append(row[3].value)

#필요없는 데이터 제거
del data[0]
del data[1]
del data[3]

# data 출력
birth_day_counts = [] #row 3번째 있는 것들(생일 담기)
st_m = [] #24이하 다시 담기
st_k = []
for i, v in enumerate(data):
    if i <= 24:
        print("index : {}, value: {}".format(i,v))
        birth_day_counts.append(v[2])
        st_m.append([str(v[0])])
        st_k.append(str(v[1])[-8:])

#bith_day_counts 필터링하기 데이터 6자리로 + (년,월,일로 슬라이싱)
bd_set_in_list = []
for value in birth_day_counts:
    value = str(value)
    bd_set_in_list.append(value[-6:])
    
year_set_in_list = []
month_set_in_list = []
day_set_in_list = []
for value in bd_set_in_list:
    year_set_in_list.append(value[0:2])
    if value[2] == "1":
        month_set_in_list.append(value[2:4])
    else:
        month_set_in_list.append(value[3:4])
    if value[4] == "0":
        day_set_in_list.append(value[5:6])
    else:
        day_set_in_list.append(value[4:6])


#마이닝된 데이터로 다시 딕셔너리만들기
for i,value in enumerate(bd_set_in_list):
    st_m[i].append(value)
for i,value in enumerate(year_set_in_list):
    st_m[i].append(value)
for i,value in enumerate(month_set_in_list):
    st_m[i].append(value)
for i,value in enumerate(day_set_in_list):
    st_m[i].append(value)
st_d =dict(zip(st_k, st_m))
print("st_d is")
pp(st_d)

#총 생일 개수 dic형태로 변환
bd_count_dict = collections.Counter(bd_set_in_list)
bd_year_count_dict = collections.Counter(year_set_in_list)
bd_month_count_dict = collections.Counter(month_set_in_list)
bd_day_count_dict = collections.Counter(day_set_in_list)
print("bd count : ")
pp(bd_count_dict)
print("bd year count : ")
pp(bd_year_count_dict)
print("bd month count : ")
pp(bd_month_count_dict)
print("bd day count : ")
pp(bd_day_count_dict)

book.close()
from korean_lunar_calendar import KoreanLunarCalendar


calendar = KoreanLunarCalendar()
def luna_day(solor_year, solor_month, solor_day):
    # params : year(년), month(월), day(일)
    calendar.setSolarDate(solor_year,solor_month,solor_day)
    return calendar.lunarDay
def luna_month(solor_year, solor_month, solor_day):
    calendar.setSolarDate(solor_year,solor_month,solor_day)
    return calendar.lunarMonth
def luna_year(solor_year, solor_month, solor_day):
    calendar.setSolarDate(solor_year,solor_month,solor_day)
    return calendar.lunarYear
    



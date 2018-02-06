import calendar
day=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
date=input().split()
for i in range(len(date)):
    date[i]=int(date[i])
d=date[0]
m=date[1]
y=date[2]
dayresult=calendar.weekday(y, m, d)
print(day[dayresult])
        

from datetime import datetime, date
x = '29.03.2024'
y = datetime.strptime(x,'%d.%m.%Y')
f = y.weekday()
if f == 4 or f == 5:
    print ('zhopa')
else:
    print('piska')
#z = datetime.strftime(y, '%d.%m.%Y')

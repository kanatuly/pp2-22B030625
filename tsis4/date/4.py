import datetime

d1 = datetime.date(2020, 12, 12)
d2 = datetime.date(2020, 11, 11)
print(abs((d2-d1).total_seconds()))

# import time
# t = time.localtime()
# print("t = ",t)


# import datetime
# start = datetime.date(1901,1,1)
# end = datetime.date(2000,12,31)
# ans = 0
# while True:
#     if start.weekday() == 0:
#         ans += 1
#     start += datetime.timedelta(days = 1)
#     if start > end:
#         break
# print(ans)





import datetime
start = datetime.date(2022,1,1)
end = datetime.date(2022,12,31)
ans = 0
while True:
    now_date = start.strftime("%Y%m%d")
    if '012' in now_date or '123' in now_date:
        ans += 1
    start += datetime.timedelta(days = 1)    
    if start > end:
        break
print(ans)
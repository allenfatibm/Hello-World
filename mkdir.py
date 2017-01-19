import os
import datetime

time_array = datetime.datetime.now()        # get current datetime stamp
path = str("E:/daily folder/")              # set destination path
currentYear = time_array.strftime('%Y')     # set current year, i.e. 2017
month = [1,2,3,4,5,6,7,8,9,10,11,12]

for n in month:
    month_stamp = datetime.date(int(currentYear),n,1).strftime('%b')
    folder_name = path + month_stamp
    os.mkdir(folder_name)  # create monthly folder
    currentmonth = datetime.date(int(currentYear), n, 1).strftime('%m')
    if n < 12:   # days in each month from Jan to Nov
        d1 = datetime.date(int(currentYear), int(currentmonth), 1).strftime("%j")
        d2 = datetime.date(int(currentYear), int(currentmonth) + 1, 1).strftime("%j")
        day_count = int(d2) - int(d1)
    else:
        day_count = 31   # days in Dec
    for i in range(1, day_count):
        time_stamp = datetime.date(int(currentYear),n,1) + datetime.timedelta(days=i)
        day_stamp = time_stamp.strftime("%F")
        week_day = datetime.datetime.isoweekday(time_stamp)
        if week_day == 1:   # day off on Monday
            pass
        elif week_day == 7:  # day off on Sunday
            pass
        else:
            sub_folder_name = folder_name + str('/') + day_stamp
            os.mkdir(sub_folder_name)

print("All folders are created!")

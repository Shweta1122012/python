import random
import time
def getrandomdates(startdate,endate):

    print("printing random dates between",startdate,"and",endate)
    randomgenerator = random.random()
    dateformat='%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime =time.mktime(time.strptime(endate,dateformat))
    randomtime = starttime + randomgenerator *(endtime-starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("generating random dates from 1/1/2014 to 12/12/2019",getrandomdates("1/1/2014","12/12/2019"))


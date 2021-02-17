from ub_gym_notifier import*
from datetime import date

today = date.today()
weekday_int = today.weekday()

loc = 'Clark Hall'
url_pre = 'https://www.signupgenius.com/go/8050848a9a729a0fe3'

days = ['monday','tuesday','wednesday','thursday','friday']
weekdays = [12,12,11,12,13]
notify_endpoint = 'https://notify.run/KQQrnm4IqCuxC6D7'
url = ''

def clark_notify_all():
    if(weekday_int==1):
        days = days[1:]
        days = days[1:]
    if(weekday_int==2):
        days = days[2:]
        weekdays = weekdays[2:]
    if(weekday_int==3):
        days = days[3:]
        weekdays = weekdays[3:]
    if(weekday_int==4):
        days = days[4:]
        weekdays = weekdays[4:]
    if(weekday_int==5):
        days = days[5:]
        weekdays = weekdays[5:]
    if(len(days)>0):
        for i in range(len(days)):
            url = url_pre + '-'+ days[i]+str(weekdays[i])
            event_notifier(url,notify_endpoint,days[i])





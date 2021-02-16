from ub_gym_notifier import*

loc = 'Clark Hall'
url_pre = 'https://www.signupgenius.com/go/8050848a9a729a0fe3'

days = ['monday','tuesday','wednesday','thursday','friday']
weekdays = [12,12,11,12,13]
notify_endpoint = 'https://notify.run/KQQrnm4IqCuxC6D7'
url = ''

def clark_notify_all():
    for i in range(len(days)):
        url = url_pre + '-'+ days[i]+str(weekdays[i])
        event_notifier(url,notify_endpoint,days[i])





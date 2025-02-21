import datetime
import random

now = datetime.datetime.now()

print('five days ago:', now - datetime.timedelta(days=5))     #1

print('yesterday:', now - datetime.timedelta(days=1))     #2
print('today:', now)
print('tomorrow', now + datetime.timedelta(days=1))

print('today without microsec:', now.replace(microsecond=0))     #3

random_day = random.randint(1,10)     #4
random_hour = random.randint(1,24)
random_sec = random.randint(1,60)
random_date = now - datetime.timedelta(days=random_day, hours=random_hour, seconds=random_sec)
print('difference from today to', random_date.replace(microsecond=0), ':', now - random_date)
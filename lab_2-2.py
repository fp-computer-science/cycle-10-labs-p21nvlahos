# Author: NV 12/4/2020

def email(lst):
    for name in lst:
        print("Hi {0}, You're in veeted to my party on Friday!".format(name))

names = (['Steve', 'Jason', 'Luke'])
email(names)
'''
Created on 2017年5月27日

@author: Todd
'''

from Get_Weather_Data import get_weather_data
from Create_Html_file import create_html_report
from Email_Via_Gmail import send_gmail

from collections import OrderedDict
from time import sleep
from pprint import pprint
import schedule


def job():
    pprint(schedule.jobs)
    weather_dict, icon = get_weather_data('KLAX')    
    print(weather_dict.items())
    print(sorted(weather_dict.items()))
    weather_dict_ordered = OrderedDict(sorted(weather_dict.items()))
    print(weather_dict_ordered)
    
    
    email_file = 'Email_File.html'
    create_html_report(weather_dict, icon, email_file)
    send_gmail(email_file)
    
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)

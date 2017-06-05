'''
Created on 2017年5月26日

@author: Todd

https://myaccount.google.com/lesssecureapps
'''

import smtplib
from email.mime.text import MIMEText
from GMAIL_PWD import GMAIL_PWD
from datetime import datetime

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:
        msg = MIMEText(message.read(), 'html', 'html')
        
    msg['Subject'] = 'Hourly Weather {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M'))
    msg['From'] = 'rekonin332@gmail.com'
    msg['To'] = 'another@gmail.com, rekonin332@gmail.com'
    
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rekonin332@gmail.com', GMAIL_PWD)
    server.send_message(msg)    
    server.close()
    
    
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    from Create_Html_file import create_html_report
    weather_dict, icon = get_weather_data()    
    email_file = 'Test_Email_File.html'
    create_html_report(weather_dict, icon, email_file)
    send_gmail(email_file)
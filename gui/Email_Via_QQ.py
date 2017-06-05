'''
Created on 2017年5月31日

@author: Todd
'''

import smtplib
from email.mime.text import MIMEText
from GMAIL_PWD import QQ_Authorization_Code
from datetime import datetime

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:
        msg = MIMEText(message.read(), 'html', 'html')
        
    msg['Subject'] = 'Hourly Weather {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M'))
    msg['From'] = '38468856@qq.com'
    msg['To'] = 'another@qq.com, 38468856@qq.com'
    
    server = smtplib.SMTP_SSL('smtp.qq.com', port=465)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
    server.login('38468856@qq.com', QQ_Authorization_Code)
    server.send_message(msg)    
    server.close()

    
    
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    from Create_Html_file import create_html_report
    weather_dict, icon = get_weather_data()  
    email_file = 'Test_QQ_Email_File.html'
    create_html_report(weather_dict, icon, email_file)
    print('===> Ready to send email via QQ')
    send_gmail(email_file)
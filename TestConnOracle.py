'''
Created on 2017年6月1日

@author: Todd
'''
# -*- coding: UTF-8 -*-
import cx_Oracle

import traceback  

# db=cx_Oracle.connect('todd','123456','192.168.177.131:1521/XE')
# try:
#     db=cx.connect('todd',
#                   '123456',
#                   '192.168.177.131:1521/XE')
# #     db=cx_Oracle.connect('todd/123456@XE')
# 
# except:
#     traceback.print_exc()
#  
#  
# print (db.version)

# connect via SQL*Net string or by each segment in a separate argument
#connection = cx_Oracle.connect("user/password@TNS")
connection = cx_Oracle.connect("todd", "123456", "192.168.177.131:1521/XE")

cursor = connection.cursor()
cursor.execute("""
        select name, grade
        from tmp_todd""",)
for column_1, column_2 in cursor:
    print("Values:", column_1, column_2)
     
 
cursor.close()
connection.close()

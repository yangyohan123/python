'''
Created on 2020. 1. 20.

@author: GDJ-19
'''
               # -m pip install --upgrade pip
import pymysql # pip install mymysql(cmd창에서 명령어 )

conn = pymysql.connect(host="localhost", port=3306,
                       user="scott", passwd="1234",
                       db="classdb", charset="utf8")

try:
    # sql 구문을 전달해줌 : cursor()
    # cursor() 객체 -> cur
    # cursor() : 실행된 모든것을 가지고 있는 것 
    cur = conn.cursor()

    cur.execute("select * from item")
#    while True :
#        row = cur.fetchone() #1건의 레코드만 조회
#        if row == None :
#            break
#        print(row)
    
    #type(row) : tuple -> 변경불가 리스트
    for row in cur.fetchall():
        #print(type(row), row)
        print(row[0],row[1],row[2])
finally:
    cur.close()
    conn.close()
'''
Created on 2020. 1. 17.

@author: GDJ-19
화면에서 내용을 입력받아 sqlite db에 내용 저장하기
'''
import sqlite3

dbpath = "text.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor()

cur.executescript('''
    drop table if exists usertable;
    create table usertable (userid varchar(4) primary key, 
        email varchar(30),
        username varchar(20), 
        birthday integer)

''')


while True :
    data1 = input("사용자ID=> ")
    if data1 == '':
        break
    data2 = input("사용자이름=> ")
    data3 = input("이메일=> ")
    data4 = input("출생 연도=> ")
    sql = "insert into usertable values('"\
     + data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    con.commit()
#등록된 내용 select로 조회하기
cur = con.cursor()
cur.execute("select * from usertable")
list = cur.fetchall()
for row in list :
    print(row)
con.close()
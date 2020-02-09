'''
Created on 2020. 1. 20.

@author: GDJ-19
정규식 예제 2. 정규화 모듈 사용하기
 정규식 표현법
 () : 그룹화
 [] : 문자
 {} : 문자의갯수
 \d : 숫자
 (\d{6})[-]\d{7} : 첫번째 그룹 : 숫자6자리. 다음 문자 -이면서
                                    다음문자는 숫자로 7자리로 이루어진 문자열
 \g<1> : 첫번째 그룹
 
 ? : 0 또는 1 개
 ca?t : c로 시작, a 문자가 없거나 1개인 경우
        ex) "ct" : ture
            "cat" : true
            "caaaat" : false
 
  * : 0개 이상
  ca*t : c로 시작, a 문자가 없거나 여러개인 경우
        ex) "ct" : ture
            "cat" : true
            "caaaat" : true
            
  + : 1개 이상
  ca+t : a 문자가 1개이거나 여러개인 경우
        ex) "ct" : false
            "cat" : true
            "caaaat" : true
  
  {n} : n개 반복
  ca{n}t : a 문자가 2개
        ex) "ct" : false
            "cat" : false
            "caat" : true            
            "caaaat" : true
  
  {n,m} : n개 이상 m개 이하 반복
  ca{2,5}t : a 문자가 n개 이상 m개이하 반복
        ex) "ct" : false
            "cat" : false
            "caat" : true
            "caaaaat" : true   
            "caaaaaaaaaaaaat" : false

'''

import re #정규식 사용을 위한 모듈

data = '''
    park 800905-1234567
    kim 700905-2234567
    choi = 850101-a123456
'''

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

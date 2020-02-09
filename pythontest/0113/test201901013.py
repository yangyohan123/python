'''
Created on 2020. 1. 13.

@author: GDJ-19

조건
1.영어단어,한글의미를 가지고 있는 사전을 등록하는 프로그램을 작성하기
2. 사전을 작성하기 위한 메뉴 
   1:조회, 2:등록, 3:수정, 4:삭제, 9:종료
   위의 번호를 제외한 값을 입력받지 않는다.
2. 등록된 사전내용이 없는 경우 조회 메뉴는 선택할 수 없다.
3.조회시 조건
   - 정렬방식을 지정할 수 있다. 영어기준, 한글 기준, 입력기준
   - 결과 참조
4. 등록시 조건
   - 같은 영어 단어가 입력되는 경우에는  이미 등록된 단어라 출력한다
   - 등록되지 않은 영어 단어인 경우 한글 의미를 입력받아
     사전에 등록한다.
5. 수정시 조건
    - 등록되지 않은 단어인 경우 등록되지 않은 단어라 출력한다.
    - 등록된 단어인 경우 한글 의미를 입력받아 수정한다.
 6. 삭제시 조건  
    - 등록되지 않은 단어인 경우 등록되지 않은 단어라 출력한다.
    - 등록된 단어인 경우 사전에서 제거한다.
7. 결과를 정답란에 입력하고, 파이썬소스를 첨부하기
'''
import operator

    

word1 = {}
word2 = {}
list = []

while(True) :
    if len(word1) == 0 :
        print("2.등록, 3:수정, 4:삭제, 9:종료")
        sel = input("번호를 입력하세요=>")
        if sel.__eq__('2') :
            eword = input("등록할 영어 단어=>")
            hword = input("등록할 한글 단어=>")
            word1[eword] = hword
        elif sel.__eq__('9') :
            break
        elif sel.__eq__('3') :
            print("수정할 단어가 없습니다.") 
        elif sel.__eq__('4') :
            print("삭제할 단어가 없습니다.")
        else :
            print("번호가 틀립니다.")
    else :    
        print("1:조회, 2:등록, 3:수정, 4:삭제 , 9:종료")
        sel = input("번호를 입력하세요=>")
    
        if sel.__eq__('9') :
            break
        elif sel.__eq__('1'):
            print("===================등록된 단어 갯수:%d"%len(word1))
            sort = input("정렬기준(1:영문기준,2:한글기준, 그외값 입력순서)=>")
            if sort.__eq__('1') :
                print("======사전 내용(영문기준 정렬)======")
                list = sorted(word1.items(), key=operator.itemgetter(0))
                for i in range(0,len(word1)) :
                    print(str(list[i][0])+"="+str(word1[list[i][0]]))
            elif sort.__eq__('2') :
                print("======사전 내용(한글기준 정렬)======")
                list = sorted(word1.items(), key=operator.itemgetter(1))
                for i in range(0,len(word1)) :
                    print(list[i])
            else :
                
                for i in range(0,len(word1)) :
                    print(word1)
                
        elif sel.__eq__('2') :
            eword = input("등록할 영어 단어=>")
            if  eword in word1 :
                print("이미 등록된 단어입니다.")
                
            else :
                hword = input("등록할 한글 단어=>")
                word1[eword] = hword
            
        elif sel.__eq__('3') :
            modify = input("수정할 영어 단어=>")
            if  modify in word1 :
                chword = input("등록할 한글 단어=>")
                word1[modify] = chword
            else :
                print("등록되지 않는 단어입니다.")
   
        elif sel.__eq__('4') :
            delword = input("삭제할 영어 단어=>")
            if  delword in word1 :
                word1.pop(delword)
            else :
                print("등록되지 않는 단어입니다.")
            
        
        else :
            print("번호가 틀립니다.")
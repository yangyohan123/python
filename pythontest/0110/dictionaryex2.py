'''
Created on 2020. 1. 10.

@author: GDJ-19
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}

for i in foods.keys() :
    print("%s=>%s"% (i,foods[i]))
    
# 화면에서 음식을 입력받아서 궁합음식 출력하기
# 입력받은 음식값이 "종료" 인 경우 프로그램 종료하기

while(True) :
    # dics_key인 foods.keys()를 list로 형변환하여 keys의 값들만 가져오고 
    # list형태를 str형변환시킴
    food = input(str(list(foods.keys())) + "음식이름을 입력하세요:")
    
    # [('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치'), ('맥주', '치킨')] => list[] 안에 튜플('맥주', '치킨')
    # dict_items([('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치'), ('맥주', '치킨')]) => 딕셔너리
    if food.__eq__("종료") :
        print("등록된 음식 갯수:%d"%len(foods))
        print("좋아하는 음식:" + str(list(foods.keys())))
        print("궁합 음식" + str(list(foods.values())))
        print(list(foods.items())) 
        print(foods.items())
        break
    if food in foods : #foods의 key값이 존재?
        print("<%s> 궁합 음식은 <%s> 입니다."% (food,foods[food]))
    else :
        print("등록된 음식이 아닙니다.")
        #등록하는 프로그램 추가하기.
        #등록하시겠습니까(Y/N)? Y인 경우 등록,
        #                  그외는 다음 음식 등록으로 넘어감
    chk = input("음식을 등록하시겠습니까?(Y/N)")
    if chk.__eq__('Y') or chk.__eq__('y') :
        f = input("궁합음식을 입력하세요:")
        foods[food] = f
        print("등록되었습니다.")
        
    else : 
        continue
    
    
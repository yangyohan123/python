'''
Created on 2020. 1. 10.

@author: GDJ-19
'''


import operator
dic, list = {},[]
dic ={"Tomas":"토마스","Edword":"에드워드","Henry":"헨리",
      "Gothen":"고든","James":"제임스"}
# key=operator.itemgetter(0) : key값 기준으로 정렬
# reverse=True 역순
list = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
print(str(list[0]))
print(list)
list =sorted(dic.items(), key=operator.itemgetter(1))
print(list)
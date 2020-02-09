'''
Created on 2020. 1. 10.

@author: GDJ-19
리스트의 기본 함수
'''
mylist = [30,10,20]
print("리스트 : %s" % mylist)

mylist.append(40)
print("mylist.append(40) 후 리스트 : %s" % mylist)

print("pop() 메서드 결과: %s "% mylist.pop())
print("mylist.pop() 후 리스트 :%s" % mylist)

mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)

mylist.reverse()
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20값의 위치: %d"% mylist.index(20))
mylist.insert(2,222)
print("mylist.insert(2,222) 후 리스트 : %s"% mylist)
mylist.remove(222)
print("mylist.remove(222) 후 리스트 : %s"% mylist)
mylist.extend([77,88,99])
print("mylist.extend([77,88,99]) 후 리스트 : %s"% mylist)
print("77값의 개수: %d"% mylist.count(77))


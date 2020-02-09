'''
Created on 2020. 1. 20.

@author: GDJ-19
정규식 예제 3
'''
import re
string = "The quick brown fox jumps over the lazy dog"
string_list = string.split()
pattern = re.compile("The")
count = 0
for word in string_list :
    if pattern.search(word):
        count += 1
#the 문자 : 1개
print("output #1 :{1:s}:{0:d}".format(count, "갯수"))


#match_word : 이름부여
#re.I : 대소문자 상관없이 the라는 단어를 찾음
pattern = re.compile("(?P<match _word>The)", re.I)
print("output #2 :")
for word in string_list :
    if pattern.search(word):
        #pattern.search(word).group("match_word")) : group match_word에서 대소문자 상관없이 the를 찾아라
        #the
        #The
        print("{0}".format(pattern.search(word).group("match_word")))
    
#r"The" -> r:row데이터임을 알려줌
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
#the,The -> 'a'문자로 변경
# The quick brown fox jumps over the lazy dog
# a   quick brown fox jumps over a   lazy dog
print("output #3 : {0}".format(pattern.sub("a", string)))
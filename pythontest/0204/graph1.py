'''
Created on 2020. 2. 4.

@author: GDJ-19
그래프 그리기
'''
import matplotlib.pyplot as plt # pip install ggplot

## ggplot :그래프를 그려주는 모듈
plt.style.use("ggplot")


customers = ["JAVA", "JSP", "SPRING", "HADOOP", "PYTHON"]


customers_index = range(len(customers)) ## 0 ~ 4 인덱스

sale_amounts = [65,90,85,60,95] ## 데이터 리리스트 설정

fig = plt.figure() # 그래프 공간. 도화지
axl = fig.add_subplot(1,1,1) ## 1행 1열 1번째 그래프


# 막대 그래프 그리기
axl.bar(customers_index, sale_amounts, align="center",
        color="blue")
axl.xaxis.set_ticks_position("bottom") # x축 설정
axl.yaxis.set_ticks_position("left") # y축 설정

#x줄 표시 설정

plt.xticks(customers_index, customers, rotation=0,
           fontsize="small")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")

#이미지 저장하기- 파일로 저장해줌
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")

# 화면에 이미지 출력하기
plt.show()


# 맷플롯립 사용을 위해 넘파이도 함께 불러오기
import numpy as np
import matplotlib.pyplot as plt

# x축
x = np.array([1, 2, 3, 4, 5, 6, 7])

# y축
y = np.array([78.8, 78.4, 78.7, 78.5, 78.4, 79.2, 78.6])

# 그래프 스타일을 지정
# scatter() 함수 --> 산포도 형식으로 나타냄
plt.scatter(x, y, color="r")

# 그래프 출력
plt.show()
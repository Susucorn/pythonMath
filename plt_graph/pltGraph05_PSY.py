# 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt

# x축
x = np.linspace(-5, 5, 300)          # -5부터 5까지 샘플 개수 300개 지정

# y축
y1 = x ** 2
y2 = (x - 2) ** 2

# 그래프 스타일
plt.plot(x, y1, color="r")
plt.plot(x, y2, color="k", linestyle="--")

# 격자 바탕 표시
plt.grid()

# 그래프 출력
plt.show()
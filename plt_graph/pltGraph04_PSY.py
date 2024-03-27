# 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt

# x축
x = np.linspace(-5, 5)          # -5부터 5까지 샘플 개수 50개 지정, 샘플 개수는 기본값이 50

# y축
y1 = 2 * x
y2 = 5 * x

# 축 레이블
plt.xlabel("X-Axis", size=14)   # X축 레이블의 글꼴 크기 14
plt.ylabel("Y-Axis", size=14)   # y축 레이블의 글꼴 크기 14

# 그래프 제목
plt.title("Graph Title")

# 그리드 표시 - 격자 바탕
plt.grid()

# 범례 및 선 스타일 지정
plt.plot(x, y1, label="y1 value", color="r")                        # 빨간색
plt.plot(x, y2, label="y2 value", linestyle="dashed", color="k")    # 라인 스타일은 dotted(solid도 가능), 색상 지정

# 범례 표시
plt.legend()

# 화면에 그래프 출력
plt.show()
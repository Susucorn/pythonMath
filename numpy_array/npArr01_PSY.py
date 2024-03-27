'''
    넘파이(NumPy Numerical Python) : 선형대수와 같은 수치 계산과 행렬이나 대규모 다차원 배열 간의 연산을 위한 라이브러리
        - numpy의 기본 별칭 np
        - array() 함수로 파이썬 리스트 생성
'''
# 넘파이 라이브러리 
import numpy as np

# 1차원 배열 선언 및 초기화
arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("arr1 배열 : ", arr1)
print()

# 넘파이 배열 만들기
# np.zeros --> 요소 값이 모두 0인 배열을 만듦
print(np.zeros(4))      # 1차원 배열, 0이 4개
print(np.zeros(3))      # 1차원 배열, 0이 3개
print("0이 4개인 배열의 길이 : ", len(np.zeros(4)))

print()

# np.ones --> 요소 값이 모두 1인 배열을 만듦
print(np.ones((2, 3)))  # 2차원 배열
b = np.ones((2, 3))     
print(np.shape(b))      # 튜플 형태로 출력
print("b의 길이 : ", len(b))

print()

# 범위를 지정하여 배열을 생성
print("0 ~ 9까지 : ", np.arange(0, 10)) # 0부터 9까지
print("5 ~ 14까지 : ",np.arange(5, 15)) # 5부터 14까지

print()

# linespace() 함수 --> np.linespace(시작값, 마지막값, 샘플 개수)
print(np.linspace(0, 10, 11))   # 0과 10 사이의 요소 11개를 출력
print(np.linspace(0, 10, 3))    # 0과 10 사이의 요소 3개를 출력
print(np.linspace(0, 10, 1))    # 0과 10 사이의 요소 1개를 출력
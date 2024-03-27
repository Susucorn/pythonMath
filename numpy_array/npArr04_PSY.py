'''
    배열의 연산
        - 넘파이 배열은 배열과 스칼라값(숫자) 사이에서 연산을 수행
        - 연산 시 스칼라값이 배열과 각 원소에 적용됨
'''
# 넘파이 라이브러리 
import numpy as np

# 2차원 배열 생성
arr1 = np.array([[1, 2], [3, 4]])
print("arr1 : ", arr1)

# 배열 연산
print(arr1 + 3)     # 배열의 모든 요소에 3씩 더함
print()
print(arr1 * 2)     # 배열의 모든 요소에 2씩 곱합
print()
print(2 ** arr1)    # 배열의 모든 요소에 제곱
print()
print(arr1 / 2)     # 배열의 모든 요소를 2씩 나눔
print()
####################################################################################

# 2차원 배열 생성
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("a : ", a)
print("b : ", b)
print()

# 배열 연산
print(a + b)
print()
print(a - b)
print()
print(a * b)
print()
print(a / b)
print()
print(a ** b)
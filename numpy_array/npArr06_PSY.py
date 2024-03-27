'''
    넘파이의 다양한 기능
        - sum() 함수 --> 요소들의 합
        - average() --> 요소들의 평균
        - max() --> 요소들 중 제일 큰 값
        - min() --> 요소들 중 제일 작은 값
'''
# 넘파이 라이브러리 
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print("arr1 : ", arr1)
print()

# 함수로 출력
print("합계 : ", np.sum(arr1))
print("평균 : ", np.average(arr1))
print("최댓값 : ", np.max(arr1))
print("최소값 : ", np.min(arr1))

print()
print()

#####################################################################

# 2차원 배열 생성
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[6, 5, 4], [3, 2, 1]])
print("a : ", a)
print("b : ", b)

print()

# 두 배열의 사칙연산
print("두 배열의 덧셈 : ", a+b)
print()
print("두 배열의 뺼셈 : ", a-b)
print()
print("두 배열의 곱셈 : ", a*b)
print()
print("두 배열의 나눗셈 : ", a/b)

#####################################################################

# 1차원 배열 생성
aa = np.array([1, 2, 3, 4, 5])
print("aa 배열 : ", aa)

print("요소들의 합 : ", aa.sum())
print("요소들의 평균 : ", aa.mean())
print("요소들 중 최댓값 : ", aa.max())
print("요소들 중 최소값 : ", aa.min())
print()

# 2차원 배열 생성
bb = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("bb 배열 : ", bb)

print("요소들의 합 : ", bb.sum())
print("배열 행의 합 : ", bb.sum(axis=0))    # 가로
print("배열 열의 합 : ", bb.sum(axis=1))    # 세로
'''
    배열 관련 함수
        - np.zeros() --> 요소 값이 모두 0인 배열 생성
        - np.ones() --> 요소 값이 모두 1인 배열 생성
        - np.arange() --> 지정한 범위 값의 배열 생성
        - np.linespace() --> 지정한 범위 값의 배열 생성
'''
# 넘파이 라이브러리 
import numpy as np

# np.zeros() --> 요소 값이 모두 0인 배열 생성
arr1 = np.zeros(4)
print("arr1 : ", arr1)

arr2 = np.zeros((2, 3))
print("arr2 : ", arr2)

print()

# np.ones() --> 요소 값이 모두 1인 배열 생성
arr3 = np.ones(4)
print("arr3 : ", arr3)

arr4 = np.ones((2, 3))
print("arr4 : ", arr4)

print()

# np.arange() --> 지정한 범위 값의 배열 생성
arr5 = np.arange(0, 10, 1)
print("arr5 :", arr5)

arr6 = np.arange(0, 10, 2)
print("arr6 :", arr6)

print()

# np.linespace() --> 지정한 범위 값의 배열 생성
arr7 = np.linspace(0, 10, 11)
print("arr7 :", arr7)

arr8 = np.linspace(0, 10, 6)
print("arr8 :", arr8)
'''
    2024.03.13
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 리스트 --
'''
numlist = []

print("5개의 정수를 입력하세요.")
for i in range(5):
    num = int(input(f"{i+1}번째의 정수를 입력 : "))
    numlist.append(num)

print(numlist)
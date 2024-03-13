'''
    2024.03.13
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 연산자와 수식 --
'''
# 1. 사용자에게 어떤 동작을 할 지 알려주기
print("-- 정수 두 개 입력하기 --")

# 2. 입력받은 내용을 정수로 각각 저장하기
num1 = int(input("첫 번째 정수 : "))
num2 = int(input("두 번째 정수 : "))

print()

# 3. 출력하기
print(f"입력하신 두 개의 정수 {num1}과 {num2}로 연산을 시작하겠습니다.")
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} // {num2} = {num1//num2}")   # 몫
print(f"{num1} % {num2} = {num1%num2}")     # 나머지
print(f"{num1} ** {num2} = {num1**num2}")   # 거듭제곱
"""
문제 설명
정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ num1 ≤ 100
0 ≤ num2 ≤ 100
입출력 예
num1	num2	result
3	4	12
27	19	513
"""

#
# def solution(num1, num2):
#     return num1 * num2


if __name__ == '__main__':
    solution = lambda num1, num2: num1 * num2
    print(solution(3, 4))
    print(solution(27, 19))

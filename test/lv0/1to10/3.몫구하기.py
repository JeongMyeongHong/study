"""
문제 설명
정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
입출력 예
num1	num2	result
10	5	2
7	2	3
"""
# solution = lambda num1, num2: int(num1 / num2)
# solution2 = lambda num1, num2: num1 // num2
solution3 = int.__floordiv__

if __name__ == '__main__':
    print(solution3(10, 5))
    print(solution3(7, 2))

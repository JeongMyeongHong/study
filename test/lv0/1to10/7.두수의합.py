"""
문제 설명
정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

제한사항
-50,000 ≤ num1 ≤ 50,000
-50,000 ≤ num2 ≤ 50,000
입출력 예
num1	num2	result
2	3	5
100	2	102
"""
solution = lambda num1, num2: num1 + num2
solution2 = lambda *x: sum(x)

if __name__ == '__main__':
    print(solution(2, 3))
    print(solution(100, 2))

"""
문제 설명
정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ num1 ≤ 10,000
0 ≤ num2 ≤ 10,000
입출력 예
num1	num2	result
2	3	-1
11	11	1
7	99	-1
"""
solution = lambda num1, num2: 1 if num1 == num2 else -1

if __name__ == '__main__':
    print(solution(2, 3))
    print(solution(11, 11))
    print(solution(7, 99))

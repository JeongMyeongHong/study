"""
문제 설명
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

제한사항
0 < n ≤ 1000

입출력 예
n	result
10	30
4	6
"""

solution = lambda n: sum([i for i in range(2, n + 1, 2)])
solution2 = lambda n: sum([i for i in range(n // 2 + 1)]) * 2
solution3 = lambda n: sum([i if i % 2 == 0 else 0 for i in range(n + 1)])

if __name__ == '__main__':
    print(solution(10))
    print(solution(4))

'''문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
입출력 예
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]'''


def solution(x, n):
    return [i for i in range(x, x * (n + 1), x)] if not x == 0 else [0 for i in range(n)]


def solution2(x, n):
    return [i * x + x for i in range(n)]


if __name__ == '__main__':
    print(solution2(2, 5))
    print(solution2(4, 3))
    print(solution2(-4, 2))
    print(solution2(0, 2))

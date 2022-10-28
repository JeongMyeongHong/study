'''
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
입출력 예
num	return
3	"Odd"
4	"Even"
'''


def solution(num):
    return 'Odd' if num % 2 == 1 else 'Even'


def solution2(num):
    return ['Even', 'Odd'][num % 2]


if __name__ == '__main__':
    print(solution2(3))
    print(solution2(0))
    print(solution2(4))
    print(solution2(11))

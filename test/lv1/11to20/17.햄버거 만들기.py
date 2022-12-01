'''
문제 설명
햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다.
함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면
조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고,
상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다.
상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다.
상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며,
재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.
예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때,
상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고,
아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다.
즉, 2개의 햄버거를 포장하게 됩니다.
상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때,
상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.


제한사항
1 ≤ ingredient의 길이 ≤ 1,000,000
ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.


입출력 예 #1
ingredient	result
[2, 1, 1, 2, 3, 1, 2, 3, 1]	2


입출력 예 #2
[1, 3, 2, 1, 2, 1, 3, 1, 2]	0
상수가 포장할 수 있는 햄버거가 없습니다.
'''


def solution_v00(ingredient):
    ls = [ingredient[i:i + 4] for i in range(len(ingredient) - 3)]
    answer = 0
    a = [1, 2, 3, 1]
    while True:
        if a in ls:
            answer += 1
            index = ls.index(a)
            ingredient = ingredient[:index] + ingredient[index + 4:]
        else:
            break
        if len(ingredient) - 3 <= 0:
            break
        else:
            ls = [ingredient[i:i + 4] for i in range(len(ingredient) - 3)]
    return answer


def solution_v01(ingredient):
    answer = 0
    a = [1, 2, 3, 1]
    index = 0
    while True:
        if index + 3 >= len(ingredient):
            break
        cnt = 0
        for idx, val in enumerate(a):
            if ingredient[index + idx] != val:
                index += 1
                break
            cnt += 1
        if cnt == 4:
            answer += 1
            ingredient = ingredient[:index] + ingredient[index + 4:]
            index -= 2
    return answer


def solution_v02(ingredient):
    answer = 0
    target = '1231'
    ingredient = ''.join(map(str, ingredient))
    while True:
        if target in ingredient:
            idx = ingredient.index(target)
            ingredient = ingredient[:idx] + ingredient[idx + 4:]
            answer += 1
        else:
            break
    return answer


def solution(ingredient):
    answer = 0
    ls = []
    for material in ingredient:
        ls.append(material)
        if ls[- 4:] == [1, 2, 3, 1]:
            for _ in range(4):
                ls.pop()
            answer += 1
    return answer


if __name__ == '__main__':
    # ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    # print(solution(ingredient))
    # print(ingredient)
    # ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
    # print(solution(ingredient))
    # print(ingredient)
    ingredient = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    print('answer = ', solution(ingredient))
    print(ingredient)

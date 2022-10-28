import re

if __name__ == '__main__':
    content = '[재료] 북어포 1마리| 찹쌀가루 1C [샐러드 드레싱] 간장 2T| 설탕 1T| 물 1T| 다진파 1T| 다진마늘 1T| 참기름 1T| 깨소금 1T| 후춧가루 약간'
    ls = re.split(r'[|]', content)
    print(ls)
    category_pattern = re.compile('^(.+)?(\[.+\])(.+)?$')
    index_ls = [idx for idx, j in enumerate(ls) if category_pattern.findall(j)]
    index_ls.reverse()
    for idx in index_ls:
        squire_brace_ls = list(category_pattern.findall(ls[idx])[0])
        ls.remove(ls[idx])
        [ls.insert(idx, value) for value in reversed(squire_brace_ls)]
    values = list(filter(None, list(map(lambda s: s.strip(), ls))))
    index_ls = [idx for idx, j in enumerate(values) if category_pattern.findall(j)]
    categories = [values[i][1:-1] for i in index_ls]  # categories 에 [] 안에 있는 문자 앞에꺼 뒤에꺼 뽑아오기
    print(values)
    print(index_ls)
    print(categories)


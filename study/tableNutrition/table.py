import pandas as pd
import re
from tqdm import tqdm


def extract_information(df, i):
    title = df['요리명'][i]  # title 변수에 요리명 으로 되어있는 컬럼 가져오기
    recipe_num = str(df['레시피일련번호'][i])  # recipe_num 변수에 레시피일련번호 로 되어있는 컬럼 가져오기
    content = df['요리내용'][i]  # content 변수에 요리내용 으로 되어있는 컬럼 가져오기
    amount = df['요리인분명'][i][:1]  # amount 변수에 요리인분명 컬럼 문자열중 앞자리 하나 가져오기
    amount2 = df['요리인분명'][i]  # amount2 변수에 요리인분명으로 되어있는 컬럼 가져오기
    content2 = df['요리내용'][i]  # content2 변수에 요리내용으로 되어있는 컬럼 가져오기

    df2 = pd.DataFrame([recipe_num], columns=['레시피일련번호'])  # DataFrame 으로 바꾸기
    df_temp = pd.DataFrame([title], columns=['요리명'])
    df2 = pd.concat([df2, df_temp], axis=1)
    df_temp = pd.DataFrame([amount], columns=['요리인분명_no'])
    df2 = pd.concat([df2, df_temp], axis=1)
    df_temp = pd.DataFrame([amount2], columns=['요리인분명'])
    df2 = pd.concat([df2, df_temp], axis=1)
    df_temp = pd.DataFrame([content2], columns=['요리내용'])
    df2 = pd.concat([df2, df_temp], axis=1)

    ls = re.split(r'[|]', content)  # content를 | 기준으로 분할한 ls 생성
    category_pattern = re.compile('^(.+)?(\[.+\])(.+)?$')  # A [xx] B 를 가진 정규식
    index_ls = [idx for idx, j in enumerate(ls) if category_pattern.findall(j)]
    index_ls.reverse()
    for idx in index_ls:  # 기존에 있던 content list에 [재료]와 갇이 [XX]로 되어있는 요소를 분할해서 삽입
        squire_brace_ls = list(category_pattern.findall(ls[idx])[0])
        del ls[idx]
        [ls.insert(idx, value) for value in reversed(squire_brace_ls)]

    values = list(filter(None, list(map(lambda s: s.strip(), ls))))  # 좌우 공백 제거 및 비어 있는 요소 제거
    index_ls = [idx for idx, j in enumerate(values) if category_pattern.findall(j)]
    categories = [values[i][1:-1] for i in index_ls]  # [xx] 의 xx만 추출한 categories list 생성
    index_ls.append(len(values))

    column = ['재료명', '중량', '단위', '재료분류']  # 바꿀 컬럼명 지정
    mat_name = []  # mat_name 리스트 생성
    mat_wei = []  # mat_wei 리스트 생성
    mat_uni = []  # mat_uni 리스트 생성
    mat_cat = []  # mat_cat 리스트 생성
    # | 기준으로 나누기 숫자, ~+- 약간 적당량 꺼내오기
    # print(recipe_num)
    # print(content)
    # print(values)
    # print(categories)
    # print(index_ls)
    for i in range(len(index_ls) - 1):
        for j in range(index_ls[i] + 1, index_ls[i + 1]):
            val = values[j]
            _ = re.findall('\d\/\d|\d\-\d|\d\~\d|\d\+\d\/\d|\d|약간|적당량', val)
            # print(j, val)
            if _:
                if _[0].isdigit():
                    uni_idx = val.find(_[0])
                    mat_name.append(val[:uni_idx])
                    mat_wei.append(val[uni_idx:uni_idx + len(_)])
                    mat_uni.append(val[uni_idx + len(_):])
                else:
                    uni_idx = val.find(_[0])
                    mat_name.append(val[:uni_idx])
                    mat_wei.append(val[uni_idx:])
                    mat_uni.append('-')
            else:
                mat_name.append(val)
                mat_wei.append('-')
                mat_uni.append('-')
            mat_cat.append(categories[i])
    _ = pd.DataFrame(zip(mat_name, mat_wei, mat_uni, mat_cat),
                     columns=column)  # _ 데이터프레임화 matname,metwei,matuni,matcat 데이터zip 컬럼명은 column 안에 있는것으로 한다
    df2 = pd.concat([df2, _], axis=1)  # 데이터 연결하기 df2 안의 데이터와 _ 안의 데이터를 연결한다.
    df2['레시피일련번호'].fillna(recipe_num, inplace=True)
    df2['요리명'].fillna(title, inplace=True)
    df2['요리인분명_no'].fillna(amount, inplace=True)
    df2['요리인분명'].fillna(amount2, inplace=True)
    df2['요리내용'].fillna(content2, inplace=True)

    return df2


if __name__ == '__main__':
    file_name = '1)무료레시피데이터결과.csv'  # 경로지정
    df = pd.read_csv('./data/' + file_name, encoding='cp949', low_memory=False)  # csv파일 읽어오기한글깨짐 방지
    df.drop([df.index[0]], inplace=True)
    df.dropna(how='any', inplace=True)
    df.reset_index(drop=True, inplace=True)
    # df.to_csv('./save/' + '널제거'+file_name, encoding='cp949', index=False)  # (개발자 확인용)널값 제거 된 데이터셋
    df = df.head(1000)  # 헤드 n개 가져오기 (개발과정용, 모든 데이터 처리시 시간이 많이 걸려 n개로 제한)
    df2 = extract_information(df, 0)  # extract_information 메소드에 (df , 0) 파라미터 넣기
    df_list = []
    for i in tqdm(range(len(df))):
        recipe_num = str(df['레시피일련번호'][i])
        if recipe_num not in df2['레시피일련번호'].unique():  # 레시피 중복 방지
            df_list.append(extract_information(df, i))
    df2 = pd.concat(df_list,
                    ignore_index=True)  # i 변수에 레시피 일련번호 넣기 df3 extract_information메소드의 파라미터 df, i 에 레시피인련번호 유일한 값 찾아서 넣기
    df2.to_csv('./save/' + file_name, encoding='cp949', index=False)  # csv 파일 저장 한글깨짐 방지

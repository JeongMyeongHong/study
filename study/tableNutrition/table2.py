import pandas as pd
import re
from tqdm import tqdm


def extract_information(df, i):
    title = df['CKG_NM'][i]
    recipe_num = str(df['RCP_SNO'][i])
    content = df['CKG_MTRL_CN'][i]
    amount = df['CKG_INBUN_NM'][i][:1]

    p = re.compile(r'(?<=\[)(.*?)(?=])')
    ls = p.findall(content)
    print(ls)
    index_ls = [idx for idx, j in enumerate(ls) if j != '' and j[0] == '[']
    index_ls.append(len(ls))
    categories = [ls[i][1:-1] for i in index_ls[:-1]]
    values = [''.join(ls[index_ls[i] + 1:index_ls[i + 1]]) for i in range(len(index_ls) - 1)]
    print(values)

    df2 = pd.DataFrame([recipe_num], columns=['RCP_SNO'])
    df_temp = pd.DataFrame([title], columns=['CKG_NM'])
    df2 = pd.concat([df2, df_temp], axis=1)
    df_temp = pd.DataFrame([amount], columns=['CKG_INBUN_NM'])
    df2 = pd.concat([df2, df_temp], axis=1)

    column = ['재료명', '중량', '단위', '재료분류']
    mat_name = []
    mat_wei = []
    mat_uni = []
    mat_cat = []
    for i, v in enumerate(values):
        value = v.split('|')
        for val in value:
            ls = re.findall('[0-9./~+-]|약간|적당량', val)
            if len(ls) and len(ls[0]) == 1:
                point = val.index(ls[0])
                mat_name.append(val[:point])
                mat_wei.append(val[point:point + len(ls)])
                mat_uni.append(val[point + len(ls):])
                mat_cat.append(categories[i])
            elif len(ls) and len(ls[0]) != 1:
                point = val.index(ls[0])
                mat_name.append(val[:point])
                mat_wei.append('-')
                mat_uni.append(val[point:])
                mat_cat.append(categories[i])
            else:
                mat_name.append(val)
                mat_wei.append('-')
                mat_uni.append('-')
                mat_cat.append(categories[i])
    _ = pd.DataFrame(zip(mat_name, mat_wei, mat_uni, mat_cat), columns=column)
    df2 = pd.concat([df2, _], axis=1)
    df2['RCP_SNO'].fillna(recipe_num, inplace=True)
    df2['CKG_NM'].fillna(title, inplace=True)
    df2['CKG_INBUN_NM'].fillna(amount, inplace=True)
    return df2


if __name__ == '__main__':
    path = '1)무료레시피데이터결과.csv'
    df = pd.read_csv('./data/' + path, encoding='cp949', low_memory=False)
    df.drop([df.index[0]], inplace=True)
    df.dropna(how='any', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df = df.head(100)
    # print(df.head(10))
    df2 = extract_information(df, 0)
    for i in tqdm(range(len(df))):
        recipe_num = str(df['RCP_SNO'][i])
        if recipe_num not in df2['RCP_SNO'].unique():
            df3 = extract_information(df, i)
            df2 = pd.concat([df2, df3], ignore_index=True)

    print(df2)
    df2.to_csv('./save/' + path, encoding='cp949', index=False)

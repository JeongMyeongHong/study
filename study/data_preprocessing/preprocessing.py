import pandas as pd
import numpy as np
import re

'''
null값이 있는 데이터는 전부 제거.

레시피일련번호, 요리명, 스크랩수(이건 내가 참고할라곸ㅋㅋㅋㅋ), 요리방법, 요리내용(->[ ]는 떼어버리고 재료, 양만 저장)

drop_columns
 '레시피제목', '등록자ID', '등록자명', '조회수', '추천수', '요리상황별명', '요리재료별명', '요리종류별명', '요리소개', '요리인분명', '요리난이도명', '요리시간명', '최초등록일시'
'''


class Pre:
    def __init__(self, data_path='./data/', save_path='./save/'):
        self.data_path = data_path
        self.save_path = save_path

    def preprocessing(self, file_name=None):
        df = pd.read_csv(self.data_path + file_name + '.csv', encoding='cp949')
        df.dropna(inplace=True)
        material_df = df['요리내용']
        df.drop(columns=['레시피제목', '등록자ID', '등록자명', '조회수', '추천수',
                         '요리상황별명', '요리재료별명', '요리종류별명', '요리소개', '요리인분명',
                         '요리난이도명', '요리시간명', '최초등록일시', '요리내용'], inplace=True)
        material_df.rename('재료', inplace=True)
        print(material_df.head())
        p = re.compile(r'(?<=\[)(.*?)(?=])')
        for i in range(len(material_df[:20])):
            name_list = p.findall(material_df.iloc[i])
            print(name_list)
            for name in name_list:
                material_df.iloc[i] = material_df.iloc[i].replace(f'[{name}] ', '|')
                print(material_df.head())
            material_df.iloc[i] = ','.join([e.strip() for e in material_df.iloc[i].split('|')][1:])

        return pd.concat([df, material_df], axis=1)

    def visualizing(self):
        pass


if __name__ == '__main__':
    data = Pre().preprocessing('1)무료레시피데이터결과')
    print(data.columns, '\n\n')
    print(data.head())
    print(data['재료'].iloc[:10])

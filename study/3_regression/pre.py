import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder


class Regression:
    def __init__(self, data_path='../data/3_regression/', save_path='../save/3_regression/'):
        self.data_path = data_path
        self.save_path = save_path

    def preprocessing(self):
        file_name_train, file_name_test = 'FIFA_train', 'FIFA_test'
        train = pd.read_csv(self.data_path + file_name_train + '.csv')
        test = pd.read_csv(self.data_path + file_name_test + '.csv')

        # id, name컬럼 제거
        x_train = train.drop(['id', 'name'], axis=1)
        x_test = test.drop(['id', 'name'], axis=1)
        y_train = train['value']

        return x_train, y_train, x_test

    def corr(self):
        train = pd.read_csv(self.data_path + 'FIFA_train' + '.csv')
        # print(train.columns)
        # ['id', 'name', 'age', 'continent', 'contract_until', 'position',
        #        'prefer_foot', 'reputation', 'stat_overall', 'stat_potential',
        #        'stat_skill_moves', 'value']
        train.drop(['id', 'name'], axis=1, inplace=True)

        # contract_until 컬럼은 년도 외 나머지 숫자는 귀찮으니 일단 그냥 잘라버리자...
        # 고맙게도 베이스라인 코드에서 해줬음
        def func(string: object) -> int:
            """계약 연도만 추출하여 int로 반환"""
            string = string[-4:]
            return int(string)

        train['contract_until'] = train['contract_until'].apply(func)

        # 'continent', 'position', 'prefer_foot'
        # 3개의 컬럼은 인코딩을 해준다.
        le_col = ['continent', 'position', 'prefer_foot']
        encoders = [LabelEncoder() for _ in le_col]
        for (encoder, col) in zip(encoders, le_col):
            encoder.fit(train[col])
            train[col] = encoder.transform(train[col])


if __name__ == '__main__':
    obj = Regression()
    obj.corr()

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor

class Regression:
    def __init__(self, data_path='../data/3_regression/', save_path='../save/3_regression/'):
        self.data_path = data_path
        self.save_path = save_path

    @staticmethod
    def visualizing(df):
        columns = ['age', 'continent', 'contract_until',
                   'position', 'prefer_foot', 'reputation',
                   'stat_overall', 'stat_potential', 'stat_skill_moves']
        plt.figure(figsize=(12, 10))
        for i, column in enumerate(columns):
            plt.subplot(3, 3, i + 1)
            x = df[column].value_counts().index
            y = df[column].value_counts().values
            plt.bar(x, y)
            plt.title(column)
        plt.show()
        # print(df['age'].value_counts().index, df['age'].value_counts().values)

    def preprocessing(self):
        file_name_train, file_name_test = 'FIFA_train', 'FIFA_test'
        train = pd.read_csv(self.data_path + file_name_train + '.csv')
        # ['id', 'name', 'age', 'continent', 'contract_until', 'position',
        #        'prefer_foot', 'reputation', 'stat_overall', 'stat_potential',
        #        'stat_skill_moves', 'value']
        test = pd.read_csv(self.data_path + file_name_test + '.csv')
        df_ls = [train, test]

        # contract_until 컬럼은 년도 외 나머지 숫자는 귀찮으니 일단 그냥 잘라버리자...
        # 고맙게도 베이스라인 코드에서 해줬음
        # 추후에 변경할때 이것만 바꾸면 됨
        def contract_until_func(string: object) -> int:
            """계약 연도만 추출하여 int로 반환"""
            string = string[-4:]
            return int(string)

        for df in df_ls:
            df.drop(['id', 'name'], axis=1, inplace=True)
            df['contract_until'] = df['contract_until'].apply(contract_until_func)

        # 'continent', 'position', 'prefer_foot'
        # 3개의 컬럼은 인코딩을 해준다.
        # 이때 인코더 fit은 트레인의 인코더에 맞게 하고 transform은 train, test 두개 전부에 적용한다.
        le_col = ['continent', 'position', 'prefer_foot']
        encoders = [LabelEncoder() for _ in le_col]
        for (encoder, col) in zip(encoders, le_col):
            encoder.fit(train[col])
        y_train = df_ls[0]['value']
        df_ls[0].drop(['value'], axis=1, inplace=True)
        for df in df_ls:
            for (encoder, col) in zip(encoders, le_col):
                df[col] = encoder.transform(df[col])
            self.visualizing(df)
        scaler = MinMaxScaler()
        scaler.fit(df_ls[0])

        x_train = scaler.transform(df_ls[0])
        x_test = scaler.transform(df_ls[1])
        return x_train, y_train, x_test

    def predict(self, x_train, y_train, x_test, model):
        model = model
        model.fit(x_train, y_train)
        accuracy = accuracy_score(model.predict(x_train), y_train)
        print(accuracy)
        predict = model.predict(x_test)
        return predict, accuracy

    def submit(self, model):
        submission = pd.read_csv(self.data_path + 'submission.csv')
        x_train, y_train, x_test = self.preprocessing()
        submission['value'], _ = self.predict(x_train, y_train, x_test, model)
        # print(submission.head())
        submission.to_csv(self.data_path + 'submission.csv', index=False)
        return 'complete'


if __name__ == '__main__':
    obj = Regression()
    x_train, y_train, x_test = obj.preprocessing()
    obj.predict(x_train, y_train, x_test, LGBMClassifier())
    obj.predict(x_train, y_train, x_test, XGBClassifier())
    obj.predict(x_train, y_train, x_test, CatBoostRegressor())
    # print(obj.submit())

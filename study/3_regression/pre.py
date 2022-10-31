import pandas as pd


class Regression:
    def __init__(self, data_path='../data/3_regression/', save_path='../save/3_regression'):
        self.data_path = data_path
        self.save_path = save_path

    def preprocessing(self):
        file_name_train, file_name_test = 'FIFA_train', 'FIFA_test'
        train = pd.read_csv(self.data_path + file_name_train + '.csv', encoding='cp949')
        test = pd.read_csv(self.data_path + file_name_test + '.csv', encoding='cp949')

        return ''


if __name__ == '__main__':
    obj = Regression()
    print(obj.preprocessing())

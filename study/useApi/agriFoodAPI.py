import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from icecream import ic
import re
import numpy as np
import time


class FoodNutrition:
    def __init__(self):
        pass

    @staticmethod
    def find_food_info(code, food_group_code, food_name):
        params = {'serviceKey': code, 'Page_No': '1', 'Page_Size': '100',
                  'food_Group_Code': food_group_code,
                  'food_Name': food_name}
        url = 'http://apis.data.go.kr/1390802/AgriFood/MzenFoodCode/getKoreanFoodList'
        response = requests.get(url, params=params)
        soup = bs(response.text, "html.parser")
        food_codes = soup.select('items item food_Code')
        food_names = soup.select('items item food_Name')
        food_code_list = [code.text for code in food_codes]
        food_name_list = [name.text for name in food_names]
        columns = ['food_code', 'food_name']
        return pd.DataFrame(zip(food_code_list, food_name_list), columns=columns)

    def find_food_nutrition(self, code, food_group_code, food_name):
        df = self.find_food_info(code, food_group_code, food_name)
        ic(df)
        if not df.empty:
            tag_list = self.extract_tag(code, df)
            nutrition_list = self.sum_nutrition(code, df, tag_list)
            _df = pd.DataFrame(nutrition_list, columns=tag_list)
            df = pd.concat([df, _df], axis=1)
            # self.save_df(df, './save/' + food_group_code + '_' + food_name)
            ic('completed')
            return df

    @staticmethod
    def extract_tag(code, df):
        url = 'http://apis.data.go.kr/1390802/AgriFood/MzenFoodNutri/getKoreanFoodIdntList'
        params = {'serviceKey': code, 'food_Code': df.iloc[0]['food_code']}
        response = requests.get(url, params=params)
        soup = bs(response.content, "html.parser")
        idnt_list = soup.select('items item idnt_List')[0]
        parms = '(?:\w+\s*=\s*"[^"]*"\s")*'
        pattern = '(<\s*\w+\s*' + parms + '\s*/?>)'
        tag_list = [tag[1:-1] for tag in re.findall(pattern, str(idnt_list))[4:]]
        return tag_list

    @staticmethod
    def sum_nutrition(code, df, tag_list):
        url = 'http://apis.data.go.kr/1390802/AgriFood/MzenFoodNutri/getKoreanFoodIdntList'
        answer = []
        for _code in df['food_code']:
            params = {'serviceKey': code, 'food_Code': _code}
            response = requests.get(url, params=params)
            soup = bs(response.content, "html.parser")
            idnt_list = [list(map(float, [soup.select('items item idnt_List ' + tag)[i].text for tag in tag_list]))
                         for i in range(len(soup.select('items item idnt_List ')))]
            idnt_list = [round(i, 1) for i in np.sum(idnt_list, axis=0)]
            idnt_list = list(map(str, idnt_list))
            answer.append(idnt_list)
            time.sleep(0.6)
        return answer

    @staticmethod
    def save_df(df, path):
        df.to_csv(path, ',', index=False)


if __name__ == '__main__':
    encoding_code = 'XyZfkg6oI9Tp1vOx3hIT4TeVbuShcJn321HjGZaLJQA8DMEdd8vTaYmpFliDpyLd9Q1Ojb7l1WUH8PwBvNGfjw%3D%3D'
    decoding_code = 'XyZfkg6oI9Tp1vOx3hIT4TeVbuShcJn321HjGZaLJQA8DMEdd8vTaYmpFliDpyLd9Q1Ojb7l1WUH8PwBvNGfjw=='
    encoding_code2 = 'P%2BgjMNmfc9Uq4qzqMGq%2BjlweWAwpg7WxRP%2FQfUiRF6cMF%2F9sA5T%2B0Ke6aquz4rIyHMK6h0ynUMgwDJuaajWvmg%3D%3D'
    decoding_code2 = 'P+gjMNmfc9Uq4qzqMGq+jlweWAwpg7WxRP/QfUiRF6cMF/9sA5T+0Ke6aquz4rIyHMK6h0ynUMgwDJuaajWvmg=='
    food_group_code = '08'
    # {'밥류': '01', '빵,과자류': '02', '면,만두류': '03', '죽류': '04', '국,탕류': '05', '찌개류': '06', '찜류': '07', '구이류': '08',
    #  '전류': '09', '볶음류': '10', '무침류': '13', '김치,장아찌': '14', '회류': '15', '젓갈류': '16', '양념류': '18', '유제품': '19',
    #  '음료및주류': '20', '과일류': '21', '단품류': '22', '떡류': '23'}
    food_name = '돼지고기'
    df = FoodNutrition().find_food_nutrition(decoding_code, food_group_code, food_name)

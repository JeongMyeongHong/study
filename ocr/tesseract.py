import pytesseract
import cv2
import pandas as pd
import numpy as np
import os
from tqdm import tqdm

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Solution:
    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        self.img = cv2.imread(path + file_name, cv2.IMREAD_GRAYSCALE)

    def get_xy(self):
        img = self.img
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
        # using RETR_EXTERNAL instead of RETR_CCOMP
        contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        mask = np.zeros(bw.shape, dtype=np.uint8)
        coordinates = []

        for idx in range(len(contours)):
            x, y, w, h = cv2.boundingRect(contours[idx])
            mask[y:y + h, x:x + w] = 0
            cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
            r = float(cv2.countNonZero(mask[y:y + h, x:x + w])) / (w * h)
            if r > 0.45 and w > 8 and h > 8:
                coordinates.append((x, y, w, h))
                # cv2.rectangle(img, (x, y), (x + w - 1, y + h - 1), (0, 255, 0), 2)

        # mul = 0.8  # 사진의 창이 너무 커서 0.8배로 줄였음. 이 숫자 변경 하면 배율 변함
        # cv2.namedWindow('view', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('view', round(img.shape[1] * mul), round(img.shape[0] * mul))
        # cv2.imshow('view', img)
        # cv2.waitKey()

        return coordinates

    def divide_image(self):
        img = self.img
        columns = ['Date', '1', '2', '3', '4', 'net']
        df = pd.DataFrame(columns=columns)
        coordinates = self.get_xy()
        res = []
        for coordinate in tqdm(coordinates):
            x, y, w, h = coordinate
            extra_point = 7
            x, y = x - extra_point, y - extra_point
            w, h = w + extra_point * 2, h + extra_point * 2
            cropped_image = img[y:y + h, x:x + w]
            # cv2.imwrite('./save/'+str(coordinate)+'.jpg', cropped_image)
            answer = pytesseract.image_to_string(cropped_image, lang='kor')
            # print('\n' + str(coordinate) + ' 의 결과 : ' + answer)
            # cv2.imshow(' ', cropped_image)
            # cv2.waitKey()
            res.append(' '.join(list(filter(None, answer.split('\n')))))
        # res = pd.DataFrame(data=[res], columns=columns)
        print(res)
        # df = pd.concat([df, res])
        # df.reset_index(drop=True, inplace=True)
        return df


data_path = './data/'
save_path = './save/'
file_names = os.listdir(data_path)
print(file_names)
#  # ['1.png', '1665019485641.jpg', '1665019486684.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', 'NIA.jpg', 'row.jpg']
file_index = -1
print(f'File name : {file_names[file_index]}')
solution = Solution(path=data_path, file_name=file_names[file_index])
print(solution.divide_image())

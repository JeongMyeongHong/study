import pytesseract
import cv2
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Solution:
    def __init__(self, path, file_name, num_row):
        self.path = path
        self.file_name = file_name
        self.num_row = num_row

    def divide_image(self):
        img = cv2.imread(self.path + self.file_name, cv2.IMREAD_GRAYSCALE)
        columns = ['Date', '1', '2', '3', '4', 'net']
        df = pd.DataFrame(columns=columns)
        row_points = [round(img.shape[0] / num_row * i) for i in range(num_row + 1)]
        col_points = [0, round(img.shape[1] / 6 * 1.3),
                      round(img.shape[1] / 6 * 2.3), round(img.shape[1] / 6 * 3.1),
                      round(img.shape[1] / 6 * 4.1), round(img.shape[1] / 6 * 5.1),
                      img.shape[1]]
        for i in range(len(row_points) - 1):
            res = []
            for j in range(len(col_points) - 1):
                cropped_image = img[row_points[i]:row_points[i + 1],
                                col_points[j]:col_points[j + 1]]
                # cv2.imshow('cropped_image', cropped_image)
                # cv2.waitKey(500)
                lang = 'Kor' if j == 0 else None

                res.append(' '.join(list(filter(None,
                                                pytesseract.image_to_string(
                                                    cropped_image, lang=lang).split('\n')))))
            res = pd.DataFrame(data=[res], columns=columns)
            df = pd.concat([df, res])
        df.reset_index(drop=True, inplace=True)
        return df


path = './data/'
file_names = ['1665019485641.jpg', '1665019486684.jpg', 'NIA.jpg']
file_index = 2
num_row = 13
solution = Solution(path=path, file_name=file_names[file_index], num_row=num_row)

print(solution.divide_image())

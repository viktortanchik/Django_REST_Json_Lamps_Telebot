# Запись

import _csv
#import psutil
with open("test_csv.csv", mode="a", encoding='utf-8') as w_file:
    file_writer = _csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Тип АКБ", "Емкость,mAh", "Цена для клиентов,грн", "На складе"])
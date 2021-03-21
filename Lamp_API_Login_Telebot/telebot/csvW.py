# Запись
import _csv
#import psutil
def CSV_W():
    with open("test_csv.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = _csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["tert","sn"])
    w_file.close()
CSV_W()
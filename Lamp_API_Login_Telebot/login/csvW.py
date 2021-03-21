# Запись
import _csv
#import psutil
def CSV_W(name,SN):
    with open("F:\Python\Django_lamps_Json_login_telebot_002\Lamp_API_Login_Telebot\login/test_csv.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = _csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow([name,SN])
    w_file.close()

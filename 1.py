print("Задание #1")
import datetime
n = int(input("Введите секунды: "))
time_format = str(datetime.timedelta(seconds = n))
print("Результат: ",time_format)
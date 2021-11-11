"""1. Реализовать вывод информации о промежутке времени
в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек."""
# 1 сутки = 86400 сек
# 1 час = 3600 сек
# 1 мин = 60 сек
duration = int(input("Введите продолжительность времени в секундах: "))

days = duration // 86400
hours = (duration - (days * 86400)) // 3600
minutes = (duration - (days * 86400) - (hours * 3600)) // 60
seconds = duration % 60
if duration < 60:
    print(f"{duration} сек")
elif 60 <= duration < 3600:
    print(f"{minutes} мин {seconds} сек")
elif 3600 <= duration < 86400:
    print(f"{hours} час {minutes} мин {seconds} сек")
elif duration >= 86400:
    print(f"{days} дн {hours} час {minutes} мин {seconds} сек")

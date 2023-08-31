#Громов Марсбек 31/08
import random
from random import randint

#Класс маршрута
class Way():
    def __init__(self, A, B):
        self.a = A
        self.b = B

#Поиск подходящих заказов
def podhod_zakazi(zakazi, A, B):
    spisok_zakazov = []  #---------------------------------------Подходящие заказы
    spisok_adress = [     #---------------------------------------Некая БД адресов
        'Ильменская',
        'Петровского',
        'Чайковского',
        'Маяковского',
        'Билибина'
    ]
    for zakaz in zakazi:
        if zakaz.a == A and zakaz.b == B: #----------------------Приоритет, определяет заказ совпадающий с маршрутом водителя
            spisok_zakazov.append((zakaz.a, zakaz.b))
        elif zakaz.a != A and zakaz.b == B: #--------------------Альтернатива, в случае если до пассажира некое расстояние
            spisok_zakazov.append((zakaz.a, zakaz.b))
    spisok_zakazov.sort(reverse=False) #-------------------------Сортировка заказов по расстоянию от меньшего к большему к водителю
    for i in range(len(spisok_zakazov)):
        if i == 0:
            print("Подходящие заказы по вашему маршруту: ") #------------------------------------Маршрут водителя Лермонова - Дзержинского
            print(f' Заказ: Лермонтова{spisok_zakazov[i][0]} - Дзержинского{spisok_zakazov[i][1]}')
        else:
            print(f' Заказ: {random.choice(spisok_adress)}{spisok_zakazov[i][0]} - Дзержинского{spisok_zakazov[i][1]}')

#Массив с рандомными заказами до Б, в том числе по заданному маршруту
zakazi = [Way((0, 0), (9, 9))]
zakazi += [Way((randint(0, 9), randint(0, 9)), (randint(0, 9), randint(0, 9))) for j in range(500)]

#Маршрут водителя
A = (0, 0) #Отправная точка
B = (9, 9) #Конечная

#Вывод найденных
search_zakaz = podhod_zakazi(zakazi, A, B)


